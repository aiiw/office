import time
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),"----------------")
    return("aaa111")

sched.add_job(my_job, 'interval', seconds=5)
sched.start()

