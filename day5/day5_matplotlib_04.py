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

fig = plt.figure(figsize=(100, 100), dpi=100)  # 그림 사이즈, 해상도 설정

plt.subplot(2, 2, 1)
plt.plot(x, y, "r")
plt.subplot(2, 2, 2)
plt.plot(x, y, "ro")
plt.subplot(2, 2, 3)
plt.plot(x, y, "r-")
plt.subplot(2, 2, 4)
plt.plot(x, y, "r+")
plt.show()


plt.subplot(2, 2, (1, 3))
plt.plot(x, y, "r")
plt.subplot(2, 2, 2)
plt.plot(x, y, "r")
plt.subplot(2, 2, 4)
plt.plot(x, y, "r")
plt.show()

