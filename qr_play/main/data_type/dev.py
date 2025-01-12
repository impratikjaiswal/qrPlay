from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.data_type.sample import bulk_data_1, bulk_data_1_utf_8_defaults
from qr_play.main.helper.data import Data
from qr_play.main.helper.formats import Formats


class Dev(DataTypeMaster):

    def __init__(self):
        super().__init__()

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_size(self):
        size = None
        super().set_size(size)

    def set_qr_code_version(self):
        qr_code_version = None
        super().set_qr_code_version(qr_code_version)

    def set_split_qrs(self):
        split_qrs = None
        super().set_split_qrs(split_qrs)

    def set_decorate_qr(self):
        decorate_qr = None
        super().set_decorate_qr(decorate_qr)

    def set_data_pool(self):
        data_pool = [
            # Part of Sample Data
            # TODO: Web App; when submitted data size grows (Auto Submit: 1 QR, Manual Submit: 2 QR)
            Data(
                remarks='Bulk Data Single Qr',
                input_data=bulk_data_1,
                qr_code_version=40,
                split_qrs=False,
            ),
            Data(
                remarks='Bulk Data Single Qr',
                input_data=bulk_data_1_utf_8_defaults,
                output_format=Formats.PNG,
                qr_code_version=40,
                split_qrs=False,
            ),
        ]
        super().set_data_pool(data_pool)
