import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_defaults import PhDefaultTypesExclude
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from qr_play.main.helper.data import Data
from qr_play.main.helper.defaults import Defaults, DefaultTypesInclude
from qr_play.main.helper.folders import Folders
from qr_play.main.helper.formats import Formats
from qr_play.main.helper.keywords import KeyWords
from qr_play.main.helper.variables import Variables


def print_data(data=None, meta_data=None, info_data=None, master_data=None):
    """
    
    :param data:
    :param meta_data:
    :param info_data:
    :param master_data:
    :return:
    """
    if master_data is not None and isinstance(master_data, PhMasterData):
        data = master_data.get_master_data(PhMasterDataKeys.DATA)
        meta_data = master_data.get_master_data(PhMasterDataKeys.META_DATA)
        info_data = master_data.get_master_data(PhMasterDataKeys.INFO_DATA)
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_ONE_LINE
    len_sep = PhConstants.SEPERATOR_ONE_LINE
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
                PhUtil.get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                              remarks_generated))
        if info_data is not None:
            info_count = info_data.get_info_count()
            info_msg = info_data.get_info_str()
            info_present = info_msg
            if info_present:
                sep = PhConstants.SEPERATOR_MULTI_LINE_TABBED if info_count > 1 else PhConstants.SEPERATOR_ONE_LINE
                meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INFO_DATA, sep, info_msg))
                if data.print_info:
                    meta_data.output_dic.update(
                        PhUtil.get_dic_data_and_print(PhKeys.INFO_DATA, len_sep, info_msg, length_needed=True))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            PhUtil.get_dic_data_and_print(PhKeys.TRANSACTION_ID, PhConstants.SEPERATOR_ONE_LINE,
                                          meta_data.transaction_id, dic_format=False, print_also=False),
            PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_PATH, PhConstants.SEPERATOR_ONE_LINE, data.output_path,
                                          dic_format=False, print_also=False) if data.output_path else None,
            PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.output_format,
                                          dic_format=False, print_also=False) if data.output_format else None,
            PhUtil.get_dic_data_and_print(PhKeys.SIZE, PhConstants.SEPERATOR_ONE_LINE, data.size,
                                          dic_format=False, print_also=False) if data.size else None,
            PhUtil.get_dic_data_and_print(PhKeys.QR_CODE_VERSION, PhConstants.SEPERATOR_ONE_LINE, data.qr_code_version,
                                          dic_format=False, print_also=False) if data.qr_code_version else None,
            PhUtil.get_dic_data_and_print(PhKeys.SPLIT_QRS, PhConstants.SEPERATOR_ONE_LINE, data.split_qrs,
                                          dic_format=False, print_also=False) if data.split_qrs else None,
            PhUtil.get_dic_data_and_print(PhKeys.DECORATE_QR, PhConstants.SEPERATOR_ONE_LINE, data.decorate_qr,
                                          dic_format=False, print_also=False) if data.decorate_qr else None,
            PhUtil.get_dic_data_and_print(PhKeys.ENCODING, PhConstants.SEPERATOR_ONE_LINE, data.encoding,
                                          dic_format=False, print_also=False) if data.encoding else None,
            PhUtil.get_dic_data_and_print(PhKeys.ENCODING_ERRORS, PhConstants.SEPERATOR_ONE_LINE, data.encoding_errors,
                                          dic_format=False, print_also=False) if data.encoding_errors else None,
            PhUtil.get_dic_data_and_print(PhKeys.ARCHIVE_OUTPUT, PhConstants.SEPERATOR_ONE_LINE, data.archive_output,
                                          dic_format=False, print_also=False) if data.archive_output else None,
            PhUtil.get_dic_data_and_print(PhKeys.ARCHIVE_OUTPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE,
                                          data.archive_output_format,
                                          dic_format=False, print_also=False) if data.archive_output_format else None,
            PhUtil.get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                          dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(
            PhUtil.get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, meta_data.input_data_org))
    if data.print_info:
        meta_data.output_dic.update(
            PhUtil.get_dic_data_and_print(PhKeys.INPUT_DATA, len_sep, meta_data.input_data_org, length_needed=True))
    output_present = meta_data.parsed_data
    if output_present:
        if data.print_output:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
        if data.print_info:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_DATA, len_sep, meta_data.parsed_data, length_needed=True))
    PhUtil.print_separator()


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # Always exclude output files
    meta_data.excludes = ['*_' + KeyWords.OUTPUT_FILE_NAME_KEYWORD + '.*']
    # Include Everything for now


