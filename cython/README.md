Cython wrappers
---------------

To generate and build the wrappers, make sure that this repository is besides
the ``Montage`` directory, then do:

```
python parse.py
python setup.py build_ext --inplace
```

Then you can run the following script for an example:

```
python example.py
```
