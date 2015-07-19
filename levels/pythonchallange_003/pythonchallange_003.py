#!python
# -*- coding: UTF-8 -*-

# http://www.pythonchallenge.com/pc/def/equality.html

import string

import requests

r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")

full_source = r.text

secret = full_source[full_source.rfind("<!--")+5:-6].replace("\n","")

answer = ""
b = ""
there_is_more = True
coord = 0

for i in secret:
    if i in string.ascii_lowercase:
        b = b + '0'
    else:
        b = b + '1'

while there_is_more:
    coord = b.find('011101110', coord+1)

    if (coord == -1):
        there_is_more = False
    else:
        answer = answer + secret[coord+4]

print(answer)

