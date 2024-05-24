import xmltodict
#json转xml函数
def jsontoxml(jsonstr):
    #xmltodict库的unparse()json转xml
    xmlstr = xmltodict.unparse(jsonstr)
    print(xmlstr)
    print("如上这个是json转xml")
if __name__ == "__main__":
    json = {'student': {'course': {'name': 'math', 'score': '90'},
                        'info': {'sex': 'male', 'name': 'name'}, 'stid': '10213'}}
    jsontoxml(json)
#parse 将xml解析为json
print("---------------------------------------------------------------------------------------------")
from pathlib import Path

path=Path('xx.xml')
aa=path.read_text()
print(aa) #直接打印出xml内容
xml_dict = xmltodict.parse(aa)   # 解析xml字符串
 
# print(type(xml_dict))  # <class 'collections.OrderedDict'>  类字典型，可以按照字典方法操作

xml_dict=dict(xml_dict)
import json

print("json.dumps",type(xml_dict))
# 遍历
aa=json.dumps(xml_dict,sort_keys=True,indent=5) #这个indent很强大,格式化代码,无论是打印输出,或者是输入到文件都是生效的
testjson=json.loads(aa)
#testjson.get('zabbix_export')['groups']['aaaa']='111222'# get获取值,如果字典值不存在则添加,存在:分1)值类似为字典,通过[添加键值对],其他类型则是修改的意思.
aa=json.dumps(testjson,sort_keys=True,indent=5,ensure_ascii=False)
print(aa)
wfp=Path("xml_to_json.json")
wfp.write_text(aa)
