#!/usr/bin/env python3
from setuptools import setup

APP = ['menubar.py']
OPTIONS = {
    'argv_emulation': False,
    'iconfile': None,
    'plist': {
        'CFBundleDisplayName': 'MenuBar',
        'CFBundleIdentifier': 'com.user.menubar',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': [],
    'includes': ['rumps'],
    'excludes': [],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)