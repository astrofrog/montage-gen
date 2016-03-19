import os

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

LIB = os.path.join('..', '..', 'lib')
MONTAGELIB = os.path.join('..', '..', 'MontageLib')

extensions = [
    Extension("_gen", ["_gen.pyx"],
        include_dirs = [os.path.join(LIB, 'include'), MONTAGELIB],
        libraries = ['wcs', 'coord','mtbl','cfitsio','m'],
        library_dirs = [LIB],
        extra_objects = [os.path.join(MONTAGELIB, 'libmontage.a')])
]

setup(
    name = "My hello app",
    ext_modules = cythonize(extensions),
    )
