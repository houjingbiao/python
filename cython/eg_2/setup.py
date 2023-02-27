# setup.py
# from distutils.core import setup, Extension
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import os

setup(ext_modules = cythonize(Extension(
    'main_opt',
    sources=['main_opt.pyx'],
    language='c',
    include_dir=["/home/houjingbiao/.local/lib/python3.8/site-packages/numpy/core/include"],
    library_dirs=[],
    libraries=[],
    extra_compile_args=[],
    extra_link_args=[]),
    language_level = "3"))