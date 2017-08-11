#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import random #随机模块
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#Image          负责处理图片
#ImageDraw      负责处理画笔
#ImageFont      负责处理字体
#ImageFilter    负责处理滤镜

#1、定义一张图片

img = Image.new()

#第一个参数：
#第二个参数：
#第三个参数：代表图片的具体颜色

#2、创建画笔
draw = ImageDraw.Draw(img)

#2、绘制线条和点
    #一条线是由2个点组成的， 每个点的位置是由X, Y轴确定的

for i in range(random.randint(1, 10)):
    draw.line(
        [
            (
                random.randint(1, 150),
                random.randint(1, 150)
            ),
            (
                random.randint(1, 150),
                random.randint(1, 150)
            )
        ],
        fill = (0, 0, 0)
    )

for i in range(1000):
    draw.point(
        [
            random.randint(1, 150),
            random.randint(1, 150)
        ],
        fill = (0, 0, 0)
    )

#4、绘制我们的蚊子：
    #1、文字应该是随机产生的
    #2、文字个数是一定的

fontList = list("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
c_chars = " ".join(random.sample(fontList, 5))
# random.sample 是在指定的列表中随机的取出指定个元素

font = ImageFont.truetype("simsun.ttc", 26)
draw.text
img.show()