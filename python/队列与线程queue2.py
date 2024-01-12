import queue
import time,threading
q=queue.Queue(maxsize=0)
 
def product(name):
    count=1
    while True:
        print('\n')
        q.put('气球兵{}'.format(count))
        print ('{}生产气球兵{}只'.format(name,count))
        count+=1
        time.sleep(3)
def consume(name):
    while True:
        print ('{}使用了{}'.format(name,q.get()))
        time.sleep(1)
        q.task_done()
t1=threading.Thread(target=product,args=('aiiw',))
t2=threading.Thread(target=consume,args=('p1',))
t3=threading.Thread(target=consume,args=('p2',))
 
t1.start()
t2.start()
t3.start()
