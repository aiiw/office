from browsermobproxy import Server
import time,sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from urllib.parse import  quote,unquote

# 启动代理
server = Server(r'browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()
print('proxy', proxy.proxy)
 
 
# 启动浏览器
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
mychrome = webdriver.Chrome(options=chrome_options)

 
# 监听结果
base_url = 'https://www.amp360.net/inHtml/MusicPlayer/index.html'
proxy.new_har(options={
    'captureContent': True,
    'captureHeaders': True
})
mychrome.get(base_url)
time.sleep(3)

mychrome.find_element_by_xpath('//*[@id="btn-area"]/span[4]').click()
# 
time.sleep(1)
mychrome.find_element_by_xpath('//*[@id="search-wd"]').send_keys('王杰')
time.sleep(1)
mychrome.find_element_by_xpath('//*[@id="search-area"]/div[1]/button').click()
time.sleep(1)
# fetch=r'''fetch("https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=1F0E9EAA85560342&ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=222&rsv_spt=1&oq=Unicode%2526gt%253Bncode%2526gt%253Brror%253A%2520%2526%252339%253Bgbk%2526%252339%253B%2520codec%2520can%2526%252339%253Bt%2520encode%2520character&rsv_pq=81a2ed660001a080&rsv_t=46b5o3koP1mW26sKgNtmSZu1dVkdj95bdzE6DEp9aGZSwo6Nvi2U1WP6oOcTCH551QxA&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_sug3=7&rsv_sug1=3&rsv_sug7=100&rsv_btype=t&prefixsug=222&rsp=8&inputT=4613&rsv_sug4=11985&bs=UnicodeEncodeError%3A%20%27gbk%27%20codec%20can%27t%20encode%20character&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=3&_cr1=49202", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "en-US,en;q=0.9,zh;q=0.8,zh-CN;q=0.7",
#     "is_referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=UnicodeEncodeError%3A%20%27gbk%27%20codec%20can%27t%20encode%20character&rsv_spt=1&oq=UnicodeEncodeError%3A%20%27gbk%27%20codec%20can%27t%20encode%20character&rsv_pq=81a2ed660001a080&rsv_t=815bx%2F1N36WuohWEXJP%2FSWBhsuSdTwp3cAUWUb%2FwO7tZ%2F25Pd4%2BcZKBFxBPCsbD4dxNd&rqlang=cn",
#     "is_xhr": "1",
#     "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "x-requested-with": "XMLHttpRequest"
#   },
#   "referrer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=222&rsv_spt=1&oq=Unicode%2526gt%253Bncode%2526gt%253Brror%253A%2520%2526%252339%253Bgbk%2526%252339%253B%2520codec%2520can%2526%252339%253Bt%2520encode%2520character&rsv_pq=81a2ed660001a080&rsv_t=46b5o3koP1mW26sKgNtmSZu1dVkdj95bdzE6DEp9aGZSwo6Nvi2U1WP6oOcTCH551QxA&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_sug3=7&rsv_sug1=3&rsv_sug7=100&rsv_btype=t&prefixsug=222&rsp=8&inputT=4613&rsv_sug4=11985",
#   "referrerPolicy": "unsafe-url",
#   "body": null,
#   "method": "GET",
#   "mode": "cors",
#   "credentials": "include"
# });'''
# resp = mychrome.execute_script(fetch)
# print(resp)

# # 读取结果
result = proxy.har
# result = json.dumps(proxy.har, ensure_ascii=False)
# har_data = json.dumps(proxy.har)
# save_har = open("req.har", 'a',encoding='utf-8')
# save_har.write(result)
# save_har.close()
print(type(result['log']['entries']))
i=0
j=0
for entry in result['log']['entries']:#这是一个list
    i=i+1

    flag=json.dumps(entry['response'].get('content').get('text'))
    if len(flag) > 10:
        print(type(entry['response'].get('content')))
        str=entry['response'].get('content').get('text')
        str1 = str.encode('utf-8')
        print(str1)
        #如下代码在sublime报错,在pycharm正常
        print(str1.decode('unicode-escape'))
        print("===================================")
        str1 = json.dumps(entry['response'],sort_keys=True,indent=5,ensure_ascii=False)
        print(str1)


# 	# print(len(entry))
# 	# temp=str(entry['response'])
# 	# temp1=temp.encode('utf-8')
# 	# temp2=temp1.decode('utf-8',"ignore")
# 	# temp3=unquote(temp2)
# 	# # temp3=json.loads(temp2)
# 	# # temp5=json.dumps(temp2,sort_keys=True,indent=5,ensure_ascii=False)
# 	# print(temp3)

	# har_data = json.dumps(entry['response'], sort_keys=True,indent=5,ensure_ascii=False)
	# har_file = open("req1.har", 'a',encoding='utf-8')
	# har_file.write(har_data)
	# har_file.close()



	# temp=str(entry['response'])
	# temp1=temp.encode('gbk',"ignore")
	# temp2=temp1.decode('gbk',"ignore")
	# temp3=json.loads(temp2)
	# temp4=(json.dumps(temp3, sort_keys=True,indent=5,ensure_ascii=False))
	# print(temp4)


    # print(json.dumps(entry['response'], sort_keys=True,indent=5,ensure_ascii=False))
    # # print(entry['request']['url'])
    # # temp=json.dumps(entry['response'], sort_keys=True,indent=5,ensure_ascii=False)
    # # print(temp)
    # print(type(entry['response']))


        CREATE OR REPLACE FUNCTION getkpidept(op varchar2) RETURN varchar2 as
  rz varchar(2000);
begin
  if op = 'WMS01' or op = 'WMS05' or op = 'WMS41' then
    rz := '钢一部';
  
  elsif op = 'AKS01' or op = 'AKS05' then
    rz := '欧德罗';
  elsif op = 'WLS01' or op = 'WLS05' then
    rz := '铝部';
  elsif op = 'WLS41' or op='WLS47' then
    rz := '铝智造';
  elsif op = 'DDS01' or op = 'DDS11' then
    rz := '电器';
  elsif op = 'HDS01' or op = 'HDS05' then
    rz := '嘉事泰';
  elsif op = 'RDS01' or op = 'RDS05' then
    rz := '精铸钢';
  end if;

  return rz;

end;
