import traceback

import binascii
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData
from python_helpers.ph_exceptions import PhExceptions
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from qr_play.main.convert import converter
from qr_play.main.convert.converter import read_web_request
from qr_play.main.convert.parser import parse_or_update_any_data
from qr_play.main.helper.data import Data
from qr_play.main.helper.metadata import MetaData


class DataTypeMaster(object):
    def __init__(self):
        self.print_input = None
        self.print_output = None
        self.print_info = None
        self.quite_mode = None
        self.remarks_list = None
        self.image_format = None
        self.scale = None
        self.qr_code_version = None
        self.split_qrs = None		
        self.data_pool = []
        self.__master_data = (Data(raw_data=None), MetaData(raw_data_org=None), PhExceptions(msg=None))

    def set_print_input(self, print_input):
        self.print_input = print_input

    def set_print_output(self, print_output):
        self.print_output = print_output

    def set_print_info(self, print_info):
        self.print_info = print_info

    def set_quiet_mode(self, quite_mode):
        self.quite_mode = quite_mode

    def set_remarks_list(self, remarks_list):
        self.remarks_list = remarks_list

    def set_image_format(self, image_format):
        self.image_format = image_format

    def set_scale(self, scale):
        self.scale = scale

    def set_qr_code_version(self, qr_code_version):
        self.qr_code_version = qr_code_version

    def set_split_qrs(self, split_qrs):
        self.split_qrs = split_qrs

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def parse_safe(self, error_handling_mode, data=None):
        """

        :param data:
        :param error_handling_mode:
        :return:
        """
        if data is None:
            data = self.data_pool
        if isinstance(data, list):
            """
            Handle Pool
            """
            for data_item in data:
                self.parse_safe(error_handling_mode=error_handling_mode, data=data_item)
            return
        """
        Handle Individual Request
        """
        try:
            if isinstance(data, dict):
                """
                Web Form
                """
                data = read_web_request(data)
            self.__parse_safe_individual(data)
        except Exception as e:
            known = False
            additional_msg = None
            if isinstance(e.args[0], PhExceptions):
                exception_msg = e.args[0].get_details()
                self.__master_data = (
                    self.__master_data[PhMasterData.INDEX_DATA], self.__master_data[PhMasterData.INDEX_META_DATA],
                    e.args[0])
            else:
                # for scenarios like FileExistsError where a touple is returned, (17, 'Cannot create a file when that file already exists')
                exception_msg = str(e)
                self.__master_data = (
                    self.__master_data[PhMasterData.INDEX_DATA], self.__master_data[PhMasterData.INDEX_META_DATA],
                    PhExceptions(exception_msg))
            if isinstance(e, binascii.Error):
                known = True
                additional_msg = 'raw_data is invalid'
            elif isinstance(e, ValueError):
                known = True
            elif isinstance(e, PermissionError):
                known = True
                additional_msg = 'input/output path reading/writing error'
            elif isinstance(e, FileExistsError):
                known = True
                additional_msg = 'Output path writing error'
            processed_data = self.__master_data[PhMasterData.INDEX_DATA]
            processed_meta_data = self.__master_data[PhMasterData.INDEX_META_DATA]
            converter.print_data(processed_data, processed_meta_data)
            msg = PhUtil.get_key_value_pair(PhConstants.EXCEPTION_KNOWN if known else PhConstants.EXCEPTION_UNKNOWN,
                                            PhConstants.SEPERATOR_MULTI_OBJ.join(
                                                filter(None, [additional_msg, exception_msg])))
            print(f'{msg}')
            if not known:
                traceback.print_exc()
            if error_handling_mode == PhErrorHandlingModes.STOP_ON_ERROR:
                raise

    def __parse_safe_individual(self, data):
        """
        Handle Individual Request
        :param data:
        :return:
        """
        if isinstance(data, Data):
            data.print_input = data.print_input if data.print_input is not None else self.print_input
            data.print_output = data.print_output if data.print_output is not None else self.print_output
            data.print_info = data.print_info if data.print_info is not None else self.print_info
            data.quite_mode = data.quite_mode if data.quite_mode is not None else self.quite_mode
            data.remarks_list = data.remarks_list if data.remarks_list is not None else self.remarks_list
            data.qr_code_version = data.qr_code_version if data.qr_code_version is not None else self.qr_code_version
            data.scale = data.scale if data.scale is not None else self.scale
            data.image_format = data.image_format if data.image_format is not None else self.image_format
            data.split_qrs = data.split_qrs if data.split_qrs is not None else self.split_qrs
        else:
            data = Data(
                raw_data=data,
                print_input=self.print_input,
                print_output=self.print_output,
                print_info=self.print_info,
                quite_mode=self.quite_mode,
                remarks_list=self.remarks_list,
                qr_code_version=self.qr_code_version,
                scale=self.scale,
                image_format=self.image_format,
                split_qrs=self.split_qrs,
            )
        meta_data = MetaData(raw_data_org=data.raw_data)
        self.__master_data = (data, meta_data)
        parse_or_update_any_data(data, meta_data)

    def get_output_data(self):
        """

        :return:
        """
        output_data = ''
        if len(self.__master_data) > PhMasterData.INDEX_ERROR_DATA:
            # Exception Object is Present
            exception_data = self.__master_data[PhMasterData.INDEX_ERROR_DATA]
            output_data = exception_data.get_details() if isinstance(exception_data, PhExceptions) else exception_data
            return output_data
        if len(self.__master_data) > PhMasterData.INDEX_META_DATA:
            # MetaData Object is Present
            meta_data = self.__master_data[PhMasterData.INDEX_META_DATA]
            output_data = meta_data.parsed_data if isinstance(meta_data, MetaData) else output_data
        return output_data
