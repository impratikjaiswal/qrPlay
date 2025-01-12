import io
import os
from importlib.resources import files

import segno
from PIL import Image
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
    logo = prepare_logo(logo_path=None,
                        file_path=meta_data.output_file_path) if data.decorate_qr and data.output_format in FormatsGroup.OUTPUT_FORMATS_PNG_IMAGES else None
    if data.split_qrs:
        qrcode_split = segno.make_sequence(data.input_data, version=data.qr_code_version)
        sequence_count = len(qrcode_split)
        print(f'sequence_count is {sequence_count}')
        # qrcode_split.save(file_path, scale=data.size)
        temp_output = []

        for index, qrcode in enumerate(qrcode_split, start=1):
            output_file = PhUtil.append_in_file_name(meta_data.output_file_path, str_append=['item', str(index)])
            res_curr = handle_individual_qr_code(data, meta_data, qrcode, logo, output_file)
            print()
            temp_output.append(res_curr)
        res = temp_output
    else:
        qrcode = segno.make(data.input_data, version=data.qr_code_version)
        # qrcode = segno.make(data.input_data, error='h')
        res = handle_individual_qr_code(data, meta_data, qrcode, logo, meta_data.output_file_path)
    return res


def handle_individual_qr_code(data, meta_data, qrcode, logo, file_path):
    print(f'individual data_length is {len(data.input_data)}')
    # print(f'mode is {qrcode.mode}')
    # print(f'error is {qrcode.error}')
    # print(f'version is {qrcode.version}')
    # print(f'default_border_size is {qrcode.default_border_size}')
    # print(f'designator is {qrcode.designator}')
    # print(f'is_micro is {qrcode.is_micro}')
    if data.output_format == Formats.SVG_URI:
        output = qrcode.svg_data_uri(scale=data.size)
    elif data.output_format == Formats.PNG_URI:
        output = qrcode.png_data_uri(scale=data.size)
    else:
        output = file_path
        qrcode.save(file_path, scale=data.size)
    #
    if logo and data.output_format in FormatsGroup.OUTPUT_FORMATS_PNG_IMAGES:
        qrcode_io_bytes = io.BytesIO()
        # Nothing special here, let Segno generate the QR code and save it as PNG in a buffer
        qrcode.save(qrcode_io_bytes, scale=data.size, kind='png')
        qrcode_io_bytes.seek(0)  # Important to let Pillow load the PNG
        output = attach_logo(data, meta_data, qrcode_io_bytes, logo, file_path)
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
    # logo_path = PhUtil.set_if_none(logo_path, Folders.in_res_images('pj_crop.png'))
    if logo_path is None:
        resource_path = files('qr_play.res')
        logo_path = resource_path.joinpath(os.sep.join(['images', 'pj_crop.png']))
        print(f'logo_path: {logo_path}')
    corner_radios_logo = 0
    source_color_rgb = (255, 255, 255)  # white
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
        logo_img = QrUtil.add_borders(logo_img, border_width=50, fill_color='brown')
    if corner_radios_logo > 0:
        logo_img = QrUtil.add_corners(logo_img, corner_radios_logo)  # Ensure Corners
    if save_logo:
        logo_image_path = PhUtil.append_in_file_name(file_path, str_append=['logo'])
        logo_img.save(fp=logo_image_path)
    return logo_img


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
    if data.output_format == Formats.SVG_URI:
        pass
    elif data.output_format == Formats.PNG_URI:
        output = QrUtil.image_to_uri(img, input_format=PhFormats.PNG)
    else:
        output = file_path
        img.save(fp=file_path)
    return output
