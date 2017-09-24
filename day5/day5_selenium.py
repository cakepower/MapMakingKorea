#!__*__coding:utf-8__*__
import time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = 'D:/ZZ.lecture/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(browser)
driver.get('http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=001&aid=0009547045')
time.sleep(3)

#for i in range(0, 10) :
#    driver.find_element_by_css_selector(".u_cbox_btn_more").click()
#    time.sleep(3)
#    i += 1

html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')
contents = bs.find_all("span", {"class" : "u_cbox_contents"})
for i in contents :
    print(str(i))
