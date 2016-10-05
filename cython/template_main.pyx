import _wrappers

{% for func in functions %}

def {{ func.name }}({{ func.arguments_with_defaults|join(', ') }}):
    return _wrappers.{{ func.name }}({{ func.arguments|join(', ') }})

{% endfor %}
