import io
import os
from importlib.resources import files

import segno
from PIL import Image, ImageDraw, ImageFont
from python_helpers.ph_colors import PhColors
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_formats import PhFormats
from python_helpers.ph_util import PhUtil

from qr_play.main.helper.formats import Formats
from qr_play.main.helper.formats_group import FormatsGroup
from qr_play.main.helper.util import Util as QrUtil

show_image = False


def handle_data(data, meta_data, info_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param info_data:
    :param flip_output:
    :return:
    """
    input_data = data.input_data
    # input_File_path = meta_data.input_data_org if meta_data.input_mode_key == PhKeys.INPUT_FILE else None
    # input_format = data.input_format
    # output_format = data.output_format
    # if flip_output is True:
    #     input_data = meta_data.parsed_data
    #     input_format = data.output_format
    #     output_format = data.input_format
    # parse_only = True
    # asn1_element = data.asn1_element
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    res = __handle_data(data=data, meta_data=meta_data, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res


def __handle_data(data, meta_data, info_data):
    info_data_available = False if PhUtil.is_none(info_data) else True
    # TODO: for debugging
    # PhUtil.to_file(output_lines=data.input_data, back_up_file=True)
    # PhUtil.print_iter(data, header='data')
    # TODO: In future, logo_path should be user specific path ( / uploaded image)
    logo = None
    if data.output_format in FormatsGroup.OUTPUT_FORMATS_PNG_IMAGES:
        if data.decorate_qr:
            logo = prepare_logo(logo_path=None, file_path=meta_data.output_file_path)
    if data.split_qrs:
        qrcode_split = segno.make_sequence(data.input_data, version=data.qr_code_version)
        sequence_count = len(qrcode_split)
        multi_qrs = True if sequence_count > 1 else False
        if multi_qrs:
            print(f'sequence_count is {sequence_count}')
        # qrcode_split.save(file_path, scale=data.size)
        temp_output = []
        for index, qrcode in enumerate(qrcode_split, start=1):
            output_file = PhUtil.append_in_file_name(meta_data.output_file_path, str_append=['item',
                                                                                             str(index)]) if multi_qrs else meta_data.output_file_path
            res_curr = handle_individual_qr_code(data, meta_data, qrcode, logo, output_file)
            temp_output.append(res_curr)
        res = temp_output
    else:
        qrcode = segno.make(data.input_data, version=data.qr_code_version)
        # qrcode = segno.make(data.input_data, error='h')
        res = handle_individual_qr_code(data, meta_data, qrcode, logo, meta_data.output_file_path)
    return res


def handle_individual_qr_code(data, meta_data, qrcode, logo, file_path):
    # Default Border
    border = None
    # PlayGround
    # border = 1
    #
    # Debug data
    #
    # print(f'version is {qrcode.version}')
    # print(f'error is {qrcode.error}')
    # print(f'mode is {qrcode.mode}')
    # print(f'default_border_size is {qrcode.default_border_size}')
    # print(f'designator is {qrcode.designator}')
    # print(f'is_micro is {qrcode.is_micro}')
    if data.output_format == Formats.SVG_URI:
        output = qrcode.svg_data_uri(scale=data.size, border=border)
    elif data.output_format == Formats.PNG_URI:
        output = qrcode.png_data_uri(scale=data.size, border=border)
    else:
        output = file_path
        qrcode.save(file_path, scale=data.size, border=border)
    #
    if data.output_format in FormatsGroup.OUTPUT_FORMATS_PNG_IMAGES:
        if logo:
            qrcode_io_bytes = io.BytesIO()
            # Nothing special here, let Segno generate the QR code and save it as PNG in a buffer
            qrcode.save(qrcode_io_bytes, scale=data.size, kind='png', border=border)
            qrcode_io_bytes.seek(0)  # Important to let Pillow load the PNG
            output = attach_logo(data, meta_data, qrcode_io_bytes, logo, file_path)
        if data.label:
            output = attach_label(data, meta_data, output)
    open_image(data, output)
    return output


def open_image(data, file_path):
    if data.quite_mode or not data.print_output:
        return
    if show_image:
        if data.output_format in FormatsGroup.OUTPUT_FORMATS_IMAGE_FILES:
            with Image.open(file_path) as img:
                print(f'File Path: {img.filename}')
                print(f'File Size: {PhUtil.get_file_size(file_path)}')
                print(f'File Format (& Description): {img.format} ({img.format_description})')
                # print(f'File Dimensions (width): {img.width}')
                # print(f'File Dimensions (height): {img.height}')
                print(f'File Dimensions (width, height): {img.size}')
                img.show()


def prepare_logo(logo_path=None, file_path=None):
    # Default Values
    if logo_path is None:
        resource_path = files('qr_play.res')
        logo_path = resource_path.joinpath(os.sep.join(['images', 'pj_crop.png']))
        # print(f'logo_path: {logo_path}')
    corner_radios_logo = 0
    source_color_rgb = PhColors.WHITE
    target_color_rgb = None
    source_color_negation = True
    add_border = False
    save_logo = True
    #
    # Play ground
    corner_radios_logo = 90
    # source_color_negation = False
    # add_border = True
    # save_logo = False
    ###
    # Logo image
    logo_img = Image.open(logo_path)  # The logo
    if target_color_rgb is not None:
        logo_img = QrUtil.change_colors(logo_img, source_color_rbg=source_color_rgb,
                                        target_color_rgb=target_color_rgb,
                                        source_color_negation=source_color_negation)
    if add_border:
        logo_img = QrUtil.add_borders(logo_img, border_width=50, fill_color=PhColors.BROWN)
    if corner_radios_logo > 0:
        logo_img = QrUtil.add_corners(logo_img, corner_radios_logo)  # Ensure Corners
    if save_logo:
        logo_image_path = PhUtil.append_in_file_name(file_path, str_append=['logo'])
        logo_img.save(fp=logo_image_path)
    return logo_img


def get_text_width_height(image_width, image_height, text, font):
    # Create a blank canvas
    canvas = Image.new('RGB', (image_width, image_height))
    draw = ImageDraw.Draw(canvas)
    draw.text((1, 1), text, font=font, fill=PhColors.WHITE)
    # Find bounding box
    bbox = canvas.getbbox()
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    return text_width, text_height


def append_padding(image_width, image_height, padding_location, padding_value):
    padding_top = 0
    padding_bottom = 0
    padding_left = 0
    padding_right = 0
    padded_image_top = 0
    padded_image_left = 0
    sep_line_start = (0, 0)
    sep_line_end = (0, 0)
    if padding_location == PhConstants.Position.TOP:
        padding_top = padding_value
        padded_image_top = 0
        sep_line_start = (0, padding_top)
        sep_line_end = (image_width, padding_top)
    if padding_location == PhConstants.Position.BOTTOM:
        padding_bottom = padding_value
        padded_image_top = image_height
        sep_line_start = (0, padded_image_top)
        sep_line_end = (image_width, padded_image_top)
    if padding_location == PhConstants.Position.LEFT:
        padding_left = padding_value
        padded_image_left = 0
        sep_line_start = (padding_left, 0)
        sep_line_end = (padding_left, image_height)
    if padding_location == PhConstants.Position.RIGHT:
        padding_right = padding_value
        padded_image_left = image_width
        sep_line_start = (image_width, 0)
        sep_line_end = (image_height, image_width)
    image_width_new = image_width + padding_right + padding_left
    image_height_new = image_height + padding_top + padding_bottom
    new_image_size = (image_width_new, image_height_new)
    # padded_image_size = (
    #     image_width_new if (image_width_new - image_width) > 0 else image_width,
    #     image_height_new if (image_height_new - image_height) > 0 else image_height,
    # )
    padded_image_size = (
        image_width_new - image_width,
        image_height_new - image_height
    )
    actual_image_position = (padding_left, padding_top)
    padded_image_position = (padded_image_left, padded_image_top)
    line_position = [sep_line_start, sep_line_end]
    return new_image_size, actual_image_position, padded_image_size, padded_image_position, line_position


def attach_label(data, meta_data, input_img_path):
    """

    :param data:
    :param meta_data:
    :param input_img_path:
    :return:
    """
    label_position = data.label_position
    label = data.label
    # font_name = 'FreeMono.ttf'
    # font_name = 'andale-mono.ttf'
    font_name = 'DejaVuSans.ttf'
    font_size = 25
    text_color = PhColors.BLACK.hex_format()
    padding_factor = 2
    #
    # Play ground
    # padding_bottom = 100

    # font_size = 36
    # text_color = PhColors.RED.hex_format()
    # Default Values
    """
    Load the image
    """
    if data.output_format == Formats.PNG_URI:
        image = QrUtil.uri_to_image(input_img_path)
    else:
        image = Image.open(input_img_path)
    image_width, image_height = image.size
    print(f'image_width: {image_width}')
    print(f'image_height: {image_height}')
    """
    Prepare Text
    """
    # Custom font style and font size
    resource_path = files('qr_play.res')
    font_path = resource_path.joinpath(os.sep.join(['fonts', font_name]))
    # print(f'font_path: {font_path}')
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = get_text_width_height(image_width, image_height, label, font)
    print(f'text_width: {text_width}')
    print(f'text_height: {text_height}')
    """
    Append Padding (Space for Text)
    """
    padding_value = 0
    if label_position in [PhConstants.Position.BOTTOM, PhConstants.Position.TOP]:
        padding_value = text_height
    if label_position in [PhConstants.Position.LEFT, PhConstants.Position.RIGHT]:
        padding_value = text_width
    if padding_factor:
        padding_value *= padding_factor
    new_image_size, actual_image_position, padded_image_size, padded_image_position, line_position = append_padding(
        image_width,
        image_height,
        padding_location=label_position,
        padding_value=padding_value)
    image_w_padding = Image.new(image.mode, new_image_size, PhColors.WHITE.hex_format())
    image_w_padding.paste(image, actual_image_position)
    """
    Start Drawling (Create a drawing contextm (add 2D graphics in an image))
    """
    draw = ImageDraw.Draw(image_w_padding)
    """
    Add Sep line
    """
    draw.line(line_position, fill=PhColors.BLUE.hex_format())
    """
    Add Text
    """
    # Calculate the position to center the text
    x = padded_image_size[0] if padded_image_size[0] > 0 else image_width
    y = padded_image_size[1] if padded_image_size[1] > 0 else image_height
    x = padded_image_position[0] + (x - text_width) // 2
    y = padded_image_position[1] + (y - text_height) // 2
    # Add text to the image
    draw.text((x, y), label, fill=text_color, font=font)
    # output_img_path = PhUtil.append_in_file_name(input_img_path, str_append=['w', 'label'])
    output_img_path = input_img_path
    if data.output_format == Formats.PNG_URI:
        output = QrUtil.image_to_uri(image_w_padding, input_format=PhFormats.PNG)
    else:
        output = output_img_path
        image_w_padding.save(fp=output_img_path)
    return output


def attach_logo(data, meta_data, qrcode_io_bytes, logo_img, file_path):
    # preferred 4 or 3
    logo_image_ratio = 4
    corner_radios_whole_qr = 0
    #
    # Play ground
    logo_image_ratio = 4
    corner_radios_whole_qr = 15
    # source_color_negation = False
    ##
    # QR image
    img = Image.open(qrcode_io_bytes)
    img = img.convert('RGB')  # Ensure colors for the output
    if corner_radios_whole_qr > 0:
        img = QrUtil.add_corners(img, corner_radios_whole_qr)  # Ensure Corners
    img_width, img_height = img.size
    # Calculate the center of the QR code
    logo_max_size = img_height // logo_image_ratio
    # Resize the logo to logo_max_size
    logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
    box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
    img.paste(logo_img, box)
    if data.output_format == Formats.PNG_URI:
        output = QrUtil.image_to_uri(img, input_format=PhFormats.PNG)
    else:
        output = file_path
        img.save(fp=file_path)
    return output
