import enum
from collections import OrderedDict

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from python_helpers.ph_variables import PhVariables


class Data:
    def __init__(self,
                 # Common Param
                 input_data=None,
                 print_input=None,
                 print_output=None,
                 print_info=None,
                 quite_mode=None,
                 remarks=[],
                 encoding=None,
                 encoding_errors=None,
                 output_path=None,
                 output_file_name_keyword=None,
                 archive_output=None,
                 archive_output_format=None,
                 # Specific Param
                 output_format=None,
                 size=None,
                 qr_code_version=None,
                 split_qrs=None,
                 decorate_qr=None,
                 label=None,
                 label_position=None,
                 # Unknown/System Param
                 **kwargs,
                 ):
        """
        Instantiate the Data Object for further Processing.

        :param input_data: Input Data; String(s), File Path(s), Dir Paths(s)
        :param print_input: Printing of input needed?
        :param print_output: Printing of output needed?
        :param print_info:  Printing of info needed?
        :param quite_mode: Quite mode needed? If yes, no printing at all.
        :param remarks: Remarks for Input Data
        :param encoding: Encoding for Input/Output Data
        :param encoding_errors: Encoding Errors Handling for Input/Output Data
        :param output_path: Output Path
        :param output_file_name_keyword:
        :param archive_output: Archiving of output needed?
        :param archive_output_format: Archive Output Format
        :param output_format: Output Format
        :param size:
        :param qr_code_version:
        :param split_qrs:
        :param decorate_qr:
        :param kwargs: To Handle unwanted/deprecated/internal/additional arguments (See Description)
        ----------

        kwargs -- (handled arguments description)
            raw_data -- @Deprecated!!! Use input_data instead \n
            remarks_list -- @Deprecated!!! Use remarks instead \n
            image_format -- @Deprecated!!! Use output_format instead \n
            scale -- @Deprecated!!! Use size instead \n
            data_group -- Used for Web App
        ----------
        """
        # Handle Normal Args
        self.input_data = input_data
        self.print_input = print_input
        self.print_output = print_output
        self.print_info = print_info
        self.quite_mode = quite_mode
        self.remarks = remarks
        self.encoding = encoding
        self.encoding_errors = encoding_errors
        self.output_path = output_path
        self.output_file_name_keyword = output_file_name_keyword
        self.archive_output = archive_output
        self.archive_output_format = archive_output_format
        self.output_format = output_format
        self.size = size
        self.qr_code_version = qr_code_version
        self.split_qrs = split_qrs
        self.decorate_qr = decorate_qr
        self.label = label
        self.label_position = label_position
        # Handle kwargs
        if self.input_data is None and PhKeys.RAW_DATA in kwargs:
            self.input_data = kwargs[PhKeys.RAW_DATA]
        if self.remarks is None and PhKeys.REMARKS_LIST in kwargs:
            self.remarks = kwargs[PhKeys.REMARKS_LIST]
        if self.output_format is None and PhKeys.IMAGE_FORMAT in kwargs:
            self.output_format = kwargs[PhKeys.IMAGE_FORMAT]
        if self.size is None and PhKeys.SCALE in kwargs:
            self.size = kwargs[PhKeys.SCALE]
        self.data_group = kwargs.get(PhKeys.DATA_GROUP, None)
        # Handle Internal args
        self.__input_modes_hierarchy = []
        self.__auto_generated_remarks = None
        self.__one_time_remarks = None
        self.__extended_remarks_needed = None
        # Handle Remarks
        self.set_user_remarks(self.remarks)
        # Handle Remarks Variables
        self.__variables_pool = {
            #           _key : (_var_name, _var_value)
            PhKeys.OUTPUT_FORMAT: (PhVariables.OUTPUT_FORMAT, self.output_format),
            PhKeys.SIZE: (PhVariables.SIZE, self.size),
            PhKeys.QR_CODE_VERSION: (PhVariables.QR_CODE_VERSION, self.qr_code_version),
            PhKeys.SPLIT_QRS: (PhVariables.SPLIT_QRS, self.split_qrs),
            PhKeys.DECORATE_QR: (PhVariables.DECORATE_QR, self.decorate_qr),
            PhKeys.LABEL: (PhVariables.LABEL, self.label),
            PhKeys.LABEL_POSITION: (PhVariables.LABEL_POSITION, self.label_position),
        }
        # Needed for the scenarios when 'label' (subset) & 'label_position' (superset) both are there.
        self.__variables_pool = OrderedDict(sorted(self.__variables_pool.items(), reverse=True))

    def set_user_remarks(self, remarks):
        self.remarks = PhUtil.to_list(remarks, trim_data=True, all_str=True)

    def set_user_remarks_expand_variables(self):
        def __set_value(x, var_name, var_value, key_name_needed, key_):
            if var_name in x and var_value is not None:
                if isinstance(var_value, enum.Enum):
                    var_value = var_value.name
                var_value = str(var_value)
                y = '_'.join([key_, var_value]) if key_name_needed else var_value
                return x.replace(var_name, y)
            return x

        def __expand_variable(x):
            key_name_needed = True if PhVariables.KEY_NAME in x else False
            if key_name_needed:
                x = x.replace(PhVariables.KEY_NAME, '')
            for key, value in self.__variables_pool.items():
                x = __set_value(x=x, var_name=value[0], var_value=value[1], key_name_needed=key_name_needed, key_=key)
            return x

        self.remarks = [__expand_variable(x) for x in self.remarks]

    def __get_default_remarks(self):
        str_input_data = PhUtil.combine_list_items(self.input_data)
        return str_input_data

    def reset_auto_generated_remarks(self):
        self.__auto_generated_remarks = None

    def set_auto_generated_remarks_if_needed(self, internal_remarks=None):
        internal_remarks = PhUtil.set_if_none(internal_remarks)
        default_remarks = self.__get_default_remarks()
        if self.remarks and self.remarks[0]:
            # User Remarks is already provided, default remarks are not needed
            default_remarks = None
        # auto generated comments are set
        self.__auto_generated_remarks = PhUtil.append_remarks(internal_remarks,
                                                              self.__auto_generated_remarks if self.__auto_generated_remarks else default_remarks,
                                                              append_mode_post=False)

    def get_remarks_as_str(self, user_original_remarks=False, force_mode=False):
        user_remarks = PhUtil.combine_list_items(self.remarks)
        if user_original_remarks:
            if user_remarks:
                return user_remarks.replace('\n', ' ')
            if not force_mode:
                return ''
        if user_remarks:
            user_remarks = PhUtil.trim_remarks(user_remarks)
        one_time_remarks = PhUtil.append_remarks(self.get_one_time_remarks(), self.__auto_generated_remarks,
                                                 append_mode_post=False)
        return PhUtil.append_remarks(one_time_remarks, user_remarks, append_mode_post=False).replace('\n', ' ')

    def set_extended_remarks_available(self, extended_remarks):
        self.__extended_remarks_needed = extended_remarks

    def get_extended_remarks_available(self):
        return self.__extended_remarks_needed

    def get_one_time_remarks(self):
        temp = self.__one_time_remarks
        self.__one_time_remarks = None
        return temp

    def set_one_time_remarks(self, one_time_remarks):
        self.__one_time_remarks = one_time_remarks

    def append_input_modes_hierarchy(self, input_mode_hierarchy):
        self.__input_modes_hierarchy.append(input_mode_hierarchy)

    def get_input_modes_hierarchy_as_str(self):
        return PhConstants.SEPERATOR_MULTI_OBJ.join(self.__input_modes_hierarchy)

    def get_input_modes_hierarchy(self):
        return self.__input_modes_hierarchy

    def validate_if_input_modes_hierarchy(self, input_mode_hierarchy):
        return True if input_mode_hierarchy in self.__input_modes_hierarchy else False
