#!__*__coding:utf-8__*__

import os
import requests
from bs4 import BeautifulSoup


url = "http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=106&oid=030&aid=0002641631"

response = requests.get(url)
bs = BeautifulSoup(response.text, 'html.parser')
rs = bs.find(id='articleBodyContent')

#rs = bs.final_all("a", {"class":re.compile("nclic")})
#rs = bs.final_all("a", {"class":"nclic"})

for i in rs(["script", "style"]):
    i.decompose()

content = rs.get_text()
result = ""
for i in content.splitlines():
    if i.strip() == "":
        pass
    else:
        result += i
        result += "\n"

print(result)