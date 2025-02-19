from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_variables import PhVariables

from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.data_type.sample import text_msg_small_data, apj_url, bulk_data_2, bulk_data_1, sample_vcard
from qr_play.main.helper.data import Data
from qr_play.main.helper.folders import Folders


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

    def set_label(self):
        label = None
        super().set_label(label)

    def set_label_position(self):
        label_position = None
        super().set_label_position(label_position)

    def set_data_pool(self):
        data_pool_empty_dummy = []
        #
        data_pool_positive = [
            #
            {
                PhKeys.REMARKS: f'Text Message; web api; {PhVariables.QR_CODE_VERSION}; {PhVariables.KEY_NAME};',
                PhKeys.INPUT_DATA: text_msg_small_data,
                PhKeys.SIZE: '10',
                PhKeys.QR_CODE_VERSION: '40',
            },
            #
            Data(
                remarks=f'Text Message; {PhVariables.QR_CODE_VERSION}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                size=10,
                qr_code_version=40,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                size=2,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                size=10,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.QR_CODE_VERSION}; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                size=8,
                qr_code_version=33,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.QR_CODE_VERSION}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                qr_code_version=20,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.QR_CODE_VERSION}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                qr_code_version=40,
            ),
        ]
        #
        data_pool_decorate_qr = [
            #
            Data(
                remarks=f'amenitypj.in; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                input_data=apj_url,
                split_qrs=False,
                decorate_qr=False,
            ),
            #
            Data(
                remarks=f'amenitypj.in; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                input_data=apj_url,
                split_qrs=False,
                decorate_qr=True,
            ),
            #
            Data(
                remarks=f'amenitypj.in; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                input_data=apj_url,
                split_qrs=False,
                decorate_qr=False,
            ),
            #
            Data(
                remarks=f'amenitypj.in; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                input_data=apj_url,
                split_qrs=False,
                decorate_qr=True,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                decorate_qr=False,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                decorate_qr=True,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                split_qrs=False,
                decorate_qr=False,
                size=2,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                split_qrs=False,
                decorate_qr=True,
                size=2,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                split_qrs=False,
                decorate_qr=False,
                size=10,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                split_qrs=False,
                decorate_qr=True,
                size=10,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.QR_CODE_VERSION}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                split_qrs=False,
                decorate_qr=False,
                qr_code_version=40,
            ),
            #
            Data(
                remarks=f'Text Message; {PhVariables.DECORATE_QR}; {PhVariables.QR_CODE_VERSION}; {PhVariables.KEY_NAME};',
                input_data=text_msg_small_data,
                split_qrs=False,
                decorate_qr=True,
                qr_code_version=40,
            ),
            #
            Data(
                remarks=f'Bulk Data Split Qrs; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                print_input=False,
                input_data=bulk_data_2,
                qr_code_version=40,
                decorate_qr=False,
                split_qrs=True,
            ),
            #
            Data(
                remarks=f'Bulk Data Split Qrs; {PhVariables.DECORATE_QR}; {PhVariables.KEY_NAME};',
                print_input=False,
                input_data=bulk_data_2,
                qr_code_version=40,
                decorate_qr=True,
                split_qrs=True,
            ),
        ]
        #
        data_pool_output_path = [
            #
            Data(
                remarks=f'amenitypj.in; Output Path',
                input_data=apj_url,
                split_qrs=False,
                output_path=Folders.in_user()
            ),
            #
            Data(
                remarks=f'amenitypj.in; email sig; {PhVariables.SIZE}; {PhVariables.KEY_NAME};',
                input_data=apj_url,
                split_qrs=False,
                decorate_qr=True,
                size=3,
                output_path=r'D:\Other\Github_Self\qrPlay\data\user_data',
            ),
        ]
        #
        data_pool_bulk_data = [
            #
            Data(
                remarks=f'Bulk Data Single Qr {PhVariables.SPLIT_QRS}; {PhVariables.KEY_NAME};',
                input_data=bulk_data_1,
                qr_code_version=40,
                split_qrs=False,
            ),
            #
            Data(
                remarks=f'Bulk Data Single Qr {PhVariables.SPLIT_QRS}; {PhVariables.KEY_NAME};',
                input_data=bulk_data_1,
                qr_code_version=40,
                split_qrs=True,
            ),
        ]
        #
        data_pool_vcard = []
        decorate_qr = [True, False]
        for _ in PhConstants.Position:
            for __ in decorate_qr:
                data_pool_vcard.append(
                    #
                    Data(
                        remarks=f'vCard; {PhVariables.DECORATE_QR}; {PhVariables.LABEL_POSITION}; {PhVariables.KEY_NAME};',
                        input_data=sample_vcard,
                        qr_code_version=40,
                        split_qrs=False,
                        label_position=_,
                        decorate_qr=__,
                        label='Qr Play',
                    ),
                )
        #
        data_pool_negative = [
            #
        ]
        #
        super().set_data_pool(
            data_pool_empty_dummy
            + data_pool_positive
            + data_pool_decorate_qr
            + data_pool_output_path
            + data_pool_bulk_data
            + data_pool_vcard
            + data_pool_negative
        )
