from python_helpers.ph_defaults import PhDefaults, PhDefaultTypesInclude, PhDefaultTypesExclude
from python_helpers.ph_file_extensions import PhFileExtensions

from qr_play.main.helper.formats import Formats


class Defaults:
    #############
    # Generic Objects
    #############
    EXECUTION_MODE = PhDefaults.EXECUTION_MODE
    ERROR_HANDLING_MODE = PhDefaults.ERROR_HANDLING_MODE
    OUTPUT_FILE_EXT = PhFileExtensions.PNG
    #############
    # Data Objects
    #############
    # Common Objects
    # INPUT_DATA
    PRINT_INPUT = PhDefaults.PRINT_INPUT
    PRINT_OUTPUT = PhDefaults.PRINT_OUTPUT
    PRINT_INFO = PhDefaults.PRINT_INFO
    QUITE_MODE = PhDefaults.QUITE_MODE
    # REMARKS
    ENCODING = PhDefaults.CHAR_ENCODING
    ENCODING_ERRORS = PhDefaults.ENCODING_ERRORS
    OUTPUT_PATH = PhDefaults.OUTPUT_PATH
    ARCHIVE_OUTPUT = PhDefaults.ARCHIVE_OUTPUT
    ARCHIVE_OUTPUT_FORMAT = PhDefaults.ARCHIVE_OUTPUT_FORMAT
    #
    OUTPUT_FORMAT = Formats.PNG
    SIZE = 5
    QR_CODE_VERSION = 5
    SPLIT_QRS = True
    DECORATE_QR = False


class DefaultTypesInclude:
    # Common Objects
    # INPUT_DATA
    PRINT_INPUT = PhDefaultTypesInclude.PRINT_INPUT
    PRINT_OUTPUT = PhDefaultTypesInclude.PRINT_OUTPUT
    PRINT_INFO = PhDefaultTypesInclude.PRINT_INFO
    QUITE_MODE = PhDefaultTypesInclude.QUITE_MODE
    # REMARKS
    ENCODING = PhDefaultTypesInclude.ENCODING
    ENCODING_ERRORS = PhDefaultTypesInclude.ENCODING_ERRORS
    OUTPUT_PATH = PhDefaultTypesInclude.OUTPUT_PATH
    ARCHIVE_OUTPUT = PhDefaultTypesInclude.ARCHIVE_OUTPUT
    ARCHIVE_OUTPUT_FORMAT = PhDefaultTypesInclude.ARCHIVE_OUTPUT_FORMAT
    # Specific Objects
    OUTPUT_FORMAT = str
    SIZE = int
    QR_CODE_VERSION = int
    SPLIT_QRS = bool
    DECORATE_QR = bool


class DefaultTypesExclude:
    # Common Objects
    INPUT_DATA: PhDefaultTypesExclude.INPUT_DATA
