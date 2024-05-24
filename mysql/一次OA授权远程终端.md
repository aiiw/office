### 一次OA授权远程终端登录

这个错误，其实就是我们安装的MySQL不允许远程登录，解决方法如下：

1.在装有MySQL的机器上登录MySQL mysql -u root -p密码
执行use mysql;
select host from user where user = ‘root’;

该结果表示是当前的root用户限制在当前的ip内访问的，需要修改他的访问域。

2.执行update user set host = ‘%’ where user = ‘root’;

3.执行FLUSH PRIVILEGES 或者重启 MySQL 即可;

### 重点:需要重启 重启 重启 或者  直接在查询窗口执行:FLUSH PRIVILEGES 



##### 另外:在navicate 编辑数据的操作:

###### 1.需要在表的列表,打开表,点[+],注意如果有主键,直接复制是会有报错的,建议先复制了一行记录,然后将原记录改为新记录,然后

###### 再粘贴记录,这些粘贴出来的记录就是旧记录.



###### 另外:附还一些在脚本的操作办法

```

```

![image-20221215171452324](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20221215171452324.png)