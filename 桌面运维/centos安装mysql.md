centos 安装mysql8

https://www.django.cn/article/show-2.html

一、如果我们想通过YUM在线安装Mysql，我们需要添加MySQL Yum库。

```
cd /home/
wget https://repo.mysql.com//mysql80-community-release-el7-1.noarch.rpm
```

下载好之后，然后安装它

```
rpm -ivh mysql80-community-release-el7-1.noarch.rpm
```

这样我们就在YUM里添加了MySQL YUM安装包。

**二、选择要安装的MySQL版本。**

在YUM库中，存储了多个版本的MySQL，现在最新版的MySQL版本为8.0的，我们更新YUM库之后，默认安装的是最新版本的MySQL，其它版本的存储库是禁用的。我们可以通过下面的命令来查看，到底支持哪几他版本的MySQL，并查看状态。

```
yum repolist all | grep mysql
```

![111.jpg](https://www.django.cn/media/upimg/111_20181120030641_839.jpg)

我可以看到现在支持这几个版本的MySQL安装，并且MySQL8.0是属于启用状态，如果我们想要安装8.0版本的MySQL就不需要更改任何配置，直接安装即可。现在我们要安装的是5.7版本的，所以我们需要修改一下配置文件。打开/etc/yum.repos.d/mysql-community.repo

```
vim /etc/yum.repos.d/mysql-community.repo
```

我们找到5.7的和8.0的配置信息。

```
[mysql57-community]
name=MySQL 5.7 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

[mysql80-community]
name=MySQL 8.0 Community Server
baseurl=http://repo.mysql.com/yum/mysql-8.0-community/el/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
```

找到要安装的MySQL版本配置信息，并编辑启用的选项。enabled=0为禁用对应版本的YUM库，enabled=1为启用，默认8.0的配置为enabled=1，安装5.7的话，我们就把8.0的enabled=1修改为enabled=0，然后把5.7的enabled=0修改为enabled=1。

修改完成之后，我们通过下面的命令来验证状态：

```
yum repolist enabled | grep mysql
```

![222.jpg](https://www.django.cn/media/upimg/222_20181120032306_613.jpg)

如上图所示，我们一会就安装这几个软件。

**三、安装MySQL**

```
sudo yum install mysql-community-server
```

假如出现类似：
mysql-community-client-8.0.28-1.el7.x86_64.rpm 的公钥尚未安装的提示，请需要输入下面的命令，导入公钥，然后再使用上面的命令进行安装。

```
rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
```

安装成功之后，通过下面命令启动Mysql：

```
sudo service mysqld start
```

如果是基本BL7平台的操作系统则用下面的命令：

```
sudo systemctl start mysqld.service
```

查看启动状态：

```
sudo service mysqld status
或
sudo systemctl status mysqld.service  #BL7平台
```

![333.jpg](https://www.django.cn/media/upimg/333_20181120034006_143.jpg)

出现这个说明MySQl已经启动。

**四、设置MySQL密码。**

MySQL在启动的时候，就已经自动进行了初始化。下面我们可以通过这个命令来查看超级用户的密码，这个存放在MySQL日志里：

```
sudo grep 'temporary password' /var/log/mysqld.log
```

![444.jpg](https://www.django.cn/media/upimg/444_20181120034620_409.jpg)

命令在上图标记的地方，然后我们通下面的命令登录MySQL：

```
mysql -u root -p
```

上面是系统生成的临时密码，安全起见，我们需要尽快更改超级用户帐户密码:

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'WwW.django.cn123';
```

密码一定要复杂，需要大小写字母、数字、和特殊符号混合，不然提示不符合要求。

![555.jpg](https://www.django.cn/media/upimg/555_20181120035452_885.jpg)

至此，MySQL5.7安装完毕。

五、常用MySQL数据库操作

```
mysql数据库使用总结
本文主要记录一些mysql日常使用的命令，供以后查询。
1.更改root密码
mysqladmin -uroot password 'yourpassword'
2.远程登陆mysql服务器
mysql -uroot -p -h192.168.137.10 -P3306
3.查询数据库
show databases;
4.进入某个数据库
use databasename;
5.列出数据库中的表
show tables;
6.查看某个表全部字段
desc slow_log;
show create table slow_log\G; （不仅可以显示表信息，还可以显示建表语句）
7.查看当前用户
select user();
8.查看当前所在数据库
select database();
9.创建新数据库（可以指定字符集）
create database db1 charset utf8;
10.创建新表
create table t1 (`id` int(4), `name` char(40));
11.查看数据库版本
select version();
12.查看数据库状态
show status;         当前会话状态
show global status;  全局数据库状态
show slave status\G;   查看主从数据库状态信息
13.查询数据库参数
show variables;
14.修改数据库参数
show variables like 'max_connect%';
set global max_connect_errors = 1000;（重启数据库会失效，要在配置文件中修改）
15.查看当前数据库队列
show processlist;
16.创建普通用户并授权给某个数据库
grant all on databasename.* to 'user1'@'localhost' identified by '123456';
17.查询表数据
select * from mysql.db;           //查询该表中的所有字段
select count(*) from mysql.user;  //count(*)表示表中有多少行
select db,user  from mysql.db;    //查询表中的多个字段
select * from mysql.db where host like '10.0.%';在查询语句中可以使用万能匹配 “%”
18.插入一行数据
insert into db1.t1 values (1, 'abc');
19.更改表的某一行数据
update db1.t1 set name='aaa' where id=1;
20.清空表数据
truncate table db1.t1;
21.删除表
drop table db1.t1;
22.清空数据库中的所有表（数据库名是eab12）
mysql -N -s information_schema -e "SELECT CONCAT('TRUNCATE TABLE ',TABLE_NAME,';') FROM TABLES WHERE TABLE_SCHEMA='eab12'" | mysql -f eab12
23.删除数据库
drop database db1;
24.数据库备份
mysqldump  -uroot -p'yourpassword' mysql >/tmp/mysql.sql
25.数据库恢复
mysql -uroot -p'yourpassword' mysql </tmp/mysql.sql
26.新建普通用户
CREATE USER name IDENTIFIED BY 'ssapdrow';
27.更改普通用户密码
SET PASSWORD FOR name=PASSWORD('fdddfd');
28.查看name用户权限
SHOW GRANTS FOR name;
29.脚本中执行mysql命令
mysql -uuser -ppasswd -e"show databases"
echo "show databases"|mysql -uuser -ppassword
以下是执行大量mysql语句采用的方式
mysql -uuser -hhostname -ppasswd <<EOF
mysql语句
EOF
```

相关文章：