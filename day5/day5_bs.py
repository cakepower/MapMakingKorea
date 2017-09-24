#!__*__coding:utf-8__*__
from bs4 import BeautifulSoup
import requests
import re

url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=001&aid=0009547045'
response = requests.get(url)
html_content = response.text
print(response.text)
bs = BeautifulSoup(html_content, 'html.parser')

print(bs.title)
print(bs.find_all("a"))
print("A" * 10)

x = bs.find_all("a", {"class":"thumb"})
print(x)
print("B" * 10)
for i in x:
    print(i.attrs)
    print(i["href"])

print("C" * 10)
x = bs.find_all(id="lyr_dimmed")
print(x)
print("D" * 10)

#x = bs.find_all(id*=re.compile("^rel\."))
x = bs.find_all(id=re.compile("in"))
print(x)
print("E" * 10)

x = bs.find_all("a", {"class":re.compile("nclic")})
print(x)
print("F" * 10)

y = bs.get_text()
print(y)

for i in bs(["script", "style"]):
    print(dir(i))
    print(i.attrs)
    print(i.get_text())
    i.decompose()

y = bs.get_text()
print(y)
print(" ".join(y.split()))


y = bs.get_text("\n")
print(y)
result = ""
for i in y.splitlines():
    if i.strip() != "":
        result = result + " ".join(i.split()) + "\n"
print(result)

    #print(i)
#print(bs.find("div"))
#contents = bs.find_all("span", {"class": "u_cbox_contents"})