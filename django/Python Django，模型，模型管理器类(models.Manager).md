# Python Django，模型，模型管理器类(models.Manager)（与数据库交互的接口），自定义模型管理器类

模型类.objects.all() ---> objects是Django自动生成的管理器对象，通过这个管理器对象可以实现与数据库的交互。

定义模型类时可以为模型类指定自定义的管理类对象，指定后Django就不会再生成默认的管理器对象了。

 

应用名/models.py（模型，定义模型类、模型管理类）：

from django.db import models

# 自定义的模型管理类（继承models.Manager）
```
class BookInfoManager(models.Manager):
    # 重写父类all()方法。 返回isDelete为False的所有记录。
    def all(self):
        # 默认返回所有记录。
        # 调用父类的成员语法为：super().方法名
        return super().all().filter(isDelete=False)  # 通过过滤器,返回isDelete为False的所有记录。

    # 封装创建模型类对象的方法
    def create_book(self, title, pub_date):
        # self.model可以获得self的模型类名(BookInfo)
        book = self.model()  # 创建模型类对象。
        book.btitle = title
        book.bpub_date = pub_date
        book.bread=0
        book.bcommet=0
        book.isDelete = False
        # 将数据插入进数据表
        book.save()
        return book

 
```



# 图书类(模型类)
```
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, db_column='title')  # 图书名称
    bpub_date = models.DateField()  # 出版日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 删除标记
    

    objects = BookInfoManager()   # 使用自定义的管理器对象。

test.py（测试类）：
```

books = BookInfo.objects.all()  # 调用的是自定义的管理器类的all()方法,返回isDelete为False的所有记录。

book = BookInfo.objects.create_book("abc",date(1980,1,1))  # 调用管理器封装的方法,创建模型类对象。
————————————————