**一个最基本的django模型**

```
python manage.py makemigrations upfile
python manage.py migrate upfile
```

我们来先看下一个新闻博客的Article模型。这个模型是最基本的django模型，里面包括了各个字段（fields)，重写了显示文章对象名字的__str__方法（python内置的），并在Meta选项里给模型命名(verbose name)。我们建议每个django模型至少包括字段，重写的__str__方法和Meta选项。

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now


class Article(models.Model):

    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    title = models.CharField('标题', max_length=200, unique=True)
    slug = models.SlugField('slug', max_length=60)
    body = models.TextField('正文')
    pub_date = models.DateTimeField('发布时间', default=now, null=True)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    mod_date = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article"
```



**基础模型很多时候并不能满足我们的需求**

**
**

django的基础模型很多时候并不能满足我们的需求。试想我们打算使用django自带的通用视图创建文章，由于通用视图在完成对象创建后需要跳转到文章的absolute_url, 这时我们需要在模型里加入自定义的get_absolute_url方法。由于我们希望统计每篇文章浏览次数，我们还需自定义一个使浏览量自增1的viewed方法，并更新数据表（详情见：[django实战，之开发页面计数器。](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483796&idx=1&sn=f9dd96a08e632553c53849dcb2cd26ef&chksm=a73c61ac904be8ba6d4dc6e2c7552199fe1329c44c98df4603265059dd1dd4b718ec55576ede&scene=21#wechat_redirect)）

```python
def get_absolute_url(self):
    return reverse('blog:article_detail', args=[str(self.id)])

def viewed(self):
    self.views += 1
    self.save(update_fields=['views'])
```

如果我们希望调用Article.objects.all()按时pub_date降序排列查询结果，我们可以在Meta里加入ordering选项即可。

```python
class Meta:
    ordering = ['-pub_date']
    verbose_name = "article"
```



**模型中自定义图片和文件上传路径**



Django模型中的ImageField和FileField的upload_to选项是必填项，其存储路径是相对于MEIDA_ROOT而来的。然而我们可能希望动态定义上传路径，比如把文件上传到每个用户名下的文件夹里，并对上传文件重命名，这时我们可以定义一个user_directory_path方法。



```python
from django.db import models
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # return the whole path to the file
    return os.path.join(instance.user.id, "avatar", filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=user_directory_path, verbose_name="头像")
  
```



**Django模型的Manager方法值得一看**

**
**

Django模型自带models.Manager方法，可以简化我们的代码。如下面案例中，我们可以使用Person.objects.all()查询到所有人，而Person.authors.all和Person.editors.all()只返回所authors和editors。

```python
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='E')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', _('Author')), ('E', _('Editor'))))
    objects = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()
```



**Django模型的save方法重写**



在很多应用场景中我们需要重写django模型的save方法，比如本例中我们希望根据title生成slug，并在一个对象数据save完成后做其它事情（比如发送邮件或发送信号），我们可以按如下代码重写django模型的save方法，非常容易。

```python
from django.template.defaultfilters import slugify

class Article(models.Model):
    ...

    def save(self, *args, **kwargs):
        if not self.slug or not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        # do other things. send_mail()
```



**一个完美的Django高级模型结构**

一个完美的django高级模型结构如下所示，可以满足绝大部分应用场景，希望对你有所帮助。

```python
from django.db import models
from django.urls import reverse


# 自定义Manager方法
class HighRatingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating='1')
    

class Product(models.Model):
    # CHOICES选项
    RATING_CHOICES = (
        ("1", 'Very good'),
        ("2", 'Good'),
        ("3", 'Bad'),
    )

    # 数据表字段
    name = models.CharField('name', max_length=30)
     rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    # MANAGERS方法
    objects = models.Manager()
     high_rating_products =HighRatingManager()

    # META类选项
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    # __str__方法
    def __str__(self):
        return self.name

    # 重写save方法
    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs) 
        do_something_else()

    # 定义绝对路径
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'pk': self.id})

    # 定义其它方法
    def do_something(self):
```