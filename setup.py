# -*- coding: UTF−8 -*-

import os

from setuptools import setup, find_packages

from qr_play.main.helper.constants_config import ConfigConst

# all packages dependencies
packages = find_packages()
if not packages:
    print(f'Selecting Hardcoded Packages')
    packages = [
        "qr_play.main",
        "qr_play.test",
        "qr_play.res",
    ]
print(f'Packages are {packages}')
# potential dependencies
install_reqs = [
    'incremental',
    'click',
    'twisted',
    'pillow',
    'segno',
]

setup_reqs = [
    'incremental',
]

# get long description from the README.md
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    use_incremental=True,
    setup_requires=setup_reqs,
    name=ConfigConst.TOOL_NAME,
    author="Pratik Jaiswal",
    author_email="impratikjaiswal@gmail.com",
    description=ConfigConst.TOOL_DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=ConfigConst.TOOL_URL,
    project_urls={
        "Bug Tracker": ConfigConst.TOOL_URL_BUG_TRACKER,
    },
    keywords=ConfigConst.TOOL_META_KEYWORDS,
    license="GNU GENERAL PUBLIC LICENSE v3.0",
    python_requires=">=3.9",
    packages=packages,
    install_requires=install_reqs,
    # Needed for Manifest.in
    # include_package_data=True,
    package_data={
        # Ref:
        "qr_play.res.images": ["*.png"],
        "qr_play.res.fonts": ["*.ttf", "*.otf"],
    },
    # test_suite="test.sample_package",
)
