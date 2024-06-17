from qr_play.main.data_type import sample
from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.helper.data import Data
from qr_play.main.helper.formats import Formats


class AnyData(DataTypeMaster):

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
        data_pool = [
            #
            Data(
                remarks='Simple Qr Png',
                input_data=sample.small_data,
                scale=10,
                image_format=Formats.PNG
            ),
            #
            Data(
                remarks='Simple Qr Png',
                input_data=sample.small_data,
                scale=10,
                image_format=Formats.PNG,
                qr_code_version=40,
            ),
            #
            Data(
                remarks='Simple Qr Png; version 20',
                input_data=sample.small_data,
                scale=10,
                image_format=Formats.PNG,
                qr_code_version=20
            ),
            #
            Data(
                remarks='Simple Qr Svg',
                input_data=sample.small_data,
                scale=10,
                qr_code_version=40,
                image_format=Formats.SVG
            ),
            #
            Data(
                remarks='Simple Qr Png Uri',
                input_data=sample.small_data,
                scale=10,
                qr_code_version=40,
                image_format=Formats.PNG_URI
            ),
            #
            Data(
                remarks='Simple Qr Svg Uri',
                input_data=sample.small_data,
                scale=10,
                qr_code_version=40,
                image_format=Formats.SVG_URI
            ),
            #
            Data(
                remarks='Bulk Data Single Qr',
                input_data=sample.bulk_data_1,
                qr_code_version=40,
            ),
            #
            Data(
                remarks='Bulk Data Single Qr; PNG URI',
                input_data=sample.bulk_data_1,
                qr_code_version=40,
                image_format=Formats.PNG_URI,
            ),
            #
            Data(
                remarks='Bulk Data Split Qrs',
                split_qrs=True,
                input_data=sample.bulk_data_2,
                qr_code_version=40,
            ),
            #
            Data(
                remarks='Bulk Data Split Qrs; PNG URI',
                split_qrs=True,
                input_data=sample.bulk_data_2,
                qr_code_version=40,
                image_format=Formats.PNG_URI,
            ),
            #
        ]
        super().set_data_pool(data_pool)
