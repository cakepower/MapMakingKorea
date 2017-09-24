#!__*__coding:utf-8__*__
#이 파일을 계속 확장해 나갈 것입니다.

import os
import sys
import string
import csv
from pytagcloud import create_tag_image, make_tags, LAYOUT_HORIZONTAL, LAYOUTS
from collections import Counter
import requests
import json
from my_help import help_screen

MY_KEY = "1c601a5ad546134edad4c84890aa4260"
URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"

# menu
# Display a menu
# Accepts no parameters
# Returns the string entered by the user.
def menu():
    # Display a menu
    return input("=== F)ile M)ovie H)elp Q)uit ===")


def draw_pytagcloud(data_array, image_filename):
    words_count = Counter(data_array)
    counts = words_count.most_common(50)
    tags = make_tags(counts, maxsize=50)
    create_tag_image(tags, image_filename, size=(900, 600), fontname='Nanum Gothic')


def get_month(i):
    j = str(i)
    if not j.isdigit():
        return False
    j = j.zfill(2)
    return j


def get_movie_data():
    global URL, MY_KEY

    movie_array = []
    f_result = open(".\\data\\my_movie_result_15.csv", "w")
    for i in range(1, 13):
        j = get_month(i)
        my_url = URL + "?key=" + MY_KEY + "&targetDt=2015" + j + "01"
        response = requests.get(my_url)
        result = response.text
        result_2 = json.loads(result, encoding="utf-8")

        f_result.write(str(i) + ",")

        for x in result_2["boxOfficeResult"]["dailyBoxOfficeList"]:
            movie_array.append(x["movieNm"])
            print(x["movieNm"])
            f_result.write(x["movieNm"])
            f_result.write(",")
        f_result.write("\n")

    f_result.close()
    draw_pytagcloud(movie_array, ".\\images\\cloud_large_movie.png")


def csv_file_open3():
    filename = input("input csv filename: ")
    #filename = ".\\data\\bbb.csv"
    x = os.path.splitext(filename)
    output_filename = x[0] + "_result" + x[1]

    try:
        f = open(filename, "r")
    except FileNotFoundError as e:
        print(e)
    else:
        csv_reader = csv.reader(f)
    finally:
        f.close()

    f2 = open(output_filename, "w")
    titles_array = []
    titles_dic = {}

    for one_row in csv_reader:
        title_key = one_row[1]
        titles_array.append(title_key)
        if title_key not in titles_dic:
            titles_dic[title_key] = 1
        else:
            titles_dic[title_key] += 1

    for title_key in titles_dic:
        f2.write("%s, %d\r\n" % (title_key, titles_dic[title_key]))

    f2.close()

    draw_pytagcloud(titles_array, '.\\images\\cloud_large.png')

if __name__ == "__main__":
    help_screen()
    while True:
        val = menu().upper()
        if val not in ["F", "M", "H", "Q"]:
            print("wrong input")
            continue
        if val == "H":
            help_screen()
        elif val == "Q":
            break
        elif val == "M":
            get_movie_data()
        else:
            csv_file_open3()
            pass