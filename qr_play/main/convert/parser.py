import os

import segno
from PIL import Image
from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_util import PhUtil

from qr_play.main.convert import converter
from qr_play.main.helper.formats import Formats
from qr_play.main.helper.metadata import MetaData


def parse_or_update_any_data(data, meta_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    converter.set_defaults_for_printing(data)
    if meta_data is None:
        meta_data = MetaData(raw_data_org=data.raw_data)
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    converter.set_defaults(data, meta_data)
    remarks = data.get_remarks_as_str()
    meta_data.file_based = True if data.image_format in [Formats.PNG, Formats.SVG] else False
    if meta_data.file_based:
        meta_data.output_file = os.sep.join(
            [PhUtil.path_default_out_folder, PhUtil.get_python_friendly_name(remarks if remarks else 'qr_code')])
        meta_data.output_file = PhUtil.append_in_file_name(meta_data.output_file,
                                                           new_ext=PhFileExtensions.SVG if data.image_format == Formats.SVG else PhFileExtensions.PNG)
        PhUtil.makedirs(PhUtil.get_file_name_and_extn(meta_data.output_file, only_path=True))
    if data.split_qrs:
        qrcode_split = segno.make_sequence(data.raw_data, version=data.qr_code_version)
        sequence_count = len(qrcode_split)
        print(f'sequence_count is {sequence_count}')
        # qrcode_split.save(file_path, scale=data.scale)
        temp_output = []
        for index, qrcode in enumerate(qrcode_split, start=1):
            output_file = PhUtil.append_in_file_name(meta_data.output_file, str_append=['item',
                                                                                        str(index)]) if meta_data.file_based else meta_data.output_file
            handle_individual_qr_code(data, meta_data, qrcode, output_file)
            print()
            if not meta_data.file_based:
                temp_output.append(meta_data.parsed_data)
        meta_data.parsed_data = temp_output
    else:
        qrcode = segno.make(data.raw_data)
        handle_individual_qr_code(data, meta_data, qrcode, meta_data.file_based)
    converter.print_data(data, meta_data)


def handle_individual_qr_code(data, meta_data, qrcode, file_path):
    print(f'data_length is {len(data.raw_data)}')
    print(f'mode is {qrcode.mode}')
    print(f'error is {qrcode.error}')
    print(f'version is {qrcode.version}')
    print(f'default_border_size is {qrcode.default_border_size}')
    print(f'designator is {qrcode.designator}')
    print(f'is_micro is {qrcode.is_micro}')
    if data.image_format == Formats.SVG_URI:
        meta_data.parsed_data = qrcode.svg_data_uri(scale=data.scale)
    elif data.image_format == Formats.PNG_URI:
        meta_data.parsed_data = qrcode.png_data_uri(scale=data.scale)
    else:
        qrcode.save(file_path, scale=data.scale)
    if data.image_format == Formats.PNG and data.print_output and not data.quite_mode:
        with Image.open(file_path) as img:
            img.show()
