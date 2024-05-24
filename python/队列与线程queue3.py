import queue
import time,threading
q=queue.Queue(maxsize=0)
 
def product(name):
    count=1
    while True:
        print('-------------',str(time.ctime())[14:19],'----------------------')
        q.put('气球兵{}'.format(count))
        # print ('{}训练气球兵{}只'.format(name,count))
        count+=1
        time.sleep(80)

def consume(name):
    count2=0
    while True:
        count2+=1
        print('计算器',str(count2))
        print ('start',str(time.ctime())[14:19])
        print('{}使用了{}'.format(name,q.get()))
        print('end',str(time.ctime())[14:19])
       
        
t1=threading.Thread(target=product,args=('aiiw',))
t2=threading.Thread(target=consume,args=('p1',))
t3=threading.Thread(target=consume,args=('p2',))
 
t1.start()
t2.start()
t3.start()
