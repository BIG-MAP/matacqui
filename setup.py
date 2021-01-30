# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'Eibar Flores'
__license__ = 'GPLv3'
__contributors__ = ['Martin Uhrin']

about = {}
with open('matacqui/version.py') as f:
    exec(f.read(), about)  # pylint: disable=exec-used

setup(name='matacqui',
      version=about['__version__'],
      description='Materials Acquisition Form for BIG-MAP',
      long_description=open('README.rst').read(),
      url='https://github.com/muhrin/milad.git',
      author='Eibar Flores',
      author_email='eibfl@dtu.dk',
      license=__license__,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      keywords='materials acquisition',
      install_requires=['appmode', 'reportlab', 'mincepy', 'dnspython', 'jupyter', 'notebook'],
      extras_require={
          'dev': [
              'ipython',
              'pip',
              'pytest~=5.4',
              'pytest-cov',
              'pre-commit~=2.2',
              'prospector',
              'pylint==2.5.2',
              'twine',
              'yapf',
          ],
      },
      packages=[
          'matacqui',
      ],
      include_package_data=True,
      test_suite='test',
      entry_points={
          'mincepy.plugins.types': ['matacqui_types = matacqui.provides:get_mince_types'],
      })
