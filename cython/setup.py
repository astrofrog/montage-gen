from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("_test", ["_test.pyx"],
        include_dirs = ['../lib/include/'],
        libraries = ['wcs', 'coord','mtbl','cfitsio','m'],
        library_dirs = ['../lib/'],
        extra_objects = ['../MontageLib/libmontage.a'])
]

setup(
    name = "My hello app",
    ext_modules = cythonize(extensions),
    )
