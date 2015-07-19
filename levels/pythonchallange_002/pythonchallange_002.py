#!python
# -*- coding: UTF-8 -*-

# http://www.pythonchallenge.com/pc/def/ocr.html

import requests

r = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

full_source = r.text

secret = full_source[full_source.rfind("<!--")+5:-6]

b = []
answer = ""

for i in secret:
    if i not in answer:
        answer = answer + i

print(answer)