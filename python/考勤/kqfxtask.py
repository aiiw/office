import time,os
import kqfx
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger



try:
	# def my_job():
	# 		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),"----------------")
	# 		if not os.path.exists("d:\\log"):
	# 			os.mkdir("d:\\log")
	# 		files=open(r'd:\\log\\f2.txt','a+')
	# 		print(time.localtime(),'main begin',file=files)
	# 		files.close()

	if not os.path.exists("d:\\log"):
		os.mkdir("d:\\log")
	files=open(r'd:\\log\\f2.txt','a+')
	print(time.localtime(),'main begin',file=files)
	files.close()

	sched = BlockingScheduler()
	trigger = CronTrigger(hour='15', minute='50')
	sched.add_job(kqfx.callkqtask, trigger) #"cron 固定写法"
	# sched.add_job(my_job, trigger) #"cron 固定写法"
	sched.start()
except Exception as e:
	print(e)
finally:
	pass 







# # BlockingScheduler
# scheduler = BlockingScheduler()
# scheduler.add_job(job, "cron"， day_of_week="1-5", hour=6, minute=30)
# schduler.start()
 
 
# scheduler.add_job(job, 'cron', hour=1, minute=5)
# hour =19 , minute =23  这里表示每天的19：23 分执行任务
# hour ='19', minute ='23'  这里可以填写数字，也可以填写字符串
# hour ='19-21', minute= '23'  表示 19:23、 20:23、 21:23 各执行一次任务
 
# #每300秒执行一次
# scheduler .add_job(job, 'interval', seconds=300)
 
# #在1月,3月,5月,7-9月，每天的下午2点，每一分钟执行一次任务
# scheduler .add_job(func=job, trigger='cron', month='1,3,5,7-9', day='*', hour='14', minute='*')
 
# # 当前任务会在 6、7、8、11、12 月的第三个周五的 0、1、2、3 点执行
# scheduler .add_job(job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
 
# #从开始时间到结束时间，每隔俩小时运行一次
# scheduler .add_job(job, 'interval', hours=2, start_date='2018-01-10 09:30:00', end_date='2018-06-15 11:00:00')
 
# #自制定时器