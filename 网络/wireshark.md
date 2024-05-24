过滤源ip、目的ip。在wireshark的过滤规则框Filter中输入过滤条件。如查找目的地址为192.168.101.8的包，ip.dst==192.168.101.8；查找源地址为ip.src==1.1.1.1；


端口过滤。如过滤80端口，在Filter中输入，tcp.port==80，这条规则是把源端口和目的端口为80的都过滤出来。使用tcp.dstport==80只过滤目的端口为80的，tcp.srcport==80只过滤源端口为80的包；


http模式过滤。如过滤get包，http.request.method=="GET",过滤post包，http.request.method=="POST"；


连接符and的使用。过滤两种条件时，使用and连接，如过滤ip为192.168.101.8并且为http协议的，ip.src==192.168.101.8 and http。


1、过滤返回内容包含某字符串

frame contains "xxxx"
#或者
tcp contains "xxxx"
#或者
http contains "xxxx"

#查看所有原地址为：192.168.0.106的数据包
ip.src == 192.168.0.106
#查看所有原地址为：192.168.0.106的 dsn数据包
ip.src == 192.168.0.106 and dns
#查看所有目标地址为：192.168.0.106的数据包
ip.dst == 192.168.0.1
#查看所有目标地址为：192.168.0.106的 dns 数据包
ip.dst == 192.168.0.1 and dns


#过滤所有端口为443的数据包
tcp.port == 443
#过滤源地址为：192.168.0.106，端口号为443的所有数据包
ip.src == 192.168.0.106 and tcp.port == 443


常用过滤语句

前面加！号代表去除该包。

例如：！http表示不选取http的包

src代表源端口，dst代表目的端口

ip.addr == 192.168.1.1 过滤ip地址为192.168.1.1的包

ip.dst == 192.168.1.1 过滤ip目的地址为192.168.1.1的包

ip.src == 192.168.1.1 过滤ip源ip地址为192.168.1.1的包

tcp  过滤tcp的包

tcp.port == 80 过滤端口为80的包

udp 过滤udp的包

arp 过滤arp的包

http http2 过滤http、http2的包

