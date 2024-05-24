from  oswalk import walk
import os
import zipfile, os
import arrow
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
def backup_log():
	theday=str(arrow.now().year)+str(arrow.now().month)+str(arrow.now().day)
	z = zipfile.ZipFile("e:/log/备份日记%s.zip"%theday, 'w') # 注意这里的第二个参数是w，这里的filename是压缩包的名字
	path=r"C:\Users\11608\Desktop\Office 电子日记"
	if  os.path.exists(path):
		for root, dirs, files in os.walk(path, topdown=False):
			for name in files:
			# print(os.path.basename(name))
				filename=os.path.join(root, name)
				z.write(filename)
		for name in dirs:
			# print(os.path.join(root, name))
			# print(os.path.basename(name))
			filename=os.path.join(root, name)
			z.write(filename)
			pass
		z.close()
try:

	sched = BlockingScheduler()
	trigger = CronTrigger(hour='11', minute='50')
	sched.add_job(backup_log, trigger) #"cron 固定写法"
	sched.start()
except Exception as e:
	print("有一个错误的日记:",e)
finally:
	print("顺利备份")
	pass 
