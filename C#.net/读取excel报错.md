最近在做Excel文件导入时候，出现"未在本地计算机上注册“Microsoft.ACE.OLEDB.12.0”提供程序" 问题

![img](https://img2022.cnblogs.com/blog/775247/202203/775247-20220331170710739-988730544.png)

 产生原因：这个问题一般是在导入Excel文件的时候报的错，原因是缺少了相对应的Microsoft Access Database Engine组件。

解决方法：安装AccessDatabaseEngine插件

1）访问下载路径（https://www.microsoft.com/zh-cn/download/details.aspx?id=13255），选择语言，点击下载

![img](https://img2022.cnblogs.com/blog/775247/202203/775247-20220331170922947-485436316.png)

 2）选择合适程序下载（32位或64位）

 ![img](https://img2022.cnblogs.com/blog/775247/202203/775247-20220331171205401-1852673514.png)

 3）点击AccessDatabaseEngine.exe 进行安装

![img](https://img2022.cnblogs.com/blog/775247/202203/775247-20220331171612833-2072393117.png)

 4）安装完成后，重启IIS或重新打开SQL Server管理工具导入（我是用程序调用的，需要重启IIS）