def dict_to_data(config_data):
    data_types_include = {
        # Common Param
        # PhKeys.INPUT_DATA:
        PhKeys.PRINT_INPUT: DefaultTypesInclude.PRINT_INPUT,
        PhKeys.PRINT_OUTPUT: DefaultTypesInclude.PRINT_OUTPUT,
        PhKeys.PRINT_INFO: DefaultTypesInclude.PRINT_INFO,
        PhKeys.QUITE_MODE: DefaultTypesInclude.QUITE_MODE,
        PhKeys.ENCODING: DefaultTypesInclude.ENCODING,
        PhKeys.ENCODING_ERRORS: DefaultTypesInclude.ENCODING_ERRORS,
        PhKeys.ARCHIVE_OUTPUT: DefaultTypesInclude.ARCHIVE_OUTPUT,
        PhKeys.ARCHIVE_OUTPUT_FORMAT: DefaultTypesInclude.ARCHIVE_OUTPUT_FORMAT,
        # Specific Param
        PhKeys.OUTPUT_FORMAT: DefaultTypesInclude.OUTPUT_FORMAT,
        PhKeys.SIZE: DefaultTypesInclude.SIZE,
        PhKeys.QR_CODE_VERSION: DefaultTypesInclude.QR_CODE_VERSION,
        PhKeys.SPLIT_QRS: DefaultTypesInclude.SPLIT_QRS,
        PhKeys.DECORATE_QR: DefaultTypesInclude.DECORATE_QR,
    }
    data_types_exclude = {
        # Common Param
        PhKeys.INPUT_DATA: PhDefaultTypesExclude.INPUT_DATA,
        # PhKeys.REMARKS: ,
    }

    config_data = PhUtil.dict_to_data(user_dict=config_data, data_types_include=data_types_include,
                                      data_types_exclude=data_types_exclude, trim_data=False)
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if not v:
            continue
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data before cleaning', verbose=True, depth_level=1)
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_common_objects(data):
    """

    :param data:
    :return:
    """
    data.quite_mode = PhUtil.set_if_none(data.quite_mode, Defaults.QUITE_MODE)
    data.print_input = PhUtil.set_if_none(data.print_input, Defaults.PRINT_INPUT)
    data.print_output = PhUtil.set_if_none(data.print_output, Defaults.PRINT_OUTPUT)
    data.print_info = PhUtil.set_if_none(data.print_info, Defaults.PRINT_INFO)
    data.encoding = PhUtil.set_if_none(data.encoding, Defaults.ENCODING)
    data.encoding_errors = PhUtil.set_if_none(data.encoding_errors, Defaults.ENCODING_ERRORS)
    data.output_path = PhUtil.set_if_none(data.output_path, Defaults.OUTPUT_PATH)
    data.archive_output = PhUtil.set_if_none(data.archive_output, Defaults.ARCHIVE_OUTPUT)
    data.archive_output_format = PhUtil.set_if_none(data.archive_output_format, Defaults.ARCHIVE_OUTPUT_FORMAT)


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    data.output_format = PhUtil.set_if_none(data.output_format, Defaults.OUTPUT_FORMAT)
    data.size = PhUtil.set_if_none(data.size, Defaults.SIZE)
    data.qr_code_version = PhUtil.set_if_none(data.qr_code_version, Defaults.QR_CODE_VERSION)
    data.split_qrs = PhUtil.set_if_none(data.split_qrs, Defaults.SPLIT_QRS)
    data.decorate_qr = PhUtil.set_if_none(data.decorate_qr, Defaults.DECORATE_QR)
    if meta_data is None:
        return
    default_output_file_mapping = {
        Formats.PNG: PhFileExtensions.PNG,
        Formats.SVG: PhFileExtensions.SVG,
    }
    meta_data.output_file_ext_default = default_output_file_mapping.get(data.output_format, Defaults.OUTPUT_FILE_EXT)
    meta_data.output_file_location_default = Folders.in_user()


