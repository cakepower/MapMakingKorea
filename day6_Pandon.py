#!__*__coding:utf-8__*__

import os
import sys
import glob
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name)

folder = r'.\data\download\*.csv'
files = glob.glob(folder)

y = []
x_ticks = []
for one_file in files:
    m = one_file[:-6]
    h = m[-4:]
    x_ticks.append(h)
    f = open(one_file, "r", encoding='cp949')
    csv_reader = csv.reader(f)

    x = 0
    for cols in csv_reader:
        try:
            x = x + int(cols[4])
        except:
            pass
    y.append(x)


x = range(len(y))
axes = plt.gca()
axes.set_ylim([400000, 450000])
plt.plot(x, y)
plt.bar(x,y,width = 0.8)
plt.ylabel("인구수")
plt.xlabel("월")
plt.xticks(x, x_ticks)
plt.show()
