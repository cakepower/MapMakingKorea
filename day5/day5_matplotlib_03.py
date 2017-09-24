# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import numpy as np

font_location = "c:/windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc("font", family=font_name)

#x = np.linspace(0, 5, 10)
x = np.linspace(0, 5, 20)
y = x ** 2

plt.figure()
plt.plot(x, y, "r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("title")
plt.show()

