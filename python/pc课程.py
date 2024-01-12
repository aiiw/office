import os
import requests,json
from urllib.parse import  quote,unquote
from urllib import request
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# 实例化一款浏览器
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import warnings
import sys
import io
from selenium.common.exceptions import ElementClickInterceptedException
# Set the stdout encoding to UTF-8
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 将 DeprecationWarning 设置为 "忽略"
warnings.filterwarnings("ignore", category=DeprecationWarning)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  #不自动关闭浏览器
options.add_argument('--start-maximized')#浏览器窗口最大化
chrome_driver = r'C:\Users\11608\Desktop\chromedriver_win32\chromedriver.exe' 
mychrome = webdriver.Chrome(executable_path = chrome_driver,options=options)
# mychrome.implicitly_wait(100)　
mychrome.get("http://192.168.0.38:7089/default/desks/users.11608/@zopen.desks:index")
mychrome.add_cookie({'name':'session_key','value':'1fc0ac1d2a94f8fd431e4cd46fd46f2a'})
mychrome.get("http://192.168.0.38:7089/default/desks/users.11608/@zopen.desks:index")
menu=mychrome.find_element_by_xpath('//*[@id="site-navbar"]/li[2]')  #find_elements_by_xpath 是取列表,列表是没有单击的
menu.click()
item=mychrome.find_element_by_class_name('navTreeLevel0')
from mysqlclass import Database
db = Database(
    host="192.168.0.7",
    user="root",
    port="3306",
    passwd="123456",
    database="dj3"
)

# # 新增数据
# fields = ['name', 'age']
# values = ('John', 30)
# last_id = db.insert('some_table', fields, values)
# print(last_id)


