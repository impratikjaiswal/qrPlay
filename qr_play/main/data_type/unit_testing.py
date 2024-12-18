from python_helpers.ph_keys import PhKeys

from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.data_type.sample import small_data
from qr_play.main.helper.data import Data


class UnitTesting(DataTypeMaster):

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

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_image_format(self):
        image_format = None
        super().set_image_format(image_format)

    def set_scale(self):
        scale = None
        super().set_scale(scale)

    def set_qr_code_version(self):
        qr_code_version = None
        super().set_qr_code_version(qr_code_version)

    def set_split_qrs(self):
        split_qrs = None
        super().set_split_qrs(split_qrs)

    def set_data_pool(self):
        data_pool_positive = [
            #
            {
                PhKeys.REMARKS: 'Simple Qr Png',
                PhKeys.INPUT_DATA: 'small_data',
                PhKeys.SCALE: '10',
                PhKeys.QR_CODE_VERSION: '40',
            },
            #
            Data(
                remarks='Simple Qr Png',
                input_data=small_data,
                scale=10,
                qr_code_version=40,
            ),
            #
            Data(
                remarks='Simple Qr Png',
                input_data=small_data,
                scale=10,
            ),
            #
            Data(
                remarks='Simple Qr; qr_code_version=33; scale=8 ',
                input_data=small_data,
                scale=8,
                qr_code_version=33,
            ),
            #
            Data(
                remarks='Simple Qr; qr_code_version=20',
                input_data=small_data,
                qr_code_version=20,
            ),
            #
            Data(
                remarks='Simple Qr; qr_code_version=40',
                input_data=small_data,
                qr_code_version=40,
            ),
        ]
        data_pool_negative = [
            #
        ]
        super().set_data_pool(data_pool_positive + data_pool_negative)
