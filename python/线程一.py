#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''threading test'''
import threading
import queue
from time import sleep
#之所以为什么要用线程，因为线程可以start后继续执行后面的主线程，可以put数据，如果不是线程直接在get阻塞。
class Mythread(threading.Thread):
 def __init__(self,que):
  threading.Thread.__init__(self)
  self.queue = que
 def run(self):
  while True:
   sleep(1)
   if self.queue.empty(): #判断放到get前面，这样可以，否则队列最后一个取完后就空了，直接break，走不到print
      break
   item = self.queue.get()
   print('self.queue.get',item)
   self.queue.task_done()
  return
que = queue.Queue()
tasks = [Mythread(que) for x in range(1)]

for i in range(10):

 que.put(i) #快速生产
for x in tasks:
 print(x)
 t = Mythread(que) #把同一个队列传入2个线程
 t.start()

que.join()

print('---success---')#!/usr/bin/env python
