#!/usr/bin/python

###
# 2020-12-30
# e-mail: aliokan.yuksel@siyahsapka.org
###

import requests, re, sys, crypt

username=str(sys.argv[1])
currentpass=str(sys.argv[2])
newpass=str(sys.argv[3])
print("INFO username: "+ username)
print("INFO current password: "+ currentpass)
print("INFO newpassword: "+ newpass)

newhash=str(crypt.crypt(newpass, crypt.mksalt(crypt.METHOD_MD5)))

params = (
    ('type', 'keygen'),
    ('user', username),
    ('password', currentpass),
)
response = requests.get('https://172.16.28.25/api/', params=params, verify=False)
r=response.text
key=re.findall(r".+<key>(.+)</key>.+",r)[0]

url='''https://172.16.28.25/api/?type=config&action=set&key='''+key+"&xpath=/config/mgt-config/users/entry[@name='"+username+"']&element=<phash>"+newhash+'''</phash>'''
response = requests.get(url, verify=False)
r=response.text

url='https://'+username+':'+newpass+'@172.16.28.25/api/?type=commit&cmd=<commit><force></force></commit>'
response = requests.get(url, verify=False)
r=response.text
print(r)



