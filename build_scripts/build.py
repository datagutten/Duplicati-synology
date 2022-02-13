#!/usr/bin/python3
import os.path
import re

url = os.getenv('ZIP_URL')
if not url:
    raise ValueError('Environment variable ZIP_URL not set')

matches = re.search(r'duplicati-([\d.]+)_(\w+)_', url)
version = matches.group(1)
script_folder = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(script_folder, 'INFO_template')) as fp_template:
    template = fp_template.read()
    template += '\n' + 'version="%s"' % version
    with open('INFO', 'w') as fp_info:
        fp_info.write(template)
    with open('VERSION', 'w') as fp_version:
        fp_version.write(version)