def click_elements(li):
    #1:els就是列表中带有扩展图标的列表,如果找到就点击一下加载子列表,一般一级菜单就是带有这个扩展图标,所以一运行就加载二级菜单
    # print("一级菜单:",li.text) 一级
    els = li.find_elements_by_css_selector(".fa.fa-angle-right.collapsed-icon")
    if els:
        #如下的el=li
        for el in els:
            search_terms = ['待审文件']
            if any(item in li.text for item in search_terms):
                break
            try:
                el.click()
            except ElementClickInterceptedException:
                mychrome.refresh()
                el.click()
            # target_element =el
            # mychrome.execute_script("arguments[0].scrollIntoView();", target_element)
            # # 向上移动100个像素
            # actions = ActionChains(mychrome)
            # actions.move_to_element_with_offset(target_element, 0, -100).perform()
            # target_element = el.find_element_by_xpath('//*[@id="left"]/div')  # 获取父元素
            mychrome.execute_script("arguments[0].scrollIntoViewIfNeeded();", el)
            time.sleep(1)
            # print(el.text)
            # 2:二级菜单是一个li列表.对每个子元素递归调用 click_elements
            for child_li in li.find_elements_by_tag_name('li'):
                # print(child_li.get_attribute("outerHTML"))
                #测试,获取元素的坐标
                y = child_li.location['y']
                   # 打印元素位置和内容
               
                # try:
                #     # print(child_li.text,y)  二级
                #     pass
                # except UnicodeEncodeError as e:
                #     print("utf-8")
                # mychrome.execute_script("window.scrollTo(0, arguments[0]);", y)
                # target_element = el.find_element_by_xpath('//*[@id="left"]/div')  # 获取父元素
                mychrome.execute_script("arguments[0].scrollIntoViewIfNeeded();", child_li)
                # actions = ActionChains(mychrome)
                # actions.move_to_element(child_li).perform()
                if child_li:
                    try:
                        child_li.click()
                    except ElementClickInterceptedException:
                        mychrome.refresh()
                        # child_li.click()
                        actions = ActionChains(mychrome)
                        actions.move_to_element(child_li).click().perform()
                    time.sleep(1.5) #这个时间很关键
                else:
                    print("这个应该不会执行的,没有child_li")
                try:
                    # tbodys = mychrome.find_element_by_tag_name("tbody")
                    #3 如下是获取一个table>这个table有tbody,tbody下有tr
                    bool = EC.presence_of_element_located((By.CSS_SELECTOR, ".listing.querySelectArea.batchAction.JColResizer.JCLRFlex"))
                    WebDriverWait(mychrome, 1).until(bool)
                    
                    table=mychrome.find_element(By.CSS_SELECTOR, ".listing.querySelectArea.batchAction.JColResizer.JCLRFlex")
                         # tbody=tbodys.find_element_by_tag_name("tbody")
                         # print("--------------------------",tbodys.get_attribute('outerHTML'),"------------------")
                    tbody=table.find_element_by_tag_name("tbody")
                except TimeoutException:
                    print("元素不存在或加载过程超时")
                    tbody = None
                if tbody:
                    try:
                        # 4 等待下一页按钮出现
                        # next_button = WebDriverWait(mychrome, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/div/div[3]/div/div/div/div[1]/div[2]/div[2]/span[5]/a")))
                        next_button = WebDriverWait(mychrome, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".next")))
                        n=0
                        if next_button:
                            while True:
                                n=n+1
                                values=()
                                page=str(n)
                                print("找到了next,开始展开:可以有%s页"%(page))
                                try:
                            # 5查找表格元素
                                    table = mychrome.find_element(By.CSS_SELECTOR, ".listing.querySelectArea.batchAction.JColResizer.JCLRFlex")
                                    next_button = WebDriverWait(mychrome, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".next")))
                                    #next_button = WebDriverWait(mychrome, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/div/div[3]/div/div/div/div[1]/div[2]/div[2]/span[5]/a")))
                                # except NoSuchElementException:

                                #     #搞错了,没有如下这个的,当发现有下一页是,
                                #     # print("最后一页是没有next按钮的,所以要终止循环,在终止前也要展开最后一页.")
                                #     # tbody = table.find_element_by_tag_name("tbody")
                                #     # for tr in tbody.find_elements_by_tag_name("tr"):
                                #     #     td=tr.find_element(By.XPATH, "./td[2]/div/a/span").text
                                #     #     print(td,":",tr.get_attribute("data-uid"))
                                #     break
                                except TimeoutException:
                                        print("没有找到下一面这个按钮了,这是最后一页了")
                                        time.sleep(1)
                                        tbody = table.find_element_by_tag_name("tbody")
                                        for tr in tbody.find_elements_by_tag_name("tr"):
                                            td=tr.find_element(By.XPATH, "./td[2]/div/a/span").text
                                            try:
                                                # print(td,":",tr.get_attribute("data-uid"))
                                                fields = ['name', 'code']
                                                values=(td,tr.get_attribute("data-uid"))
                                                last_id = db.insert('wk', fields, values)
                                                print(last_id)
                                            except UnicodeEncodeError as e:
                                                print("utf-8")
                                        break
                
                             # 6遍历表格，输出每行的内容
                                tbody = table.find_element_by_tag_name("tbody")
                                for tr in tbody.find_elements_by_tag_name("tr"):
                                    td=tr.find_element(By.XPATH, "./td[2]/div/a/span").text
                                    try:
                                        # print(td,":",tr.get_attribute("data-uid"))
                                        fields = ['name', 'code']
                                        values=(td,tr.get_attribute("data-uid"))
                                        last_id = db.insert('wk', fields, values)
                                        print(last_id)
                                    except UnicodeEncodeError as e:
                                        print("utf-8")
                                # Handle the exception here
                                next_button.click()
                                time.sleep(1)
                        else:
                            print("正常这里是不会执行的,因为如果不存在next_button的话,直接就抛出异常了.")
                         # 没有下一页按钮，直接遍历表格


                    except Exception as e:
                        # 点击child_li时,如果只有一页,则打印这一页
                            print("没有找到了next:点击child_li时,如果只有一页,则打印这一页")
                            table = mychrome.find_element(By.CSS_SELECTOR, ".listing.querySelectArea.batchAction.JColResizer.JCLRFlex")
                            tbody = table.find_element_by_tag_name("tbody")
                            for tr in tbody.find_elements_by_tag_name("tr"):
                                td = tr.find_element(By.XPATH, "./td[2]/div/a/span").text
                                try:
                                    fields = ['name', 'code']
                                    values=(td,tr.get_attribute("data-uid"))
                                    last_id = db.insert('wk', fields, values)
                                    print(last_id)
                                except UnicodeEncodeError as e:
                                    print("utf-8")
                                # Handle the exception here



                       
                click_elements(child_li)
        return # 退出递归
    else:
        return '1' # 递归结束时返回 '1'

# 遍历每个列表项，并对每个列表项调用 click_elements 函数
lis=item.find_elements_by_css_selector("li")
for li in lis:
    click_elements(li)


