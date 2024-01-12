# python语言实现

# /Users/mac/test.py
import os
from pathlib import Path

fn=Path("cd.txt") #通过这个Path产生path对象
fn.write_text("aaa2\n") #这里我改了源码,正常添加内容会覆盖的,源码改为a+
fn1=Path(r'C:\Users\11608\Desktop\public\n1.txt')
fn1.write_text("abc")
cur_path=Path.cwd() #这个是获取当前路径
cur_path_parent=cur_path.parent #这个是很直观

#这个是拼接路径
join_path=Path.cwd()
vs=join_path.joinpath('aa','bb')
print(vs)
# #这个是创建目录
# cc=Path("123//123//123")
# cc.mkdir(mode=777,parents=1)

p = Path(r"d:\py")
print(type(p))
for i in p.iterdir():
  print(i)

print("aaaa",p.parts)  # 分割路径 类似os.path.split(), 不过返回元组

print(p.drive)  # 返回驱动器名称

print(p.root)  # 返回路径的根目录

print(p.anchor)  # 自动判断返回drive或root

print(p.parents)  # 返回所有上级目录的列表



gen1=p.glob('*.py') # 过滤目录(返回生成器))  rglob返回子文件夹的文件
for gen in gen1:
    print(gen)



q=Path("1.txt")          # pathlib 的open 写文件,应该是封装好了with
vv=q.open("a+")
vv.write("bbk")

with q.open('a+') as vv: #普通的写文件
    vv.write("aaaa")
if  not q.exists():      #判断文件是否存在
    q.rename('a5.txt')   #更改文件名


