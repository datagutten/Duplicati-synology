#!/usr/bin/python3
import os.path
import re
import subprocess

url = 'https://updates.duplicati.com/beta/duplicati-2.0.6.3_beta_2021-06-17.zip'
matches = re.search(r'duplicati-([\d.]+)_(\w+)_', url)
version = matches.group(1)

folder = '/tmp/_duplicati_spk_build'
os.mkdir(folder)
local_zip = os.path.join(folder, 'duplicati_%s.zip' % version)

if not os.path.exists(local_zip):
    subprocess.run(['wget', '-O', local_zip, url])
subprocess.run(['unzip', '-q', '-d', folder, local_zip])
