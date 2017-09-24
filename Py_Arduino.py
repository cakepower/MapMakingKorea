#!__*__coding:utf-8__*__
import serial
import time
from selenium import webdriver
import urllib.request

client_id = "GJmkt42zXCVIkwOoXz_n"
client_secret = "oVhPFocJFy"

#global driver
ser = serial.Serial('COM3', baudrate=9600, timeout=1)
#driver = None
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=sadi"
url = "http://www.sadi.net"
url = "https://www.instagram.com/explore/tags/%EC%82%AC%EB%94%94/"
#url = "https://www.instagram.com/explore/tags/%EA%B5%AD%EC%A0%95%EC%9B%90/"

while 1:
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
    if(arduinoData == 'C' or arduinoData == 'CC'):
        #if driver == None:
        browser = '.\\chromedriver\\chromedriver.exe'
        driver = webdriver.Chrome(browser)
        driver.get(url)
        time.sleep(1)
#    ser.write(b'N')


