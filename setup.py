#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil -*-

from distutils.core import setup
from distutils.command.build_scripts import build_scripts as _build_scripts
from distutils.command.clean import clean as _clean
import glob
import os
import shutil

class custom_clean_command(_clean):
    description = "Custom clean command"
    user_options= _clean.user_options[:]
    def initialize_options(self):
        _clean.initialize_options(self)
        self.cwd = None
    def finalize_options(self):
        _clean.finalize_options(self)
        self.cwd = os.getcwd()
    def run(self):
        _clean.run(self)
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        shutil.rmtree('./build', ignore_errors=True)
        shutil.rmtree('./dist', ignore_errors=True)
        try:
            os.remove('MANIFEST')
        except:
            pass

class custom_build_scripts(_build_scripts):
    """Currently no-op extension of build_scripts command class"""
    description = "Custom build_scripts command"
    user_options = _build_scripts.user_options[:]
    def initialize_options(self):
        _build_scripts.initialize_options(self)
        self.cwd = None
    def finalize_options(self):
        _build_scripts.finalize_options(self)
        self.cwd = os.getcwd()
    def run(self):
        _build_scripts.run(self)

setup(name='indicator-session-idle-inhibit',
      version='0.1beta',
      description='Session idle inhibit indicator',
      long_description=open('README.txt').read(),
      author='Øyvind Stegard',
      author_email='oyvinst@ifi.uio.no',
      license='GPLv3',
      url='http://stegard.net/tools/',
      scripts=['bin/indicator-session-idle-inhibit'],
      data_files=[('share/applications',                ['data/indicator-session-idle-inhibit.desktop']),
                  ('share/icons/ubuntu-mono-dark/status/22', glob.glob('data/icons/ubuntu-mono-dark/status/22/*.svg')),
                  ('share/icons/ubuntu-mono-light/status/22', glob.glob('data/icons/ubuntu-mono-light/status/22/*.svg'))],
      requires=['appindicator', 'pyxdg'],
      cmdclass={ "build_scripts": custom_build_scripts, "clean": custom_clean_command }
)
