cimport gen

{% for func in functions %}

cdef {{ func.name }}({{ func.arguments_decl|join(', ') }}):
    cdef gen.{{ func.struct_name }} *ret
    ret = gen.{{ func.name }}({{ func.arguments|join(', ') }})
    retdict = {}
    {% for var in func.struct_vars %}retdict['{{ var }}'] = ret.{{ var }}
    {% endfor %}return retdict    

{% endfor %}
