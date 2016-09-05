cimport montage_wrappers

{% for func in functions %}

cdef {{ func.name }}({{ func.arguments_decl|join(', ') }}):
    cdef montage_wrappers.{{ func.struct_name }} *ret
    ret = montage_wrappers.{{ func.name }}({{ func.arguments|join(', ') }})
    retdict = {}
    {% for var in func.struct_vars %}retdict['{{ var }}'] = ret.{{ var }}
    {% endfor %}return retdict    


def {{ func.name }}_py({{ func.arguments_with_defaults|join(', ') }}):
    return {{ func.name }}({{ func.arguments|join(', ') }})

{% endfor %}
