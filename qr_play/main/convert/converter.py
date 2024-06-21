from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from qr_play.main.helper.data import Data
from qr_play.main.helper.defaults import Defaults


def print_data(data, meta_data):
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE
    if data.print_info:
        remarks_original = data.get_remarks_as_str(user_original_remarks=True)
        remarks_generated = data.get_remarks_as_str()
        remarks_generated_stripping_needed = True if remarks_generated.endswith(
            PhConstants.DEFAULT_TRIM_STRING) else False
        if remarks_original:
            if remarks_generated_stripping_needed:
                if remarks_generated.strip(PhConstants.DEFAULT_TRIM_STRING) in remarks_original:
                    remarks_generated = ''
            else:
                if remarks_original in remarks_generated:
                    remarks_generated = ''
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                       remarks_generated))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(PhKeys.TRANSACTION_ID, PhConstants.SEPERATOR_ONE_LINE, meta_data.transaction_id,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.IMAGE_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.image_format,
                                   dic_format=False, print_also=False) if data.image_format else None,
            get_dic_data_and_print(PhKeys.SCALE, PhConstants.SEPERATOR_ONE_LINE, data.scale,
                                   dic_format=False, print_also=False) if data.scale else None,
            get_dic_data_and_print(PhKeys.QR_CODE_VERSION, PhConstants.SEPERATOR_ONE_LINE, data.qr_code_version,
                                   dic_format=False, print_also=False) if data.qr_code_version else None,
            get_dic_data_and_print(PhKeys.SPLIT_QRS, PhConstants.SEPERATOR_ONE_LINE, data.split_qrs,
                                   dic_format=False, print_also=False) if data.split_qrs else None,
            get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                   dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, meta_data.input_data_org))
    print_output = data.print_output
    if data.print_output and print_output:  # and meta_data.parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    PhUtil.print_separator()


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    return PhUtil.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def parse_config(config_data):
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if v:
            # Trim Garbage data
            v = PhUtil.trim_white_spaces_in_str(v)
            if v in ['None']:
                v = None
                config_data[k] = v
            if v in [PhConstants.STR_SELECT_OPTION]:
                v = None
                config_data[k] = v
            if v in ['True']:
                v = True
                config_data[k] = v
            if v in ['False']:
                v = False
                config_data[k] = v
        if not v:
            continue
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_printing(data):
    if data.quite_mode is None:
        data.quite_mode = Defaults.QUITE_MODE
    if data.print_input is None:
        data.print_input = Defaults.PRINT_INPUT
    if data.print_output is None:
        data.print_output = Defaults.PRINT_OUTPUT
    if data.print_info is None:
        data.print_info = Defaults.PRINT_INFO


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    if data.qr_code_version is None:
        data.qr_code_version = Defaults.QR_CODE_VERSION
    if data.scale is None:
        data.scale = Defaults.SCALE
    if data.image_format is None:
        data.image_format = Defaults.IMAGE_FORMAT
    if data.split_qrs is None:
        data.split_qrs = Defaults.SPLIT_QRS


def read_web_request(request_form):
    return Data(**parse_config(request_form))
