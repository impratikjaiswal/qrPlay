from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from qr_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    QUITE_MODE = False
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    QR_CODE_VERSION = 5
    SCALE = 5
    IMAGE_FORMAT = Formats.PNG_URI
    SPLIT_QRS = True
