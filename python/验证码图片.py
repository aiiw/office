# https://www.cnblogs.com/goodshipeng/p/7997682.html
from PIL import Image
from PIL import ImageDraw
img = Image.new(mode="RGB", size=(120, 30), color=(255,255,255))
draw = ImageDraw.Draw(img, mode="RGB")
# 第一个参数：表示起始坐标
# 第二个参数：表示写入内容
# 第三个参数：表示颜色
draw.text([20, 10], "python", fill="red")
with open("code.png",'wb') as f:
 img.save(f,format="png")
# 从 Pillow 中导入图片处理模块 Image    
from PIL import Image    
# 导入基于 Tesseract 的文字识别模块 pytesseract    
import pytesseract
"""    
@pytesseract：https://github.com/madmaze/pytesseract    
"""    
 
    
# 打开图片    
im = Image.open("code.png")
# 识别图片内容    
text = pytesseract.image_to_string(im)
# print(text)