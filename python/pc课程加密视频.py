from selenium import webdriver
import time
# 实现无可视化界面的操作
from selenium.webdriver.chrome.options import Options
from urllib import request
import requests
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
from bs4 import BeautifulSoup
import re
# 实例化一款浏览器
from selenium import webdriver
# chrome_driver=r'C:\Users\11608\Desktop\桌面\chromedriver_win32\chromedriver.exe'
#mychrome = webdriver.Chrome(options=chrome_options)  不显示窗口
chrome_driver = r'C:\Users\11608\Desktop\chromedriver_win32\chromedriver.exe' 
mychrome = webdriver.Chrome(executable_path = chrome_driver)
# mychrome = webdriver.Chrome() 
# 添加Cookie
mychrome.get("https://www.mzyun.ren/")
mychrome.add_cookie({'name':'connect.sid','value':'s:jSCYyrvq0iNfj4zjYzX3dYCuZz-f7hbE.RzSSheWzrUnLrptwx6nxvPP4cVOFJUen8g+JamImkgs'})
mychrome.get("https://www.mzyun.ren/companyCourse/list?mode=image&category1=a2d26f50-ed1c-11ec-986f-a9686702b0a1&category2=a9f27870-ed1c-11ec-8c78-8761508d236f")
#方式1
# categories = mychrome.find_elements_by_xpath('//*[@id="courseList"]/div[2]/div/*')
# # categories = mychrome.find_elements_by_xpath("//a[contains(@href,'companyCourse')]" )
# print(len(categories))

from Crypto.Cipher import AES

