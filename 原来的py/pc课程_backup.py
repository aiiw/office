import os
import requests,json
from urllib.parse import  quote,unquote
from urllib import request
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# 实例化一款浏览器
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  #不自动关闭浏览器
options.add_argument('--start-maximized')#浏览器窗口最大化
chrome_driver = r'C:\Users\11608\Desktop\chromedriver_win32\chromedriver.exe' 
mychrome = webdriver.Chrome(executable_path = chrome_driver,options=options)
# mychrome.implicitly_wait(100)　
mychrome.get("http://192.168.0.38:7089/default/desks/users.11608/@zopen.desks:index")
mychrome.add_cookie({'name':'session_key','value':'9ff0fc5c44c9c8263d37bc5bcd7b0eed'})
mychrome.get("http://192.168.0.38:7089/default/desks/users.11608/@zopen.desks:index")
menu=mychrome.find_element_by_xpath('//*[@id="site-navbar"]/li[2]')  #find_elements_by_xpath 是取列表,列表是没有单击的
menu.click()
item=mychrome.find_element_by_class_name('navTreeLevel0')
def click_elements(li):
    els = li.find_elements_by_css_selector(".fa.fa-angle-right.collapsed-icon")
    if els:
        for el in els:
            el.click()
            time.sleep(0.3)
            # print(el.text)
            # 对每个子元素递归调用 click_elements
            for child_li in li.find_elements_by_tag_name('li'):
                # print(child_li.get_attribute("outerHTML"))
                
                y = child_li.location['y']
                   # 打印元素位置和内容
                print(child_li.text,y)
                # mychrome.execute_script("window.scrollTo(0, arguments[0]);", y)
                child_li.click()
                time.sleep(2)
                try:
                    # tbodys = mychrome.find_element_by_tag_name("tbody")
                    bool = EC.presence_of_element_located((By.CSS_SELECTOR, ".listing.querySelectArea.batchAction.JColResizer.JCLRFlex"))
                    WebDriverWait(mychrome, 5).until(bool)
                    if bool:
                         table=mychrome.find_element(By.CSS_SELECTOR, ".listing.querySelectArea.batchAction.JColResizer.JCLRFlex")
                         # tbody=tbodys.find_element_by_tag_name("tbody")
                         # print("--------------------------",tbodys.get_attribute('outerHTML'),"------------------")
                         tbody=table.find_element_by_tag_name("tbody")
                except NoSuchElementException:
                    tbody = None
                if tbody:
                    # EC.presence_of_element_located((By.CSS_SELECTOR, "/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/span[5]"))
                    
                    for tr in tbody.find_elements_by_tag_name("tr"):
                        td=tr.find_element(By.XPATH, "./td[2]/div/a/span").text
                        print(td,":",tr.get_attribute("data-uid"))
                        # print(tr.get_attribute("outerHTML"))

                       
                click_elements(child_li)
        return # 退出递归
    else:
        return '1' # 递归结束时返回 '1'

# 遍历每个列表项，并对每个列表项调用 click_elements 函数
lis=item.find_elements_by_css_selector("li")
for li in lis:
    click_elements(li)


