from qr_play.main.helper.formats import Formats


class FormatsGroup:
    IMAGE_FORMATS_SUPPORTED = [
        Formats.PNG,
        Formats.PNG_URI,
        Formats.SVG,
        Formats.SVG_URI,
    ]

    QR_CODE_VERSIONS_SUPPORTED = list(range(40, 0, -1))
