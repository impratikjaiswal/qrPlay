from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from qr_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = True
    PRINT_INPUT = False
    PRINT_OUTPUT = True
    QUITE_MODE = False
    QR_CODE_VERSION = 40
    SCALE = 10
    IMAGE_FORMAT = Formats.PNG
    SPLIT_QRS = True
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
