```
# **常用的linux命令**

有3种不同类型：文件所有者、群组用户、其他用户

权限	权限数值	二进制	具体作用
r	4	00000100	read，读取。当前用户可以读取文件内容，当前用户可以浏览目录。
w	2	00000010	write，写入。当前用户可以新增或修改文件内容，当前用户可以删除、移动目录或目录内文件。
x	1	00000001	execute，执行。当前用户可以执行文件，当前用户可以进入目录。
————————————————

一 ：
du -sh
du -sh *  当前目录 下各目录 的大小
df -m

chown -R oracle:oinstall 目录
chmod 777 目录 第一个7个用户,第二个7是组,第三个7是其它

二：
Linux下查看某个目录下的文件、或文件夹个数用到3个命令:ls列目录、用grep过虑、再用wc统计。
举例说明：
1、查看统计当前目录下文件的个数
　　ls -l | grep "^-" | wc -l
2、查看统计当前目录下文件的个数，包括子目录里的。
　　ls -lR| grep "^-" | wc -l
3、查看某目录下文件夹(目录)的个数，包括子目录里的。
　　ls -lR| grep "^d" | wc -l

命令解释：
ls -l
长列表输出该目录下文件信息(注意这里的文件，不同于一般的文件，可能是目录、链接、设备文件等)，每一行对应一个文件或目录，如果要列出所有子目录下的文件就是ls -lR。
grep "^-"
这里将长列表输出信息过滤一部分，只保留一般文件，如果只保留目录就是grep "^d"。
wc -l
统计输出信息的行数，因为已经过滤得只剩一般文件了，所以统计结果就是一般文件信息的行数，又由于一行信息对应一个文件，所以也就是文件的个数。

三：
查看服务列表代码  
sudo service --status-all
sudo initctl list
chkconfig 

四：
uname -a
Linux ubuntu 3.16.0-23-generic #31-Ubuntu SMP Tue Oct 21 18:00:35 UTC 2014 i686 i686 i686 GNU/Linux
Linux - 内核名


====确认:查发行版本的命令:cat /etc/redhat-release 查看CentOS版本 (通过)  redhat:使用cat /etc/issue 查看版本


audit - 主机名
2.6.18-128.el5 - 内核版本
#1 SMP Wed Jan 21 10:41:14 ....2009 - 内核编译日期
x86_64 - 操作系统版本
x86_64 - 处理器类型
x86_64 - 硬件平台
（以上3 个可能顺序不对，都是一样的不要区别，x86_64表示64位的）

GNU/Linux - 操作系统


六：
tar -czvf /目标/123.tar.gz  /源目录
tar -ztvf 123.tar.gz   （查看）  
tar -xtvf 123.tar.gz   （解压）
------------------------------------如上是有压缩与解压

jar -cvf /weblogic/wls1036/deploy/backup/hryw`date +%Y%m%d`.war /weblogic/wls1036/deploy/hryw/ 压缩  //默认没有该命令
jar -xvf 目标  源   --解压  （省略目标，即为目录 为目标）

Linux下自带了一个unzip的程序可以解压缩文件，
解压命令是：unzip filename.zip 
同样也提供了一个zip程序压缩zip文件，命令是 
zip filename.zip files 
会将files压缩到filename.zip   

七：授权
读写执行（421）
chmod 111 ssh_config
chmod 222 ssh_config
chmod 444 ssh_config

八：用户
cat /etc/passwd |cut -f 1 -d : （查看用户）  a:b  指定以:为分隔  f为字段  取第一个字段

--cut 截取字段  f 指定第一段 d 指定截取的符号


useradd test
passwd test(创建用户）
1、添加用户

首先用adduser命令添加一个普通用户，命令如下：
#adduser tommy  //添加一个名为tommy的用户
#passwd tommy   //修改密码
Changing password for user tommy.
New UNIX password:     //在这里输入新密码
Retype new UNIX password:  //再次输入新密码
passwd: all authentication tokens updated successfully.
2、赋予root权限
方法一：修改 /etc/sudoers 文件，找到下面一行，把前面的注释（#）去掉

## Allows people in group wheel to run all commands

%wheel    ALL=(ALL)    ALL
然后修改用户，使其属于root组（wheel），命令如下：
#usermod -g root tommy
修改完毕，现在可以用tommy帐号登录，然后用命令 su - ，即可获得root权限进行操作。
方法二：修改 /etc/sudoers 文件，找到下面一行，在root下面添加一行，如下所示：

## Allow root to run any commands anywhere

root    ALL=(ALL)     ALL
tommy   ALL=(ALL)     ALL
修改完毕，现在可以用tommy帐号登录，然后用命令 su - ，即可获得root权限进行操作。

九：liunx 启动到命令行
1：首先打开VMware,将Linux 系统启动.会进入图形化界面,通过快捷键[Ctrl+Shift+Alt+Fn（n=1,2,3,4,5,6）],进入命令行界面  20191008 --测试用 crtl_alt_fn
2：在命令界面下，当然，必须要root或者具有root权限的用户名下才可以修改.
vi /etc/inittab --用vi编辑器编辑/etc/inittab文件 
3：找到id:5:initdefault这一行，把5改成3 

十：性能监控
1：vmstat 5 2  每5秒钟采集 共2次  一个汇总的性能监控
(（空闲 CPU时间，一般来说，id + us + sy = 100,一般我认为id是空闲CPU使用率，us是用户CPU使用率，sy是系统CPU使用率。）
(bi:即读块设备。 bo:即写块设备。)
--各参数说明见（http://www.cnblogs.com/ggjucheng/archive/2012/01/05/2312625.html）)
2：top   可以看到每个进程的
top命令显示的前五行是系统整体的统计信息。
(Tasks : 115 total  进程总数
1 running  正在运行进程数
114  sleeping  睡眠进程数
0  stopped  停止进程数
0  zombie  僵尸进程数
Cpu(s) : 16.1%  us  用户空间占用CPU百分比
2.0%  sy  内核空间占用CPU百分比
0.0%  ni  用户进程空间内改变过优先级的进程占用CPU百分比
79.5%  id  空闲CPU百分比
1.4%  wa  等待输入输出的CPU时间百分比
0.0%  hi
0.0%  si)  
3:iostat -d -k 2
iostat主要用于监控系统设备的IO负载情况，iostat首次运行时显示自系统启动开始的各项统计信息，

十一：
vi:
:%s /旧值/新值/g 
:set number  设置行号显示
输入行号  可以跳转
替换命令：1,$ s/321/tujaiiw/g （替换全部）

/字符串  查找字符串

1. 将光标移动到要复制的文本开始的地方，按v进入可视模式。
2. 将光标移动到要复制的文本的结束的地方，按y复制。此时vim会自动将光标定位到选中文本的开始的地方，并退出可视模式。

yy	复制光标所在的整行 
p 命令：粘贴命令，粘贴当前缓冲区中的内容。

1. 选定文本块。使用v进入可视模式，移动光标键选定内容。 

2.复制的命令是y，即yank（提起） ，常用的命令如下： 
    y      在使用v模式选定了某一块的时候，复制选定块到缓冲区用； 
    yy    复制整行（nyy或者yny ，复制n行，n为数字）； 
    y^   复制当前到行头的内容； 
    y$    复制当前到行尾的内容； 
    yw   复制一个word （nyw或者ynw，复制n个word，n为数字）； 
    yG    复制至档尾（nyG或者ynG，复制到第n行，例如1yG或者y1G，复制到档尾）  
    

3. 剪切的命令是d，即delete，d与y命令基本类似，所以两个命令用法一样，包括含有数字的用法.  
   d      剪切选定块到缓冲区； 
   dd    剪切整行 
   d^    剪切至行首 
   d$     剪切至行尾 
   dw    剪切一个word 
   dG     剪切至档尾  

4. 粘贴的命令式p，即put（放下） 
   p      小写p代表贴至游标后（下），因为游标是在具体字符的位置上，所以实际是在该字符的后面 
   P      大写P代表贴至游标前（上） 
   整行的复制粘贴在游标的上（下）一行，非整行的复制则是粘贴在游标的前（后）

v模式：shift+> (向右缩进) ，shift+<(向左缩进)。 set tabstop=4 shiftwidth=4 

撤销undo上次操作：u

重做redo上次操作：ctrl+R

强制保存：wq!  强制退出q! 


十二：
find -name april* 在当前找
find -name An*
find -name "An*" 不支持正则表达式
find / -name apr  在/ 下找

 find -name "[a-z]s*" -exec ls -l {} \;

查找某一类型的文件，诸如：
b – 块建筑文件。chinaunix论坛。
d – 目录。
c – 字符建筑文件。
p – 管道文件。
l – 符号链接文件。
f – 日常平凡文件。
-size n：[c] 查找文件长度为n块的文件，带有c时表示文件长度以字节计。

-mtime   -n +n                #按文件更改时间来查找文件，-n指n天以内，+n指n天以前
-atime    -n +n               #按文件访问时间来查GIN: 0px">
-ctime    -n +n              #按文件创建时间来查找文件，-n指n天以内，+n指n天以前
find    /   -mmin   -5         # 查找在系统中最后5分钟里修改过的文件
find    /   -mtime   -1       #查找在系统中最后24小时里修改过的文件
查当前目录下的所有普通文件

# find . -type f -exec ls -l {} \; $ find logs -type f -mtime +5 -exec   -ok   rm {} \;

 find -name '1' -type d  -mmin -5

十三：for
#!/bin/bash
for((i=0;i<10;i++));do
echo $i;
done

十四：定时任务

--前提 crond 服务启动

用户设置 
crontab -e

*/1 * * * * /mysh/mycrontab.sh

系统设置

vi /etc/crontab

十五：while 及读取文件内容

vi mywhile
while read line
do
echo $line > ${line}date %d
done < ntest

---------------------------------------

十六：if

 if [ $line ];then

> echo date
> else
> echo data %d
> fi
> data %d
> [root@localhost exp]# 

----------------------------------------------

十七：正则表达式

 ls -F | grep /$|wc -l  --以结尾

 ls|grep "^[^abc]"   --以XXX开头


十八：挂点

mkdir /mnt/mycd
mount /dev/sr0 /mnt/mycd

十九：rpm

rpm -i -v -h  i install v 看  h 进度  -e 删除  -U升级  -qi 查询(注意查询时，必须是包名，而不是全称）
RPM         ==安装到自动目录
源码包安装  ==安装到指定目录


二十：
ls | xargs cat  --将前面的输出作为后面命令的参数
ls |cat         --将前面的输出作为后面的输入


二十一：查看所有服务

ntsysv  
sudo service --status-all
sudo initctl list
chkconfig 


二十二：安装yum

wget http://tel.mirrors.163.com/centos/5/os/x86_64/CentOS/yum-3.2.22-40.el5.centos.noarch.rpm 
wget http://tel.mirrors.163.com/centos/5/os/x86_64/CentOS/python-elementtree-1.2.6-5.x86_64.rpm 
wget http://tel.mirrors.163.com/centos/5/os/x86_64/CentOS/python-2.4.3-56.el5.x86_64.rpm

二十三 xargs 以及 awk 的使用

ps aux|grep oracle|awk '{print $2}'|xargs kill -9

二十四 
netstat -apnl

==a=all（不包括L 正在监听？） n端口显示数字 p显示programname l显示套 L正在监听


二十五：修改系统时间
 cd /usr/share/zoneinfo/ 

 cp UTC /etc/localtime 

二十六：[root@localhost etc]# ls |grep yum|xargs ls -l

可以查找当前目录包括的内容

二十七：不重启可以让配置文件生效

配置文件：~/.bashrc (修改别名）
source ~/.bashrc

二十八：/etc/fstab --开机自动挂载默认的，不能挂载光盘，因为当下次光盘不能用时
会导致系统崩溃


29：运行级别：
redhat系的runlevel定义如下：

runlevel 0: halt 系统停机状态，系统默认运行级别不能设为0，否则不能正常启动

runlevel 1: single user 单用户工作状态，root权限，用于系统维护，禁止远程登陆

runlevel 2: multiuser without network 多用户状态(没有NFS)

runlevel3: multiuser 完全的多用户状态(有NFS)，登陆后进入控制台命令行模式

runlevel4: unuse 系统未使用，保留

runlevel5: x11 X11控制台，登陆后进入图形GUI模式

runlevel6: reboot 系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动

30:shutdown、reboot、halt、poweroff等，当然了我们可以使用init 运行等级runlevel 0即halt来关机，或使用init 运行等级runlevel 6即reboot来执行重启。

31:创建隐藏文件:touch .a.txt 则创建的文件是隐藏文件

32: / 是根目录,~ 是家目录

33:ls -a 显示隐藏文件

34：2>/dev/null 将错误过滤

35：文件类型

~	常规文件，即file
d	目录文件
b	block device 即块设备文件，如硬盘;支持以block为单位进行随机访问
c	character device 即字符设备文件，如键盘支持以character为单位进行线性访问
l	symbolic link 即符号链接文件，又称软链接文件
p	pipe 即命名管道文件
s	socket 即套接字文件，用于实现两个进程进行通信




```

