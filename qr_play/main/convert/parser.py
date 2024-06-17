import os

import segno
from PIL import Image
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_util import PhUtil

from qr_play.main.convert import converter
from qr_play.main.helper.formats import Formats
from qr_play.main.helper.metadata import MetaData

show_image = False


def parse_or_update_any_data(data, meta_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    """
    Individual
    """
    converter.set_defaults_for_printing(data)
    if meta_data is None:
        meta_data = MetaData(input_data_org=data.input_data)
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    converter.set_defaults(data, meta_data)
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    remarks = data.get_remarks_as_str()
    meta_data.file_based = True if data.image_format in [Formats.PNG, Formats.SVG] else False
    if meta_data.file_based:
        meta_data.output_file = os.sep.join(
            [PhUtil.path_default_out_folder, PhUtil.get_python_friendly_name(remarks if remarks else 'qr_code')])
        meta_data.output_file = PhUtil.append_in_file_name(meta_data.output_file,
                                                           new_ext=PhFileExtensions.SVG if data.image_format == Formats.SVG else PhFileExtensions.PNG)
        PhUtil.makedirs(PhUtil.get_file_name_and_extn(meta_data.output_file, only_path=True))
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
            handle_individual_qr_code(data, meta_data, qrcode, output_file)
            print()
            temp_output.append(meta_data.parsed_data)
        meta_data.parsed_data = temp_output
    else:
        qrcode = segno.make(data.input_data, version=data.qr_code_version)
        handle_individual_qr_code(data, meta_data, qrcode, meta_data.output_file)
    converter.print_data(data, meta_data)


def handle_individual_qr_code(data, meta_data, qrcode, file_path):
    print(f'individual data_length is {len(data.input_data)}')
    # print(f'mode is {qrcode.mode}')
    # print(f'error is {qrcode.error}')
    # print(f'version is {qrcode.version}')
    # print(f'default_border_size is {qrcode.default_border_size}')
    # print(f'designator is {qrcode.designator}')
    # print(f'is_micro is {qrcode.is_micro}')
    if data.image_format == Formats.SVG_URI:
        meta_data.parsed_data = qrcode.svg_data_uri(scale=data.scale)
    elif data.image_format == Formats.PNG_URI:
        meta_data.parsed_data = qrcode.png_data_uri(scale=data.scale)
    else:
        meta_data.parsed_data = file_path
        qrcode.save(file_path, scale=data.scale)
    if show_image:
        if data.image_format == Formats.PNG and data.print_output and not data.quite_mode:
            with Image.open(file_path) as img:
                img.show()
