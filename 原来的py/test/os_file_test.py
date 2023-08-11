import os
from pathlib import Path
import time
import arrow
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    # return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
    return time.strftime('%Y-%m-%d', timeStruct)


def get_FileCreateTime(filePath):
    # '''获取文件的创建时间'''
    # filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath):
    # '''获取文件的修改时间'''
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)


def get_FileAccessTime(filePath):
    # '''获取文件的访问时间'''
    # filePath = unicode(filePath, 'utf8')
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


def get_FileSize(filePath):
    # '''获取文件的大小,结果保留两位小数，单位为MB'''
    # filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)

p = Path(r"e:\\log")

t = arrow.now()
t1=t.format("YYYY-MM-DD")
print(t1)
for i in p.iterdir():
	if get_FileCreateTime(i)==t1:
		print(i.name)


