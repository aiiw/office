import win32net

import os

username = '11608'
password = '12qwaszx'
ip_address = '192.168.0.123'
share_name = '11608'

directory = r'\\{}\{}'.format(ip_address, share_name)

# 指定用户名和密码访问共享资源
command = 'net use {} /user:{} {}'.format(directory, username, password)
os.system(command)


directory = r'\192.168.0.123\11608'

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        print("文件: " + filepath)
    elif os.path.isdir(filepath):
        print("目录: " + filepath)

# 断开与共享的连接