def handle_web_request(request_form):
    return Data(**dict_to_data(request_form))


def set_output_file_path(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    remarks_needed = False
    remarks_with_indexes = False
    sample_file_name_from_input_file = False
    sample_file_name = ''
    name_as_per_remarks = ''
    output_file_name = ''
    # if not (meta_data.input_mode_key == PhKeys.INPUT_YML or data.output_path):
    #     return
    output_path = data.output_path
    output_file_location = meta_data.output_file_location_default
    if not output_path:
        # Image File writing is needed, But output_path is not Provided, so Dest Folder will be default folder
        output_path = output_file_location
    if output_path:
        sample_file_ext = PhUtil.get_file_name_and_extn(output_path, only_extn=True)
        sample_file_folder = PhUtil.get_file_name_and_extn(output_path, only_path=True)
        sample_file_name = PhUtil.get_file_name_and_extn(output_path)
        if Variables.ITEM_INDEX in sample_file_name:
            remarks_with_indexes = True
            sample_file_name = sample_file_name.replace(Variables.ITEM_INDEX, '')
        if sample_file_name == Variables.REMARKS:
            # Only Target Directory is provided; Remarks usage is explicitly mentioned
            remarks_needed = True
            sample_file_name = sample_file_name.replace(Variables.REMARKS, '')
            output_file_location = sample_file_folder
        elif sample_file_ext:
            # Target File Provided
            output_file_name = sample_file_name
            output_file_location = sample_file_folder
        else:
            # Only Target Directory is provided
            output_file_location = os.sep.join([sample_file_folder, sample_file_name])
            # Remarks usage is implicit
            remarks_needed = True
            sample_file_name = ''
    if remarks_needed or sample_file_name_from_input_file:
        if remarks_needed:
            if data.get_extended_remarks_available():
                remarks_with_indexes = True
            name_as_per_remarks = PhUtil.get_python_friendly_name(
                data.get_remarks_as_str(user_original_remarks=not remarks_with_indexes,
                                        force_mode=True), case_sensitive=False)
        output_file_name = PhUtil.append_in_file_name(str_file_path=sample_file_name,
                                                      str_append=[name_as_per_remarks,
                                                                  data.output_file_name_keyword],
                                                      new_ext=meta_data.output_file_ext_default)
    meta_data.output_file_path = os.sep.join([output_file_location, output_file_name])
    PhUtil.make_dirs(dir_path=output_file_location)


def read_input_file(data, meta_data, info_data):
    try:
        # Text File
        with open(data.input_data, mode='r', encoding=data.encoding, errors=data.encoding_errors) as the_file:
            resp = ''.join(the_file.readlines())
    except UnicodeDecodeError:
        # Binary File/Encoding Error
        with open(data.input_data, 'rb') as the_file:
            resp = the_file.read()
    if not resp:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.EMPTY_INPUT_FILE))
    return resp


def write_output_file(data, meta_data, info_data, flip_output=False):
    output_file_path = meta_data.output_file_path
    data_to_write = meta_data.parsed_data
    if flip_output is True:
        output_file_path = meta_data.re_output_file_path
        data_to_write = meta_data.re_parsed_data
    data_to_write = PhUtil.set_if_none(data_to_write, PhConstants.STR_EMPTY)
    with open(output_file_path, mode='w', encoding=data.encoding, errors=data.encoding_errors) as file:
        file.writelines(data_to_write)
