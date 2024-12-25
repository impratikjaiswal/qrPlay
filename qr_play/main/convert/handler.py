import segno
from PIL import Image
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from qr_play.main.helper.formats import Formats

show_image = False


def handle_individual_qr_code(data, meta_data, qrcode, file_path):
    print(f'individual data_length is {len(data.input_data)}')
    # print(f'mode is {qrcode.mode}')
    # print(f'error is {qrcode.error}')
    # print(f'version is {qrcode.version}')
    # print(f'default_border_size is {qrcode.default_border_size}')
    # print(f'designator is {qrcode.designator}')
    # print(f'is_micro is {qrcode.is_micro}')
    if data.image_format == Formats.SVG_URI:
        output = qrcode.svg_data_uri(scale=data.scale)
    elif data.image_format == Formats.PNG_URI:
        output = qrcode.png_data_uri(scale=data.scale)
    else:
        output = file_path
        qrcode.save(file_path, scale=data.scale)
    if show_image:
        if data.image_format == Formats.PNG and data.print_output and not data.quite_mode:
            with Image.open(file_path) as img:
                img.show()
    return output


def handle_qr_code(data, meta_data, info_data):
    print(f'full data_length is {len(data.input_data)}')
    # TODO: for debugging
    # PhUtil.to_file(output_lines=data.input_data, back_up_file=True)
    # PhUtil.print_iter(data, header='data')
    if data.split_qrs:
        qrcode_split = segno.make_sequence(data.input_data, version=data.qr_code_version)
        sequence_count = len(qrcode_split)
        print(f'sequence_count is {sequence_count}')
        # qrcode_split.save(file_path, scale=data.scale)
        temp_output = []
        for index, qrcode in enumerate(qrcode_split, start=1):
            output_file = PhUtil.append_in_file_name(meta_data.output_file, str_append=['item',
                                                                                        str(index)]) if meta_data.file_based else meta_data.output_file
            res = handle_individual_qr_code(data, meta_data, qrcode, output_file)
            print()
            temp_output.append(res)
        res = temp_output
    else:
        qrcode = segno.make(data.input_data, version=data.qr_code_version)
        # qrcode = segno.make(data.input_data, error='h')
        res = handle_individual_qr_code(data, meta_data, qrcode, meta_data.output_file)
    return res


def process_data(data, meta_data, info_data, flip_output=False):
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
    # Handle Qr Code
    res = handle_qr_code(data=data, meta_data=meta_data, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res
