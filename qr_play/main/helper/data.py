from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


class Data:
    def __init__(self,
                 input_data=None,
                 print_input=None,
                 print_output=None,
                 print_info=None,
                 quite_mode=None,
                 remarks=[],
                 qr_code_version=None,
                 scale=None,
                 image_format=None,
                 split_qrs=None,
                 **kwargs,
                 ):
        """
        Instantiate the Data Object for further Processing.

        :param input_data: Input Data
        :param print_input: Printing of input needed ?
        :param print_output: Printing of output needed ?
        :param print_info:  Printing of info needed ?
        :param quite_mode: Quite mode needed ? if yes, no printing at all.
        :param remarks: Remarks for Input Data
        :param qr_code_version:
        :param scale:
        :param image_format:
        :param split_qrs:
        :param kwargs: To Handle unwanted/deprecated/internal/additional arguments (See Description)
        ----------

        kwargs -- (handled arguments description)
            raw_data -- @Deprecated!!! Use input_data instead \n
            remarks_list -- @Deprecated!!! Use remarks instead \n
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
        self.qr_code_version = qr_code_version
        self.scale = scale
        self.image_format = image_format
        self.split_qrs = split_qrs
        # Handle kwargs
        if self.input_data is None and PhKeys.RAW_DATA in kwargs:
            self.input_data = kwargs[PhKeys.RAW_DATA]
        if self.remarks is None and PhKeys.REMARKS_LIST in kwargs:
            self.remarks = kwargs[PhKeys.REMARKS_LIST]
        self.data_group = kwargs.get(PhKeys.DATA_GROUP, None)
        # Handle Internal args
        self.__auto_generated_remarks = None
        self.__one_time_remarks = None
        self.__extended_remarks_needed = None
        # Handle Remarks
        self.set_user_remarks(self.remarks)

    def set_user_remarks(self, remarks):
        self.remarks = PhUtil.to_list(remarks, trim_data=True, all_str=True)

    def __get_default_remarks(self):
        str_input_data = PhUtil.combine_list_items(self.input_data)
        return str_input_data

    def reset_auto_generated_remarks(self):
        self.__auto_generated_remarks = None

    def set_auto_generated_remarks_if_needed(self, internal_remarks=None):
        internal_remarks = PhUtil.set_if_not_none(internal_remarks)
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
