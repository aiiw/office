#!/usr/bin/python3

import threading
import time

class myThread (threading.Thread):
    threadLock = threading.Lock()  #将锁给类属性
    def __init__(self, threadID, name, delay,count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.count=count
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        # myThread.threadLock.acquire()
        print_time(self.name, self.delay, self.count)
        # 释放锁，开启下一个线程
        # myThread.threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s:------------------%s" % (threadName, time.strftime("%Y-%m-%d %X", time.localtime() )))
        counter -= 1


threads = []

# 创建新线程
thread1 = myThread(1, "线程1", 2,5)
thread2 = myThread(2, "线程2", 2,5)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
# 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)

# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")
print("aa-------------------------------------------------------------------------------aa")