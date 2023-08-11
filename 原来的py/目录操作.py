import os
def walk_dir(dir,fileinfo,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            print(os.path.join(name))
            fileinfo.write(os.path.join(root,name) + '\n')
        for name in dirs:
            print(os.path.join(name))
            fileinfo.write('  ' + os.path.join(root,name) + '\n')
dir =os.path.dirname(os.path.abspath(__file__))
#os.path.dirname 取目录 
#os.path.abspath 取所在文件路径
# print(os.path.abspath(__file__))
# print(dir)
fileinfo = open('list.txt','w')
walk_dir(dir,fileinfo)