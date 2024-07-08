# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: find_location_icon.py
# @Author: jingfu.tao
# @E-mail: jingfu.tao@jiiov.com
# @Time: 1月 06, 2023
# ---
import numpy as np
import cv2 as cv
from glob import glob
import matplotlib.pyplot as plt
import math


# 取值范围
def get_distance(x, y, center=85):
    return math.sqrt((math.pow(x - center, 2) + math.pow(y - center, 2)))


if __name__ == "__main__":
    # 以下是读取MMI_raw代码：实现均图以及对应的画轴线
    height, width = 191, 191
    dis_end = height // 2
    b = np.zeros((height, width))
    new_b = np.zeros(b.shape)
    new_g = np.zeros(b.shape)
    new_r = np.zeros(b.shape)
    alpha = np.ones(b.shape) * 255
    aim_diameter = 191
    icon_ratio = aim_diameter / height
    for x, y in np.ndindex(width, height):
        distance = get_distance(x, y, center=dis_end)
        distance_ratio = distance / dis_end
        new_b[y][x] = 230 if distance_ratio <= icon_ratio else 0
        new_g[y][x] = 255 if distance_ratio <= icon_ratio else 0
        new_r[y][x] = 255 if distance_ratio <= icon_ratio else 0
        alpha[y][x] = 255 if distance_ratio <= icon_ratio else 0
    img_BGR = cv.merge((new_b, new_g, new_r, alpha))
    cv.imwrite("icon.png", img_BGR)


    """
    alpha = np.ones(b.shape) * 255
    aim_diameter = 100
    icon_ratio = aim_diameter / height

    for x, y in np.ndindex(width, height):
        distance = get_distance(x, y, center=dis_end)
        distance_ratio = distance / dis_end

        if distance_ratio <= icon_ratio:
            new_b[y][x] = 255
            print(1)
        elif distance_ratio <= 1:
            new_b[y][x] = 255
            print(2)

        if distance_ratio <= icon_ratio:
            new_g[y][x] = 0
        elif distance_ratio <= 1:
            new_g[y][x] = 255

        if distance_ratio <= icon_ratio:
            new_r[y][x] = 0
        elif distance_ratio <= 1:
            new_r[y][x] = 255

        alpha[y][x] = 255 if distance_ratio <= 1 else 0

    img_BGR = cv.merge((new_b, new_g, new_r, alpha))
    cv.imwrite("icon.png", img_BGR)
    """
