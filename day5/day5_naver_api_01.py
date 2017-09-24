#!__*__coding:utf-8__*__

import os
import sys
import urllib.parse
import json
import csv
import requests
import html
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import time
#from urlparse import urlparse

CLIENT_ID = "JgFePQpRlo8WsOVzP5zL"
CLIENT_SECRET_ID = "fWKDntC3kY"
BLOG_SEARCH_URL = "https://openapi.naver.com/v1/search/blog?query="
NEWS_SEARCH_URL = "https://openapi.naver.com/v1/search/news.json?query="


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


def get_naver_blog_crawling(url):
    x = urllib.parse.urlparse(url)
    host_address = "%s://%s/" % (x.scheme, x.netloc)
    url = html.unescape(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find(id="mainFrame")
    if result is None:
        return False
    else:
        level2_url = result["src"]
        level2_url = urllib.parse.urljoin(host_address, level2_url)
        response = requests.get(level2_url)
        level2_soup = BeautifulSoup(response.text, 'html.parser')
        level2_result = level2_soup.find(id="postListBody")
        if level2_result == None:
            print(level2_url)
        content = level2_result.get_text("\n")
        content = remove_space(content)
        return content
    pass


driver = None


def get_social_comment(url, html_content):
    global driver
    browser = 'D://ZZ.lecture/chromedriver_win32/chromedriver.exe'
    #browser = 'Z://chromedriver_win32/chromedriver.exe'
    if driver is None:
        driver = webdriver.Chrome(browser)
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.find_all("span", {"class": "u_cbox_contents"})
    result = []

    for i in contents:
        print(str(i))
        result.append(str(i.get_text()))

    return "@@@".join(result)
    pass


def get_naver_news_crawling(url):
    url = html.unescape(url)
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    if url.find("entertain.naver.com") >= 0:
        find_id = "articeBody"
    elif url.find("news.naver.com") >= 0:
        find_id = "articleBodyContents"
    else:
        find_id = "none"
    result = soup.find(id=find_id)

    if result is None:
        return (False, False)
    else:
        for script in result(["script", "style"]):
            script.decompose()
            script.extract()
        content = result.get_text("\n")
        content = remove_space(content)

        if url.find("news.naver.com") >= 0:
            comment_content = get_social_comment(url, html_content)
        else:
            comment_content = ""
        return (content, comment_content)


def get_query(keyword, x, type="blog"):
    print("get_query function")

    encText = urllib.parse.quote(keyword)
    #url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    if type == "blog":
        url = BLOG_SEARCH_URL + encText + "&display=100&start=" + x
    elif type == "news":
        url = NEWS_SEARCH_URL + encText + "&display=100&start=" + x
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    naver_headers = {}
    naver_headers["X-Naver-Client-Id"] = CLIENT_ID
    naver_headers["X-Naver-Client-Secret"] = CLIENT_SECRET_ID
    response = requests.get(url, headers=naver_headers, cookies={})
    rescode = response.status_code

    if(rescode==200):
        response_body = response.text
        return response_body
    else:
        print("Error Code:" + rescode)


def run_naver_search_from_blog(keyword):
    print("run_naver_search_from_blog function")

    fout = open("naver_result_%s.csv" % keyword, "w", encoding="utf=8", newline= "")
    csv_writer = csv.writer(fout)

    for i in range(1, 1000, 100):
        a = get_query(keyword, str(i))
        b = json.loads(a, encoding="utf-8")

        for x in b["items"]:
            rx = []
            rx.append(remove_html_tag(x["title"]))
            rx.append(x["link"])
            rx.append(x["bloggername"])
            rx.append(x["bloggerlink"])
            rx.append(x["postdate"])
            rx.append(remove_html_tag(x["description"]))

            if x["link"].find("blog.naver.com") >= 0:
                content = get_naver_blog_crawling(x["link"])
            else:
                content = ""
                pass
            rx.append(content)
            csv_writer.writerow(rx)
            #break

    fout.close()


def run_naver_search_from_news(keyword):
    print("run_naver_search_from_news function")

    fout = open("naver_news_result_%s.csv" % keyword, "w", encoding="utf=8", newline= "")
    csv_writer = csv.writer(fout)

    for i in range(1, 1000, 100):
        a = get_query(keyword, str(i), type="news")
        b = json.loads(a, encoding="utf-8")

        for x in b["items"]:
            rx = []
            rx.append(remove_html_tag(x["title"]))
            rx.append(x["link"])
            if x["link"].find("naver.com") >= 0:
                (content, comment_content) = get_naver_news_crawling(x["link"])
            else:
                content = ""
                comment_content = ""
            rx.append(x["originallink"])
            rx.append(x["pubDate"])
            rx.append(remove_html_tag(x["description"]))
            rx.append(content)
            rx.append(comment_content)
            csv_writer.writerow(rx)
            #break

    fout.close()