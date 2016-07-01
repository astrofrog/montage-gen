import os
import glob
import json
from jinja2 import Template

MONTAGELIB = os.path.join('..', '..', 'Montage', 'MontageLib')

CTYPE = {}
CTYPE['int'] = 'int '
CTYPE['int*'] = 'int '
CTYPE['integer'] = 'int '
CTYPE['char'] = 'char '
CTYPE['string'] = 'char *'
CTYPE['string*'] = 'char *'
CTYPE['boolean'] = 'int '
CTYPE['boolean*'] = 'int '
CTYPE['double'] = 'double '
CTYPE['double*'] = 'double *'

with open('template.pxd', 'r') as f:
    template_pxd = Template(f.read())

with open('template.pyx', 'r') as f:
    template_pyx = Template(f.read())

functions = []

for json_file in glob.glob(os.path.join(MONTAGELIB, '*', '*.json')):

    print("Parsing {0}...".format(json_file))

    with open(json_file, 'r') as fjson:
        data = json.load(fjson)

    if data['return'] is None:
        continue

    function = {}
    function['name'] = data['function']
    function['struct_name'] = data['function'] + "Return"

    function['arguments'] = []
    function['arguments_decl'] = []
    for inp in data['arguments']:
        argument = "{0}{1}".format(CTYPE[inp['type']], inp['name'])
        function['arguments'].append(inp['name'])
        function['arguments_decl'].append(argument)

    function['struct_vars'] = []
    function['struct_vars_decl'] = []
    for ret in data['return']:
        if len(ret) == 0:
            continue
        struct_var = "{0}{1}".format(CTYPE[ret['type']], ret['name'])
        function['struct_vars'].append(ret['name'])
        function['struct_vars_decl'].append(struct_var)

    functions.append(function)

with open('montage_wrappers.pxd', 'w') as f:
    f.write(template_pxd.render(functions=functions))

with open('_montage_wrappers.pyx', 'w') as f:
    f.write(template_pyx.render(functions=functions))