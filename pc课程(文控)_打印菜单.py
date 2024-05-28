from mysqlclass import Database
import os
import requests
import json
from urllib.parse import quote, unquote
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
from datetime import datetime
# Set the stdout encoding to UTF-8
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 将 DeprecationWarning 设置为 "忽略"
warnings.filterwarnings("ignore", category=DeprecationWarning)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # 不自动关闭浏览器
# options.add_argument('--start-maximized')#浏览器窗口最大化
# options.add_argument('--headless')#这个是后来隐藏的窗口 但是需要加上窗口的大小
options.add_argument('--window-size=1920,1080')  # 设置窗口大小为 1920x1080

chrome_driver = r'C:\Users\11608\Desktop\chromedriver-win32\chromedriver.exe'
mychrome = webdriver.Chrome(executable_path=chrome_driver, options=options)
mychrome.implicitly_wait(1)
# mychrome.implicitly_wait(100)　
mychrome.get(
    "http://www.kaster.cn:7089/default/desks/users.admin/@zopen.desks:index")
mychrome.add_cookie(
    {'name': 'session_key', 'value': 'b0c869d6761bbfc2d5e61c3505144fa9'})
mychrome.get(
    "http://www.kaster.cn:7089/default/desks/users.admin/@zopen.desks:index")
# find_elements_by_xpath 是取列表,列表是没有单击的
menu = mychrome.find_element_by_xpath('//*[@id="site-navbar"]/li[2]')
menu.click()
navTreeLevel0 = mychrome.find_element_by_class_name('navTreeLevel0')  # 按class_name
def click_elements(li):
    # 1:els就是列表中带有扩展图标的列表,如果找到就点击一下加载子列表,一般一级菜单就是带有这个扩展图标,所以一运行就加载二级菜单
    # print("一级菜单:",li.text) 一级
    els = li.find_elements_by_css_selector(".loadTree.fa.fa-angle-right.collapsed-icon")
    if els:
        # 如下的el=li
        for el in els:
            try:
                el.click()  # el是批带有下级菜单图标图标图标图标图标图标图标图标图标图标图标图标图标
            except ElementClickInterceptedException:#通常是由于某些元素遮挡了目标元素而导致无法点击的异常。这可能是因为页面上有其他元素位于目标元素之上，或者目标元素处于不可见状态
                print("通常是由于某些元素遮挡了目标元素而导致无法点击的异常。这可能是因为页面上有其他元素位于目标元素之上，或者目标元素处于不可见状态")
                print("异常的一级菜单",li.text)
            time.sleep(1)
            print("一级菜单",li.text)
            # 2:二级菜单是一个li列表.对每个子元素递归调用 click_elements
            for child_li in li.find_elements_by_tag_name('li'):  # 获取下级子菜单
                print("子菜单",child_li.text)
                child_li.click()
                click_elements(child_li)
          # 退出递归 这种情况下，函数会立即结束并返回 None
    else:
        print("这里递归返回1")
        return '1'  # 递归结束时返回 '1'


# 遍历每个列表项，并对每个列表项调用 click_elements 函数
navTreeItems = navTreeLevel0.find_elements_by_tag_name("li")
for li in navTreeItems:
    click_elements(li)

# li =>1.0管理手册 2.0程序文件........
