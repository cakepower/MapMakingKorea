#1__*__ UTF-8

import os
import sys
import requests
import json
from pytagcloud import create_tag_image, make_tags
from collections import Counter

mykey = "1c601a5ad546134edad4c84890aa4260"
URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
key = "?key="+mykey+"&targetDt=20170901"
titles_dic = {}

def draw_pytagcloud(data_array):
    words_count = Counter(data_array)
    counts = words_count.most_common(100)
    tags = make_tags(counts, minsize=10, maxsize=60)
    print(type(tags))
    create_tag_image(tags, "movie_large.png", size=(900,600), fontname="Nanum Gothic", rectangular=False)

def get_month(i):
    global URL, mykey
    i = str(i)
    if len(i) == 1:
        i = "0"+i
    key = URL + "?key=" + mykey + "&targetDt=2016" + "10" + i
    return key

movie_lst = []
movie_lst2 = []
titles_array = []
titles_dic = {}

for j in range(1, 13):
    URL_1 = get_month(j)
    response = requests.get(URL_1)
    result = response.text
    result = json.loads(result, encoding="utf-8")
    x = result["boxOfficeResult"]["dailyBoxOfficeList"]

    for items in x:
        title_key = items["movieNm"]
        if title_key not in titles_dic:
            titles_dic[title_key] = 1
        else:
            titles_dic[title_key] = titles_dic[title_key] + 1

        # print(items["movieNm"])
        movie_lst.append(items["movieNm"])
        movie_lst2.append(str(items["movieNm"]))
    movie_lst.append("\n")

draw_pytagcloud(movie_lst)
f = open("movie_result.txt", "w")
for i in movie_lst:
    f.write(str(i))
    if (i == "\n"):
        pass
    else:
        f.write(",")
f.close()

report = open("result.txt", "w")
for title in titles_dic:
    report.write(title + ":")
    report.write(str(titles_dic[title]))
    report.write("\n")
report.close()

