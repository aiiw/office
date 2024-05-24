dic={}
dic['a']='a'

# dict =defaultdict( factory_function)
# 这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，
#比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，如下举例：

from collections import defaultdict

# dict2 = defaultdict(set)
# dict3 = defaultdict(str)
dict4 = defaultdict(list)

dict4["a"].append("aaa")
dict4['a'].append("abs")
dict4["a"].append("bbs")
dict4['b']="bbbb"
dict4['adsd'].append("dsafd")
dict4['随便'].append("随便写")
print(dict(dict4)) #这个解决了当时的问题,所以应该很好用吧
print(type(dict4))
print(type(dict(dict4)))
print("----------------------------------")


tdict4=dict(dict4)
print(tdict4.get('a'))
print(dict4)
print(dict4.items())
print(dict(dict4.items()),"这个就转换为字典了~~") #这个就转换为字典了~~
print(dict(dict4),"这个就转换为字典了~~") #这个就转换为字典了~~对比上面是一样的效果
print("----------------------------------")
#字典也是可以append的,首先定义了key的值为[]
dict1 = defaultdict(int)
dict1[2] ='two'
a = [11,22,33,44,55,66,77,88,99,90]
b ={
"key1" : [],
"key2" : []
}
for i in a:
    if i > 66:
        b["key1"].append(i)
    elif i < 66:
        b["key2"].append(i)
print(b)


print("------------tree-----------------")
from collections import defaultdict
def tree(): return defaultdict(tree)
d = tree()
d["person"]["name"]["first_name"] = 'raymon'
d["person"]["name"]["last_name"] = 'Gen'
d["person"]["age"] = 18
# for key,values in d.iteritems():
# 	print(key,'aa')
# print(d["person"][2][1])
# #[{"id":1,"text":"text1"},{"id":2,"text":"text2"},{"id":3,"text":"text3","selected":true},{"id":4,"text":"text4"},{"id":5,"text":"text5"}]

