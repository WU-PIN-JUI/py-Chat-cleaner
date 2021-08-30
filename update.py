import py7zr
import requests
import hashlib
import os
channelt = open('channel', 'r').read()
open('channel', 'r').close()
channellist = str(channelt).splitlines()
channel = channellist[0]
print('channel = ' + str(channel))
url = 'https://raw.githubusercontent.com/WU-PIN-JUI/py-Chat-cleaner/' + str(channel) + '/v' 
print('url = ' + str(url))
vt = requests.get(url)
if vt.status_code == requests.codes.ok:
    vt2 = str(vt.text).splitlines()
    v = vt2[0]
    print('version = ' + str(v))
    os.remove('v')
    open('v', 'w').write(v)
    open('v', 'w').close()
else:
    print('Update error (can\'t get version file)')
    exit()
