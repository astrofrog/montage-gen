import os

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

if os.path.exists(os.path.join('..', 'Montage')):
    LIB = os.path.join('..', 'Montage', 'lib')
    MONTAGELIB = os.path.join('..', 'Montage', 'MontageLib')
elif os.path.exists(os.path.join('..', '..', 'Montage')):
    LIB = os.path.join('..', '..', 'Montage', 'lib')
    MONTAGELIB = os.path.join('..', '..', 'Montage', 'MontageLib')
else:
    raise ValueError("Could not find the Montage directory")

extensions = [
    Extension("montage_direct._wrappers", ["montage_direct/_wrappers.pyx"],
        include_dirs = [os.path.join(LIB, 'include'), MONTAGELIB],
        libraries = ['wcs', 'coord','mtbl','cfitsio','m', 'boundaries', 'freetype', 'twoplane', 'pixbounds', 'www', 'json', 'lodepng', 'cmd'],
        library_dirs = [LIB, os.path.join(LIB, 'freetype', 'lib')],
        extra_objects = [os.path.join(MONTAGELIB, 'libmontage.a'), os.path.join(LIB, 'libjpeg.a')]),
    Extension("montage_direct.main", ["montage_direct/main.pyx"],
        include_dirs = [os.path.join(LIB, 'include'), MONTAGELIB],
        libraries = ['wcs', 'coord','mtbl','cfitsio','m', 'boundaries', 'freetype', 'twoplane', 'pixbounds', 'www'],
        library_dirs = [LIB, os.path.join(LIB, 'freetype', 'lib')],
        extra_objects = [os.path.join(MONTAGELIB, 'libmontage.a')])
]

setup(
    name="montage_direct",
    version="0.1.0.dev",
    packages=['montage_direct'],
    ext_modules = cythonize(extensions),
    )
