迁移xadmin到centos7.5.

1、在centos 安装 python 环境。可以安装一个anaconda,详细见《linux 安装 anaconda》

2、安装虚拟环境：

2.1更新conda源,如果不更改源的话，无法创建虚拟环境

```bash
base) [root@localhost Downloads]# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
(base) [root@localhost Downloads]# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
(base) [root@localhost Downloads]# conda config --set show_channel_urls yes
(base) [root@localhost Downloads]# conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
```

2.2 附conda的一些常用

```python
conda create -n your_env_name python=3.6
conda activate 环境名
conda deactivate 
conda clean --all #删除缓存
conda config --show #查看已经安装过的镜像源
conda config --remove channels url    #删除镜像地址url
conda remove -n rcnn --all 删除环境

```

2.3 创建3.8的环境

conda create -n python388 python=3.8.8



3 在虚拟环境里用pip3 安装django和uwsgi

首先在系统安装好uwsgi,yum install uwsgi

```text
pip3 install django （如果用于生产的话，则需要指定安装和你项目相同的版本）
pip3 install uwsgi
```

4 将需要迁移的包上传到centos，上传方法参照如下：

```
yum install samba samba-client samba-common

smbclient //192.168.4.253/oksoft -U 11608@mastercn.local

lcd /home

get requirements01.txt

get xadmin01.rar
```

5进入python388环境

conda activate python388

