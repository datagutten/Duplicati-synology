#!/usr/bin/python3
import os.path
import re
import subprocess
import sys

url = 'https://updates.duplicati.com/beta/duplicati-2.0.6.3_beta_2021-06-17.zip'
matches = re.search(r'duplicati-([\d.]+)_(\w+)_', url)
version = matches.group(1)

folder = '/tmp/_duplicati_spk_build'
os.mkdir(folder)
local_zip = os.path.join(folder, 'duplicati_%s.zip' % version)

if not os.path.exists(local_zip):
    status = subprocess.call(['wget', '--ca-certificate', 'cacert.pem', '-O', local_zip, url])
    if status != 0:
        sys.exit(status)

status = subprocess.call(['unzip', '-q', '-d', folder, local_zip])
if status != 0:
    sys.exit(status)