def m3u8(file_path,url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    # requests得到m3u8文件内容
    content = requests.get(url,headers=header).text
    if "#EXTM3U" not in content:
        print("这不是一个m3u8的视频链接！")
        return False
    if "EXT-X-KEY" not in content:
        print("没有加密")
        return False


    # 使用re正则得到key和视频地址
    jiami=re.findall('#EXT-X-KEY:(.*)\n',content)
    key=re.findall('URI="(.*)"',jiami[0])
    print(key)
    #得到每一个ts视频链接
    tslist=re.findall('EXTINF:(.*),\n(.*)\n#',content)
    newlist=[]
    for i in tslist:
        newlist.append(i[1])

    
    # 先获取URL/后的后缀，再替换为空  
    urlkey=url.split('/')[-1]
    url2 = url.replace(urlkey, '')  #这里为得到url地址的前面部分，为后面key的链接和视频链接拼接使用

    #得到key的链接并请求得到加密的key值
    keyurl=url2+key[0]
    print(keyurl)
    keycontent= requests.get(keyurl,headers=header).text

    #得到每一个完整视频的链接地址
    tslisturl=[]
    for i in newlist:
        tsurl=url2+i
        tslisturl.append(tsurl)

    #得到解密方法，这里要导入第三方库  pycrypto
    #这里有一个问题，安装pycrypto成功后，导入from Crypto.Cipher import AES报错
    #找到使用python环境的文件夹，在Lib文件夹下有一个 site-packages 文件夹，里面是我们环境安装的包。
    #找到一个crypto文件夹，打开可以看到 Cipher文件夹，此时我们将 crypto文件夹改为 Crypto 即可使用了
    cryptor = AES.new("mzyunnnyifengke&".encode("utf-8"), AES.MODE_CBC)

    #for循环获取视频文件
    for i in tslisturl:
        res = requests.get(i, header)
        #使用解密方法解密得到的视频文件
        cont=cryptor.decrypt(res.content)
        #以追加的形式保存为mp4文件
        with open(file_path, 'ab+') as f:
            f.write(cont)
    return True

#
def downpdf(url,file_path):

    
    ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    header  =  {"User-Agent"  : ua,
            "Cookie":r"connect.sid=s:jSCYyrvq0iNfj4zjYzX3dYCuZz-f7hbE.RzSSheWzrUnLrptwx6nxvPP4cVOFJUen8g+JamImkgs"
            }

    file = requests.get(url, headers=header)
    soup = BeautifulSoup(file.content, 'html.parser')
    print(soup.iframe.attrs['src'])
    url1=soup.iframe.attrs['src']
    # url1='https://upload.mzyun.ren/pdf/web/viewer.html?file=https://public.mzyun.ren/ppd/2923be60-146a-11ec-9d0b-bfdb0beb590a.pdf'
    url2=url1.split('=')
    file1 = requests.get(url2[-1], headers=header)
    with open(file_path, 'wb') as f:
        f.write(file1.content)
    print('PDF成功下载')
    time.sleep(10)
# for item in categories:
#     inst=item.find_elements_by_xpath('./following::*') #这个查当前元素下的所有子元素(包括下级)
#     for a in inst:
#         print(a.text)
# #
list=[]

links=mychrome.find_elements_by_xpath('//*[@id="courseList"]/div[2]/div/*')
print(len(links))
for link in links:
    # print(link.find_element_by_tag_name('a').get_attribute('href'))
    list.append(link.find_element_by_tag_name('a').get_attribute('href'))

path='//*[@id="mBody"]/span'

for i in range(2,len(list)):
    mychrome.get(list[i])
    mychrome.find_element_by_xpath(path).click()

    path1='''//h4[contains(@class,'uppercase chapterCont') and contains(@style,'margin-top: 0')]/a[contains(@href,'zce')]'''
    courses=mychrome.find_elements_by_xpath(path1)
    for course in courses:
        print(len(courses))
        print(course.get_attribute('href'))
        url=course.get_attribute('href')


        ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        header  =  {"User-Agent"  : ua,
                "Cookie":r"connect.sid=s:jSCYyrvq0iNfj4zjYzX3dYCuZz-f7hbE.RzSSheWzrUnLrptwx6nxvPP4cVOFJUen8g+JamImkgs"
                }

        file = requests.get(url, headers=header)
        soup = BeautifulSoup(file.content, 'html.parser')
        print(soup.iframe.attrs['id'])
        flag=soup.iframe.attrs['id']
        if  soup.iframe.attrs['id']!='ifm_m3u8':
            path_file=course.get_attribute('title')+".pdf"
            downpdf(url,path_file)
        else:
            path_file=course.get_attribute('title')+".mp4"
            key=url.split("=")[-3][0:-5]
            vurl='https://m3u8.mzyun.ren/{}/{}.m3u8'.format(key,key)
            m3u8(path_file,vurl)
            print(vurl)
        # print(course.find_element_by_tag_name('a').get_attribute('href'))
        # print(course.find_element_by_tag_name('a').get_attribute('title'))


    # path2='//*[contains(@src,'pdf')]' #这个是找当前页面中的pdf文件
    # //a[contains(@href,'/companyCourse/view')] 这个是使用标签的属性包括值
    # [contains(@class,'chapterInfoContent')]
    #//*[@id="courseChapter"]/div[1]/div/ul/following::* [contains(@class,'chapterInfoContent')]
    #//*[@id="courseChapter"]/div[1]/div/ul/li/div/div/ul/li/div[3]/div[2]/h4

    # <iframe width="100%" height="680" id="pdfLoader" src="https://upload.mzyun.ren/pdf/web/viewer.html?file=https://public.mzyun.ren/ppd/2923be60-146a-11ec-9d0b-bfdb0beb590a.pdf" frameborder="0" style="height: 499px;"></iframe>
    # for item in categories:
    #     # print(category.text)
    #
    #     vv=item.find_elements_by_xpath(".//*" ) # 这个是查找当前下的所有子元素
    #     vv = item.find_elements_by_xpath(".//*")  # 这个是查找当前下的所有子元素
    #     for v in vv:
    #
    #         if v.find_element_by_xpath("a[contains(@href,'companyCourse/view')]" ):
    #
    #             print(v.get_attribute('href'))
    #
    #
    #     # time.sleep(1)


