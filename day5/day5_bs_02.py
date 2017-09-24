#!__*__coding:utf-8__*__
from bs4 import BeautifulSoup
import requests
import re

bs = BeautifulSoup("<html><body></body></html>", "html.parser")

new_tag = bs.new_tag("a", href="http://www.chosun.com", id="new_id", **{"class":"test", "onClink":"test()"})
new_tag.string = "click here"

bs.body.append(new_tag)

print(str(bs))
print(bs.prettify())
