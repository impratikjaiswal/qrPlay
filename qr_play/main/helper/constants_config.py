from qr_play._git_info import GIT_SUMMARY
from qr_play._tool_name import TOOL_NAME
from qr_play._version import __version__


class ConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = 'QR Play'
    TOOL_GIT_SUMMARY = GIT_SUMMARY
    TOOL_DESCRIPTION = f'Qr Code Generator. Multiple Qr codes can be generated automatically when input text does not fit in one.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, QR, QR code, QR Code Generator, Quick Response Code, QRcode Generator, Qrcode, Multiple Qrcode Generator, Multiple Qr Code Generator'
    TOOL_URL = 'https://github.com/impratikjaiswal/qrPlay'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/qrPlay/issues'
