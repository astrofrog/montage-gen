import os

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

LIB = os.path.join('..', '..', 'Montage', 'lib')
MONTAGELIB = os.path.join('..', '..', 'Montage', 'MontageLib')

extensions = [
    Extension("montage_wrappers._wrappers", ["montage_wrappers/_wrappers.pyx"],
        include_dirs = [os.path.join(LIB, 'include'), MONTAGELIB],
        libraries = ['wcs', 'coord','mtbl','cfitsio','m'],
        library_dirs = [LIB],
        extra_objects = [os.path.join(MONTAGELIB, 'libmontage.a')]),
    Extension("montage_wrappers.main", ["montage_wrappers/main.pyx"],
        include_dirs = [os.path.join(LIB, 'include'), MONTAGELIB],
        libraries = ['wcs', 'coord','mtbl','cfitsio','m'],
        library_dirs = [LIB],
        extra_objects = [os.path.join(MONTAGELIB, 'libmontage.a')])
]

setup(
    name="montage_wrappers",
    version="0.1.0.dev",
    packages=['montage_wrappers'],
    ext_modules = cythonize(extensions),
    )
