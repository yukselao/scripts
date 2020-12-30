#!/usr/bin/python3

###
# 2020-12-30
# e-mail: aliokan.yuksel@siyahsapka.org
# notes:
# --
# Tested on PanOS 8.x
# Usage:
# chmod +x change-passwd.py
# ./change-passwd.py <ip> <username> <CurrentPassword> <NewPassword>
###

import requests, re, sys, crypt

fwip=str(sys.argv[1])
username=str(sys.argv[2])
currentpass=str(sys.argv[3])
newpass=str(sys.argv[4])
print("INFO Appliance Url: https://"+ fwip)
print("INFO username: "+ username)
print("INFO current password: "+ currentpass)
print("INFO newpassword: "+ newpass)

newhash=str(crypt.crypt(newpass, crypt.mksalt(crypt.METHOD_MD5)))

params = (
    ('type', 'keygen'),
    ('user', username),
    ('password', currentpass),
)
response = requests.get("https://"+fwip+'/api/', params=params, verify=False)
r=response.text
key=re.findall(r".+<key>(.+)</key>.+",r)[0]

url="https://"+fwip+'''/api/?type=config&action=set&key='''+key+"&xpath=/config/mgt-config/users/entry[@name='"+username+"']&element=<phash>"+newhash+'''</phash>'''
response = requests.get(url, verify=False)
r=response.text

url='https://'+username+':'+newpass+'@'+fwip+'/api/?type=commit&cmd=<commit><force></force></commit>'
response = requests.get(url, verify=False)
r=response.text
print(r)



