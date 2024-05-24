import pytesseract
from PIL import Image
import PIL.ImageOps
# captcha = Image.open("１.jpg")
# result = pytesseract.image_to_string(captcha)
# print(result)   #6067

import pytesseract
from PIL import Image


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
def initTable(threshold=50):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

im = Image.open('1.png')
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
out.show()
# 先将图片转换为L模式

# 然后去噪

# 反转颜色

# 将重要部分裁剪放大

# 输出结果：