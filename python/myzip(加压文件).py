import zipfile, os

z = zipfile.ZipFile(filename, 'w') # 注意这里的第二个参数是w，这里的filename是压缩包的名字

#假设要把一个叫testdir中的文件全部添加到压缩包里（这里只添加一级子目录中的文件）：
if os.path.isdir(testdir):
    for d in os.listdir(testdir):
        z.write(testdir+os.sep+d)
# close() 是必须调用的！
z.close()