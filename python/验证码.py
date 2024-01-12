import pytesseract
from PIL import Image
import PIL.ImageOps
import os
import requests,json
from urllib.parse import  quote,unquote
import connector
import time
from urllib import request


def convert_img(img, threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img


# captcha = Image.open("2.png")
# captcha = convert_img(captcha, 120)
# captcha.show()
# captcha.save("threshold.jpg")
# result = pytesseract.image_to_string(captcha)
# print(result)  #3n3D
def initTable(threshold=60):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table
path=r'img'
for root,dir,file in os.walk(path):
	for tt in  file:
		dd=os.path.join(os.path.abspath(root),tt)
		im = Image.open(dd)
#图片的处理过程
		im = im.convert('L')
		binaryImage = im.point(initTable(), '1')
		im1 = binaryImage.convert('L')
		im2 = PIL.ImageOps.invert(im1)
		im3 = im2.convert('1')
		im4 = im3.convert('L')
		#将图片中字符裁剪保留
		box = (3,2,46,20) 
		region = im4.crop(box)  
		#将图片字符放大
		out = region.resize((120,55)) 
		print (pytesseract.image_to_string(out))
		
		# 先将图片转换为L模式

		# 然后去噪

		# 反转颜色

		# 将重要部分裁剪放大

		# 输出结果：

		# 先将图片转换为L模式

		# 然后去噪

		# 反转颜色

		# 将重要部分裁剪放大

		# 输出结果：