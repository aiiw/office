from urllib import request
import time
import random

def get_and_save_verify(i):
    try:
        url = 'http://192.168.0.181:8090/Common/GetValidateCode?length=4&id=validateCode1&299&Math.random()&Math.random()'
        request.urlretrieve(url,'HRM_' + str(i) + '.png')
        print('第' + str(i) + '张图片下载成功')
    except Exception:
        print('第' + str(i) + '张图片下载失败')
 
 
def get_proxy():
    # 使用代理步骤
    # - 1、设置代理地址
    proxys = [{'http': '39.137.69.10:8080'},
              {'http': '111.206.6.101:80'},
              {'http': '120.210.219.101:8080'},
              {'http': '111.206.6.101:80'},
              {'https': '120.237.156.43:8088'}]
    # - 2、创建ProxyHandler
    proxy = random.choice(proxys)
    proxy_handler = request.ProxyHandler(proxy)
    # - 3、创建Opener
    opener = request.build_opener(proxy_handler)
    # - 4、导入Opener
    request.install_opener(opener)
 
 
if __name__ == '__main__':
    for i in range(1, 1):
        # get_proxy()
        # time.sleep(random.randint(1, 4))
        get_and_save_verify(i)
import pytesseract
import cv2
import os
import numpy as np
path = 'D:/py/img/'
 
file_name = []
for k in os.walk(path):
	print(k)
	file_name = k[-1]
 
print('识别值' + '-----' + '真实值')
num = 0
for i in file_name:
    print(i)
    img = cv2.imdecode(np.fromfile(path + i, dtype=np.uint8), 1)
    print(img)
    a = pytesseract.image_to_string(img)
    true_value = i[-8:-4]
    print(i)
    print(true_value)
    print(a + '-----' + true_value)
    if a == true_value:
     num += 1
 
print('识别的准确率为：' + str(num/100))
