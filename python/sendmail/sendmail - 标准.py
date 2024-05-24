#如下为模板
# 进行邮箱连接的库
import smtplib
# 处理邮件内容的库
from email.mime.text import MIMEText
from email import encoders  # 邮箱编码器
from email.mime.multipart import MIMEMultipart  # 多部件库
from email.header import Header  # 国际化标题
from email.mime.base import MIMEBase  # 表示任意对象
from pathlib import Path
import keyring
import filetimes
import arrow
# 获取注册在系统中的第三方授权码
mail_pass = keyring.get_password("163", "aliaiiw@163.com")
# 构造邮件多元对象
email = MIMEMultipart()
email["Subject"] = "今天备份的工作记录"  # 定义邮件主题
email["From"] = "aliaiiw@163.com"  # 发件人
email["To"] = "107766637@qq.com"  # 收件人
# 邮件正文内容
contents = "今天的工作备份,请查收。"
att = MIMEText(contents, "plain", "utf-8")  # 使用UTF-8编码格式保证多语言的兼容性
email.attach(att)
# word附件 已经屏蔽
p = Path(r"e:\\log")
t = arrow.now()
t1=t.format("YYYY-MM-DD")
print(arrow.now())

for att_name in p.iterdir():
		if filetimes.get_FileCreateTime(att_name)==t1:
			att1 = MIMEBase("application", "octet-stream")
			att1.set_payload(open(att_name, "rb").read())
			# 设置编码格式,附件重命名成xxx.docx
			att1.add_header("Content-Disposition", "attachment", filename=Header(att_name.name, "utf-8").encode())
			encoders.encode_base64(att1)
			email.attach(att1)
	# att1.set_payload(open(r"E:\\log\\备份日记2021115.zip", "rb").read())


mail_host="smtp.163.com"  #设置服务器
mail_user="aliaiiw@163.com"    #用户名
# smtp = smtplib.SMTP_SSL("smtp.qq.com", port=465)
smtpObj = smtplib.SMTP() 
smtpObj.connect(mail_host,25) #将端口改为25号就成功了 20220509
smtpObj.login(mail_user,mail_pass)
sender = 'aliaiiw@163.com'

receivers = ['alidongxing@163.com','107766637@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
smtpObj.sendmail(sender, receivers, email.as_string())

 #send_email('smtp.163.com', 'xxxx@163.com', 'xxxx', 'xxxx@163.com', '邮件标题', '邮件内容')
smtpObj.quit()
print("发送成功")
print(arrow.now())

