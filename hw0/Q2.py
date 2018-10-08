# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open("westbrook.jpg")
pix = im.load()
# 获得图像尺寸:
w, h = im.size
newim = Image.new("RGB", (w, h))
for i in range(w):
    for j in range(h):
        r, g, b = pix[i, j]  # pix[i,j]为tuple
        newim.putpixel((i, j), (r // 2, g // 2, b // 2))
newim.save('Q2.jpg', 'jpeg')
