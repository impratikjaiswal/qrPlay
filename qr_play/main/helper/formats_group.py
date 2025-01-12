from qr_play.main.helper.formats import Formats


class FormatsGroup:
    OUTPUT_FORMATS_SUPPORTED = [
        Formats.PNG,
        Formats.PNG_URI,
        Formats.SVG,
        Formats.SVG_URI,
    ]

    OUTPUT_FORMATS_IMAGE_FILES = [
        Formats.PNG,
        Formats.SVG
    ]

    OUTPUT_FORMATS_PNG_IMAGES = [
        Formats.PNG,
        Formats.PNG_URI
    ]

    QR_CODE_VERSIONS_SUPPORTED = list(range(40, 0, -1))
