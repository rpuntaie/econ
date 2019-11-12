#!/usr/bin/env python

from setuptools import setup
import os
from os.path import dirname
import ast

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), 'rt') as f:
    long_description = f.read()

os.chdir(here)

_version_re = re.compile(r'__version__\s*=\s*(.*)')
with open(os.path.join(here, 'econ', '__init__.py'), 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(name='econ',
      version=__version__,
      description='econ - support econ repo',
      license='GPLv3',
      author='Roland Puntaier',
      keywords=['Documentation'],
      author_email='roland.puntaier@gmail.com',
      url='https://github.com/rpuntaie/econ',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Topic :: Utilities',
          ],
      long_description=long_description
      install_requires=['rstdoc','click','sqlalchemy']
      packages=['econ'],
      package_data={'econ': ['../econ-1.0.rst'%__version__]},
      zip_safe=False,
      tests_require=['pytest', 'pytest-coverage', 'mock'],
      entry_points='''
        [console_scripts]
        econ=econ:cli
    ''',
)
