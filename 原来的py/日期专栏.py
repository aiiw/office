
########################################## arrow #################################################################
from datetime import datetime, timedelta

now = datetime.now()

# 明天的日期
tomorrow = now + timedelta(days=1)

# 两小时之后的时间
two_hours_later = now + timedelta(hours=2)

# 一周零两天后的日期
one_week_two_days_later = now + timedelta(weeks=1, days=2)

# 创建Arrow对象：

# arrow.now()：获取当前时间的Arrow对象。
# arrow.get('2019-01-01')：根据给定字符串创建Arrow对象。
# arrow.utcnow()：获取当前的UTC时间的Arrow对象。
# Arrow对象的属性：

# year、month、day、hour、minute、second：返回Arrow对象的年、月、日、时、分、秒。
# tzinfo：返回Arrow对象的时区信息。
# 格式化输出：

# format()：将Arrow对象转换为指定格式的字符串。例如，arrow.now().format('YYYY-MM-DD HH:mm:ss')。
# 时间操作：

# shift()：对Arrow对象进行时间偏移。例如，arrow.now().shift(hours=-2)表示将当前时间向前移动2小时。
# replace()：对Arrow对象的特定部分进行替换。例如，arrow.now().replace(day=1)表示将当前日期的日替换为1号。
# 时间比较：

# 、<、==、!=：对Arrow对象进行时间大小的比较。

# 时间戳的转换：

# timestamp()：将Arrow对象转换为UNIX时间戳。
# fromtimestamp()：根据UNIX时间戳创建Arrow对象。
# 这些只是arrow库中的一些常用方法，详细的使用方法可以参考官方文档或使用dir()函数来查看arrow对象的可用方法。


import arrow
from  datetime import timedelta #([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
a=timedelta(days=1,minutes=12)
b=arrow.now()
print("timedelta(days=1,minutes=12)",a)
print("arrow.now()",b)
d=arrow.now().format('YYYY-MM-DD HH:MM:SS')#错误
d1=arrow.now().format("YYYY-MM-DD:HH:mm:ss")#正确
print(d)
print(d1)
#日期运算
t = arrow.now()
t1=t.shift(hours=-1)  # 前一天 weeks months years hours days
print(t1.format("YYYY-MM-DD:HH:mm:ss"))  # 前一天) 
a1=arrow.get('2022-02-01 12:15:15', 'YYYY-MM-DD HH:mm:ss') #这里少一个冒号

b2=arrow.get('2021-03-01')
print("b2-a1",b2-a1)
dd=b2-a1
print(type(dd))

e=arrow.utcnow().format('YYYY-MM-DD HH:MM:SS')
print("arrow.utcnow().format('YYYY-MM-DD HH:MM:SS')",e)

t1 = arrow.now()
print("arrow.now()",t1)

###################################################################################################################
# #from DateTime.DateTime import datetime
# from datetime import datetime, date, time, timezone

# # 当前时间+3天 print(datetime.datetime.now() + datetime.timedelta(3))
# print("datatime.now 取当前时间",datetime.now()) # datatime.now 取当前时间

# print(date.today())  #取当前日期
# print("使用time 表示")
# #使用time 表示
# import time
# # 把结构化时间转换为格式化时间 # %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒 
# print("把结构化时间转换为格式化时间 # %Y年-%m月-%d天 %X时分秒=%H时:%M分:%S秒 ",time.strftime("%Y-%m-%d %X", time.localtime() )) #取当前日期
# # 把格式化时间化为结构化时间，它和strftime()是逆操作 
# print("# 把格式化时间化为结构化时间，它和strftime()是逆操作 ",time.strptime('2013-05-20 13:14:52', '%Y-%m-%d %X'))
# print("time.localtime()",time.localtime(),"time.time()",time.time())
# start = time.time() 
# time.sleep(0.1) 
# end = time.time()
# total_time=end-start
# print(time.strftime("%X",time.localtime(total_time)))
# print(time.strftime("%Y-%m-%d %X",time.gmtime(11111123))) #GMTIME是按标准时间 LOCALTIME是按了北京时间
# now_time=time.time()
# #将秒变为日期
# print("将秒变为日期")
# print(time.strftime("%H:%M:%S", time.gmtime(36000)))
# def mmtohh(mm:int)->str:
# 	days=str(mm//3600//24)
# 	times=str(time.strftime("%H:%M:%S", time.gmtime(mm)))
# 	return days+"天"+times

# print(mmtohh(13600))
# print(time.time())
