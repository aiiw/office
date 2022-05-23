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

~~conda create -n python388 python=3.8.8~~

搞错了，实际的虚拟环境是xadmin01,  python3.7.10

3 在虚拟环境里用pip3 安装django和uwsgi

首先在系统安装好uwsgi,yum install uwsgi

```
首先查查源的django版本
(base) D:\xadmin01\xadmin01>django-admin --version
3.2.4
搞错了，实际的虚拟环境是xadmin01,  django 2.2.5
(base) D:\xadmin01\xadmin01>
```



```text
(python388) [root@localhost xadmin01]# pip install django==2.2.5
Collecting django==3.2.4
  Downloading Django-3.2.4-py3-none-any.whl (7.9 MB)
pip3 install uwsgi
```

4 在需要迁移的包中导出包

```
4.1将xadmin生成 xadmin.zip
4.2cmd,切换到项目根目录，pipreqs ./ --encoding=utf8
```

![image-20220517095042453](https://raw.githubusercontent.com/aiiw/office/main/img/image-20220517095042453.png)

5 将需要迁移的包上传到centos，上传方法参照如下：

```
yum install samba samba-client samba-common

smbclient //192.168.4.253/oksoft -U 11608@mastercn.local

lcd /home

get requirements.txt

get xadmin01.rar
```

5进入python388环境，安装 requirements

```
conda activate python388

pip install -r requirements.txt
```

6  将数据迁移到centos,并导入

```text
#导出Mysql,django为你的数据库mysqldump -uroot -p123456 dj3>django.sql
#把django.sql上传到服务器，在服务器里用下面命令导入

mysql -uroot -ppassword 
create database dj3

use dj3

source your /home/django.sql
```

7 启动程序 ，调试

```
python manage.py runserver 
发现还有缺少的包，就pip install 包


1 ModuleNotFoundError: No module named 'future'
pip install future

2 No module named 'crispy_forms'
解决方法：
pip install django_debug_toolbar
pip install django-crispy-forms


3
xadmin01/lib/python3.7/site-packages/django/utils/__init__.py)
解决ImportError: cannot import name 'six' from 'django.utils'
首先导入six库，pip3 install six

1.进入python3.6/site-packages

2.将six.py 复制到 django/utils即可
[root@localhost site-packages]# cd /root/anaconda3/envs/xadmin01/lib/python3.7/site-packages/
[root@localhost site-packages]# pwd
/root/anaconda3/envs/xadmin01/lib/python3.7/site-packages
[root@localhost site-packages]# cp six.py ./django/utils/


4 oduleNotFoundError: No module named 'reversion'
pip install reversion

5 django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?
pip install pymysql
已安装情况下仍然报错
报错内容为找不到
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module. Did you install mysqlclient?

ImportError: cannot import name 'python_2_unicode_compatible' from 'django.utils.encoding' (/root/anaconda3/envs/python388/lib/python3.8/site-packages/django/utils/encoding.py)
通常解决办法
/root/anaconda3/envs/xadmin01/lib/python3.7/site-packages/django/db/backends/mysql/目录中__init__.py中添加
import pymysql
pymysql.install_as_MySQLdb()

6 ImportError: cannot import name 'python_2_unicode_compatible' from 'django.utils.encoding'
添加from six import python_2_unicode_compatible

7 ModuleNotFoundError: No module named 'django.contrib.formtools'
 pip3 install django-formtools
 
 8ModuleNotFoundError: No module named 'httplib2'
 
 8 ImportError: cannot import name 'FieldDoesNotExist' from 'django.db.models'
 /home/xadmin01/xadmin01/extra_apps/xadmin/plugins/aggregation.py
 try:
    from django.db.models.fields import FieldDoesNotExist
except ImportError:
    from django.core.exceptions import FieldDoesNotExist
    
 9 ModuleNotFoundError: No module named 'import_export'
  pip install django-import_export
  
 10 
```





