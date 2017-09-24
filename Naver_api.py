#!__*__coding:utf-8__*__
# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import urllib.parse
import requests
import json
import csv
import html.parser
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from konlpy.tag import Hannanum, Kkma, Twitter, Komoran
from collections import Counter


client_id = "GJmkt42zXCVIkwOoXz_n"
client_secret = "oVhPFocJFy"


MY_MOVIE_KEY = "1c601a5ad546134edad4c84890aa4260"
MOVIE_URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"


my_Twitter = None
def get_nouns(comment):
    global my_Twitter
    if my_Twitter is None:
        my_Twitter = Twitter()

    k = my_Twitter.nouns(comment)
    return " ".join(k)

def remove_html_tag(my_string):
    a = BeautifulSoup(my_string, 'html.parser')
    return a.get_text()

def remove_space(my_content):
    result = ""
    for i in my_content.splitlines():
        if i.strip() == "":
            pass
        else:
            x = " ".join(i.split())
            result += x
            result += "\n"
    return result

def get_querry(keyword,x,type):
    encText = urllib.parse.quote(keyword)
    #url = "https://openapi.naver.com/v1/search/blog?query=" + encText +"&display=100&sort=date&start="+str(x)# json 결과

    if type == "blog":
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText +"&display=100&start=" + x # json 결과
    elif type == "news":
        url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100&start=" + x  # json 결과

    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body
    else:
        print("Error Code:" + rescode)

def get_querry_2(keyword,x,type):
    encText = urllib.parse.quote(keyword)
    #url = "https://openapi.naver.com/v1/search/blog?query=" + encText +"&display=100&sort=date&start="+str(x)# json 결과

    if type == "blog":
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText +"&display=100&start=" + x # json 결과
    elif type == "news":
        url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=100&start=" + x  # json 결과

    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    naver_headers = {}
    naver_headers['X-Naver-Client-Id'] = client_id
    naver_headers['X-Naver-Client-Secret'] = client_secret
    response = requests.get(url, headers=naver_headers, cookies={})
    rescode = response.status_code

    if(rescode==200):
        response_body = response.text
        return response_body
    else:
        print("Error Code:" + rescode)


def run_naver_search_from_blog(keyword):
    f_out = open(".\\data\\naver_blog_%s.csv" % keyword, "w" , encoding='utf-8', newline="")
    csv_writer = csv.writer(f_out)
    for i in range(1, 100, 100):
        a = get_querry(keyword, str(i), "blog")
        b = json.loads(a, encoding='utf-8')
        for items in b['items']:
            rx = []
            rx.append(items['title'])
            rx.append(items['link'])
            rx.append(items['bloggername'])
            rx.append(items['bloggerlink'])
            rx.append(items['postdate'])
            csv_writer.writerow(rx)

    f_out.close()

def run_naver_search_from_news(keyword):
    f_out = open(".\\data\\naver_news_%s.csv" % keyword, "w" , encoding='utf-8', newline="")
    csv_writer = csv.writer(f_out)
    for i in range(1, 100, 100):
        a = get_querry_2(keyword, str(i), "news")
        b = json.loads(a, encoding='utf-8')
        for items in b['items']:
            rx = []
            rx.append(remove_html_tag(items['title']))
            rx.append(items['link'])
            rx.append(items['originallink'])
            rx.append(remove_html_tag(items['description']))
            rx.append(items['pubDate'])

            if items['link'].find("news.naver.com") >= 0:
                content, comment = get_naver_news_crawling_comment(items['link'])
            elif items['link'].find("entertain.naver.com") >= 0:
                content, comment = get_naver_news_crawling_comment(items['link'])
            elif items['link'].find("topstarnews.net") >= 0:
                content, comment = get_naver_news_crawling_comment(items['link'])
            elif items['link'] != None:
                content, comment = get_naver_news_crawling_comment(items['link'])
            else:
                content = ""
                comment = ""
            rx.append(content)
            rx.append(comment)
            csv_writer.writerow(rx)

    f_out.close()

driver = None
def get_naver_news_crawling_comment(url):
    global  driver
    if driver == None:
        browser = '.\\chromedriver\\chromedriver.exe'
        driver = webdriver.Chrome(browser)
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    if url.find("entertain.naver.com") >= 0:
        find_id = "articeBody"
    elif url.find("news.naver.com") >= 0:
        find_id = "articleBodyContents"
    elif url.find("topstarnews.net") >=0:
        find_id = "adnmore_inImage"
    else:
        find_id = "none"

    main_result = bs.find(id=find_id)


    if main_result is None:
        return (False, False)
    else:
        for script in main_result(["script", "style"]):
            script.decompose()
            script.extract()
        content = main_result.get_text("\n")
        content = remove_space(content)

        contents = bs.find_all("span", {"class": "u_cbox_contents"})
        result = []

    # main_result = main_result.get_text()
        for i in contents:
           # print(str(i))
            result.append(str(i.get_text()))

        y = "".join(result)
        result = get_nouns(y)
        comment_content = "@@@".join(result)

        return (content, comment_content)
    pass





if __name__ == '__main__':
    a = input("Crawling File Name: ")
    run_naver_crawling(a)