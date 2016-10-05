# http://stackoverflow.com/questions/17014379/cython-cant-convert-python-object-to-double

cimport wrappers

cimport cpython.array as _array

{% for func in functions %}

cdef {{ func.name }}_cy({{ func.arguments_decl|join(', ') }}):
    cdef wrappers.{{ func.struct_name }} *ret
    ret = wrappers.{{ func.name }}({{ func.arguments|join(', ') }})
    retdict = {}
    {% for var in func.struct_vars %}retdict['{{ var }}'] = ret.{{ var }}
    {% endfor %}return retdict


def {{ func.name }}({{ func.arguments_with_defaults|join(', ') }}):
    {% for line in func.array %}
    {{ line }}
    {% endfor %}
    return {{ func.name }}_cy({{ func.arguments_py|join(', ') }})

{% endfor %}
