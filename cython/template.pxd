cdef extern from "montage.h":

    {% for func in functions %}

    cdef struct {{ func.struct_name }}:
        {% for declaration in func.struct_vars_decl %}{{ declaration }}
        {% endfor %}

    cdef {{ func.struct_name }} *{{ func.name }}({{ func.arguments_decl|join(', ') }})

    {% endfor %}
