#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 多部件库
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="aliaiiw@163.com"    #用户名
mail_pass="GHFLAXITISFXXMIV"   #口令
 #IBPYQYJQNKZXJQMK
sender = 'aliaiiw@163.com'
email = MIMEMultipart()
receivers = ['alidongxing@163.com','107766637@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText('content','plain','utf-8')
message['From'] = sender
message['To'] =  receivers[0] #这个只是在收件人地址显示用的,实际上是用receivers作实际应用
subject = 'Python SMTP'  #发送邮件的标题
message['Subject'] = subject
# 邮件正文内容
contents = "不经一番寒彻骨，怎得梅花扑鼻香。"
att = MIMEText(contents, "plain", "utf-8")  # 使用UTF-8编码格式保证多语言的兼容性
email.attach(att)
# # word附件
# att1 = MIMEBase("application", "octet-stream")
# att1.set_payload(open(r"C:\\Users\TYC\Desktop\3.docx", "rb").read())
print ("开始发送邮件")
print(message.as_string())
# smtpObj = smtplib.SMTP() 
# smtplib.SMTP_SSL(mail_host, '465')    # 25 为 SMTP 端口号
smtpObj = smtplib.SMTP() 
#smtpObj.connect(mail_host,808)
smtpObj.connect(mail_host,25) #将端口改为25号就成功了 20220509
smtpObj.login(mail_user,mail_pass)

smtpObj.sendmail(sender, receivers, message.as_string())

 #send_email('smtp.163.com', 'xxxx@163.com', 'xxxx', 'xxxx@163.com', '邮件标题', '邮件内容')
print ("邮件发送成功")


# #如下为模板
# # 进行邮箱连接的库
# import smtplib
# # 处理邮件内容的库
# from email.mime.text import MIMEText
# from email import encoders  # 邮箱编码器
# from email.mime.multipart import MIMEMultipart  # 多部件库
# from email.header import Header  # 国际化标题
# from email.mime.base import MIMEBase  # 表示任意对象

# import keyring

# # 获取注册在系统中的第三方授权码
# pwd = keyring.get_password("yagmail", "284036658@qq.com")
# # 构造邮件多元对象
# email = MIMEMultipart()
# email["Subject"] = "上堂开示颂"  # 定义邮件主题
# email["From"] = "284036658@qq.com"  # 发件人
# email["To"] = "284036658@qq.com"  # 收件人
# # 邮件正文内容
# contents = "不经一番寒彻骨，怎得梅花扑鼻香。"
# att = MIMEText(contents, "plain", "utf-8")  # 使用UTF-8编码格式保证多语言的兼容性
# email.attach(att)
# # word附件
# att1 = MIMEBase("application", "octet-stream")
# att1.set_payload(open(r"C:\\Users\TYC\Desktop\3.docx", "rb").read())
# # 设置编码格式,附件重命名成xxx.docx
# att1.add_header("Content-Disposition", "attachment", filename=Header("上堂开示颂.docx", "utf-8").encode())
# encoders.encode_base64(att1)
# email.attach(att1)
# # 发送邮件
# smtp = smtplib.SMTP_SSL("smtp.qq.com", port=465)
# smtp.login("284036658@qq.com", pwd)
# smtp.sendmail("284036658@qq.com", "284036658@qq.com", email.as_string())
# smtp.quit()
# print("发送成功")