OSI参考模型和TCP/IP参考模型

![image-20220523200950164](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523200950164.png)

应用层——消息
传输层——数据段(segment)
网络层——分组、数据包（packet）
链路层——帧（frame）
物理层——P-PDU（bit）

1.报文(message)
报文包含了应用层的完整的数据信息。

2.数据段(segment)
数据段是传输层的信息单元。

3.数据报(datagram)
数据报是面向无连接的数据传输。采用数据报方式传输时，被传输的分组称为数据报。如传输层TCP的分组叫做数据段，UDP的叫做数据报。
还有一种说法是数据报是数据包的分组，一个完整的数据包由一个或多个数据报组成。（待确认）

4.数据包(packet)
数据包是网络层传输的数据单元。也称为IP包，包中带有足够寻址信息(IP地址)，可独立地从源主机传输到目的主机
还有一种说法是数据报是网络层的传输基本单位，数据包是IP协议中完整的数据单元，由一个或多个数据报组成。（待确认）

5.帧(frame)
帧是数据链路层的传输单元。它将上层传入的数据添加一个头部和尾部，组成了帧，帧根据MAC地址寻址。 

6.bit流(bit)
bit是在物理层的介质上直接实现无结构bit流传送的。

![image-20220523201014142](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523201014142.png)

![image-20220523201027985](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220523201027985.png)

