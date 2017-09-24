#!__*__coding:utf-8__*__
import tweepy
import os

TOKEN = "44498241-6O6QZbeJ13v3oS6OmVXLnkU7gHzfyDctQ1jIlCk"
TOKEN_KEY = "lPyhLTPIacEamNtouEXAOaZOaZviIruLjDDWdWcyhrI"
CON_SECRET = "sy9SrErwMFoJRv1M0Ywug"
CON_SECRET_KEY = "uxHZxm56KfI6TPwpRepRqn4Kvna920Hb3jpNoZ5NrF4"


def get_twit():
    auth = tweepy.OAuthHandler(CON_SECRET, CON_SECRET_KEY)
    auth.set_access_token(TOKEN, TOKEN_KEY)
    api = tweepy.API(auth)

    location = "%s,%s,%s" % ("35.95", "128.25", "1000km")  # 검색기준(대한민국 중심) 좌표, 반지름
    keyword = "#임시공휴일"  # OR 로 검색어 묶어줌, 검색어 5개(반드시 OR 대문자로)                               # api 생성
    wfile = open(os.getcwd() + "/twitter.txt", mode='w', encoding="utf-8")  # 쓰기 모드

    # twitter 검색 cursor 선언
    cursor = tweepy.Cursor(api.search,
                           q=keyword,
                           since='2016-01-01',  # 2015-01-01 이후에 작성된 트윗들로 가져옴
                           count=100,  # 페이지당 반환할 트위터 수 최대 100
                           geocode=location,  # 검색 반경 조건
                           include_entities=True)

    for i, tweet in enumerate(cursor.items()):
        print("{}: {}".format(i, tweet.text))

        wfile.write(tweet.text + '\n')
    wfile.close()


get_twit()