#!__*__coding:utf-8__*__

import os
import sys
import glob
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat
from konlpy.tag import Hannanum, Kkma, Twitter, Komoran
from collections import Counter

font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name)

#f = open(".\\data\\data.txt", "r", encoding='utf-8')
#content = f.read()

file = open(".\\data\\naver_news_북한.csv", encoding='cp949' )
csv_reader = csv.reader(file)

col_r = []
for i in csv_reader:
    result = i[5]
    k= Twitter()
    r = k.nouns(result)
    col_r += r

print(col_r)
words_list = ["것", "수", "고", "일", "이", "문", "형", "재", "등"]
#words_list_set = set(words_list)
#col_r_set = set(col_r)
#y = col_r_set - words_list_set
#print (y)
#y = list(y)

for i in col_r:
    if i in words_list:
        col_r.remove(i)

x = Counter(col_r).most_common(10)


print(x)
headers = []
values = []
for i in x:
    headers.append(i[0])
    values.append(i[1])

x = range(len(values))
plt.bar(x, values, width=0.5)
plt.xticks(x, headers)
plt.show()
