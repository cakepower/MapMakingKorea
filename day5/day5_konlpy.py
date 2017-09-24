#!__*__coding:utf-8__*__
from konlpy_test.tag import Hannanum, Kkma, Twitter, Komoran
import requests
from bs4 import BeautifulSoup
import os
#mycmd = "c:/curl/curl.exe -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh"
#os.system(mycmd)

result = "오늘은 참 좋은 날씨입니다. 저녁에 식당에 가서 삽겹살을 먹어야겠습니다."

k= Twitter()
r = k.nouns(result)
r.sort()
print(r)

