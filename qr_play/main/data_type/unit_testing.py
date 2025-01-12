from python_helpers.ph_keys import PhKeys

from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.data_type.sample import small_data, apj_url, bulk_data_2
from qr_play.main.helper.data import Data
from qr_play.main.helper.folders import Folders
from qr_play.main.helper.formats import Formats


class UnitTesting(DataTypeMaster):

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
        data_pool_positive = [
            #
            {
                PhKeys.REMARKS: 'Simple Qr Png',
                PhKeys.INPUT_DATA: 'small_data',
                PhKeys.SIZE: '10',
                PhKeys.QR_CODE_VERSION: '40',
            },
            #
            Data(
                remarks='Simple Qr Png',
                input_data=small_data,
                size=10,
                qr_code_version=40,
            ),
            #
            Data(
                remarks='Simple Qr Png',
                input_data=small_data,
                size=10,
            ),
            #
            Data(
                remarks='Simple Qr; qr_code_version=33; size=8 ',
                input_data=small_data,
                size=8,
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
        data_pool_decorate_qr = [
            #
            Data(
                remarks='amenitypj.in; $DECORATE_QR; $KEY_NAME',
                input_data=apj_url,
                output_format=Formats.PNG,
                split_qrs=False,
                decorate_qr=False,
            ),
            #
            Data(
                remarks='amenitypj.in; $DECORATE_QR; $KEY_NAME',
                input_data=apj_url,
                output_format=Formats.PNG,
                split_qrs=False,
                decorate_qr=True,
            ),
            #
            Data(
                remarks='amenitypj.in; $DECORATE_QR; $KEY_NAME',
                input_data=apj_url,
                output_format=Formats.PNG_URI,
                split_qrs=False,
                decorate_qr=False,
            ),
            #
            Data(
                remarks='amenitypj.in; $DECORATE_QR; $KEY_NAME',
                input_data=apj_url,
                output_format=Formats.PNG_URI,
                split_qrs=False,
                decorate_qr=True,
            ),
            #
            Data(
                remarks='Bulk Data Split Qrs; $DECORATE_QR; $KEY_NAME',
                print_input=False,
                input_data=bulk_data_2,
                output_format=Formats.PNG,
                qr_code_version=40,
                decorate_qr=False,
                split_qrs=True,
            ),
            #
            Data(
                remarks='Bulk Data Split Qrs; $DECORATE_QR; $KEY_NAME',
                print_input=False,
                input_data=bulk_data_2,
                output_format=Formats.PNG,
                qr_code_version=40,
                decorate_qr=True,
                split_qrs=True,
            ),
        ]
        data_pool_output_path = [
            #
            Data(
                remarks='Qr With image',
                input_data=apj_url,
                output_format=Formats.PNG,
                split_qrs=False,
                output_path=Folders.in_sample()
            ),
            #
            Data(
                remarks='amenitypj.in; email sig; $SIZE; $KEY_NAME',
                input_data=apj_url,
                output_format=Formats.PNG,
                split_qrs=False,
                decorate_qr=True,
                size=3,
                # TODO: Hard code path
                output_path=r'D:\Other\Github_Self\amenitypj',
            ),
        ]
        data_pool_negative = [
            #
        ]
        super().set_data_pool(
            data_pool_positive
            + data_pool_decorate_qr
            + data_pool_output_path
            + data_pool_negative
        )
