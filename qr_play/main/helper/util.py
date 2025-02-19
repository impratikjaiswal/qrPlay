import base64
import io

import numpy as np
from PIL import Image, ImageDraw, ImageOps
from python_helpers.ph_colors import PhColors
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_formats import PhFormats, PhMimeTypes


class Util:
    @classmethod
    def get_colors(cls, im):
        # im = im.convert("P")
        im = im.convert('RGB')
        # getting colors
        im1 = Image.Image.getcolors(im)
        print(im1)

    @classmethod
    def change_colors(cls, im,
                      source_color_rbg=PhColors.WHITE,
                      target_color_rgb=PhColors.RED,
                      source_color_negation=True,
                      ):
        cls.get_colors(im)
        im = im.convert('RGBA')
        data = np.array(im)  # "data" is a height x width x 4 numpy array
        red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability
        source_red = source_color_rbg[0]
        source_green = source_color_rbg[1]
        source_blue = source_color_rbg[2]
        # Replace white with red... (leaves alpha values alone...)
        white_areas = (red == source_red) & (green == source_green) & (blue == source_blue)
        non_white_areas = (red != source_red) | (green != source_green) | (blue != source_blue)
        if source_color_negation:
            data[..., :-1][non_white_areas.T] = target_color_rgb  # Transpose back needed
        else:
            data[..., :-1][white_areas.T] = target_color_rgb  # Transpose back needed
        im2 = Image.fromarray(data)
        return im2

    @classmethod
    def add_borders(cls, im, border_width, fill_color):
        im = ImageOps.expand(im, border=border_width, fill=fill_color)
        return im

    @classmethod
    def add_corners(cls, im, rad):
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        alpha = Image.new('L', im.size, "white")
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im

    @classmethod
    def image_to_uri(cls, im, input_format=PhFormats.PNG, encoding=PhConstants.CHAR_ENCODING_UTF8):
        """
        Ref: https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types#image_types

        :param im:
        :param input_format: image/jpeg, image/png, and image/svg+xml
        :param encoding:
        :return:
        """
        buff = io.BytesIO()
        im.save(buff, format=input_format)
        return f'data:{PhMimeTypes.format_to_mimetype_mappings.get(input_format)};base64,{base64.b64encode(buff.getvalue()).decode(encoding)}'


class Shapes:
    SQUARE = 1
    ROUNDED = 2


class ShapesAttributes:
    ROUNDED_CORNER = 2
