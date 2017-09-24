#!__*__coding:utf-8__*__

import requests

test_url = "http://blog.naver.com/nadiatear0?Redirect=Log&logNo=221078980434"
test_url2 = "http://blog.naver.com/PostView.nhn?blogId=nadiatear0&logNo=221078980434&beginTime=0&jumpingVid=&from=search&redirect=Log&widgetTypeCall=true"

response = requests.get(test_url2)

f=open(".\\data\\naver_cr2.txt", "w", encoding='utf-8')
f.write(response.text)
f.close()

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
result_txt = soup.get_text()
t = soup.find(id="postViewArea")
result_txt = t.get_text()

f = open(".\\data\\naver_cr_3.txt", "w", encoding='utf-8')
f.write(result_txt)
f.close()