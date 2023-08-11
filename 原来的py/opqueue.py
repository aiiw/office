import queue
import time
q = queue.Queue(13)  # 调用构造函数，初始化一个大小为3的队列
# print(q.empty())  # 判断队列是否为空，也就是队列中是否有数据
#  入队，在队列尾增加数据， block参数，可以是True和False 意思是如果队列已经满了则阻塞在这里，
# timeout 参数 是指超时时间，如果被阻塞了那最多阻塞的时间，如果时间超过了则报错。
q.put_nowait(1)
q.get_nowait()
q.task_done()
q.join()
for a in range(1,10):
	q.put(a, block=True, timeout=5)#入队，在队列尾增加数据， block参数，可以是True和False 意思是如果队列已经满了则阻塞在这里，
	print (q.queue,time.ctime())
	print(q.full())  # 判断队列是否满了，这里我们队列初始化的大小为3
	print(q.qsize())  # 获取队列当前数据的个数
#  block参数的功能是 如果这个队列为空则阻塞，
#  timeout和上面一样，如果阻塞超过了这个时间就报错，如果想一只等待这就传递None
print("------------------")
print(q.get(block=True, timeout=None))
print(q.qsize())  # 获取队列当前数据的个数

# #  queue模块还提供了两个二次封装了的函数，
# q.put_nowait(23)  # 相当于q.put(23, block=False)
# print(q.get_nowait())  # 相当于q.get(block=False)
#!/usr/bin/python3

# import queue
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)

# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1

# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1

# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()

# # 等待队列清空
# while not workQueue.empty():
#     pass

# # 通知线程是时候退出
# exitFlag = 1

# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")