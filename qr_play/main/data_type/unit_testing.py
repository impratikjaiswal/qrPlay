from qr_play.main.data_type.data_type_master import DataTypeMaster


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

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

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
                'remarks_list': 'Simple Qr Png',
                'raw_data': 'small_data',
                'scale': '10',
                'qr_code_version': '40',
                'image_format': 'png',
            },
        ]
        data_pool_negative = [
            #
        ]
        super().set_data_pool(data_pool_positive + data_pool_negative)
