#!__*__coding:utf-8__*__
from konlpy.tag import Hannanum, Kkma, Twitter, Komoran
from collections import Counter
import csv

file = open(".\\data\\naver_news_절대미인.csv")
csv_reader = csv.reader(file)

for i in csv_reader:
    result = i[5]
    k= Twitter()
    r = k.nouns(result)
    x = Counter(r)
    print(x.most_common(5))

#mycmd = "c:/curl/curl.exe -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh"
#os.system(mycmd)

#result = "오늘은 참 좋은 날씨입니다. 저녁에 식당에 가서 삽겹살을 먹어야겠습니다. 삽겹살은 맛있습니다."



#r.sort()
#print(r)