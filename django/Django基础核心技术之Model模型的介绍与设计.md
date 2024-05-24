Django网络应用开发的**5项基础核心技术**包括模型（Model）的设计，URL的配置，View（视图）的编写，Template（模板）的设计和Form(表单)的使用。今天小编我就拼了老命来用千字长文给你来介绍下第一项Django核心基础知识之Model的设计吧。想持续了解后续Django Web开发技术请订阅我的公众号【**Python与Django大咖之路**】。



**什么是Model模型？**

**
**

Model (模型) 简而言之即数据模型。模型不是数据本身（比如数据库里的数据），而是抽象的描述数据的构成和逻辑关系。每个Django model实际上是个类，继承了models.Model。每个Model应该包括属性，关系（比如单对单，单对多和多对多）和方法。当你定义好Model模型后，Django的接口会自动帮你在数据库生成相应的数据表(table)。这样你就不用自己用SQL语言创建表格或在数据库里操作创建表格了，是不是很省心？



我们来看个书与出版社的实际案例。出版社有名字和地址。书有名字，描述和添加日期。当然我们还要利用ForeignKey定义出版社与书单对多的关系，因为一个出版社可以出版很多书。我们定义了如下模型，那你看看代码有问题吗?

```
# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField()

    def __str__(self):
        return self.name
		
class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    publisher = ForeignKey(Publisher)
    add_date = models.DateField()

    def __str__(self):
        return self.name
```



当你运行*python manage.py migrate* 创建表格的时候你会遇到错误，错误原因如下：

- CharField里的max_length选项没有定义
- ForeignKey(Publisher)里的on_delete选项有没有定义



所以当你定义Django模型Model的时候，你一定要十分清楚2件事:

- 这个Field是否有必选项, 比如CharField的max_length和ForeignKey的on_delete选项是必须要设置的。
- 这个Field是否必需(blank = True or False)，是否可以为空 (null = True or False)。这关系到数据的完整性。

其实在上述案例中还有一个隐藏的错误，即*TextField(blank = True, null = True)*。blank = True 意味这个字段不是必需的，在客户端不是必填选项。null = True意味这个数据库里这个字段可以存储为null空值。但是Django对于空白的CharField和TextField永远不会存为null空值，而是存储空白字符串''，所以正确的做法是设置default=''。



下表才是一个比较正确的Django模型(Model)。

```
# models.pyfrom django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name
		
class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = ForeignKey(Publisher, on_delete = models.CASCADE)
    add_date = models.DateField()

    def __str__(self):
        return self.name
```



**Django Model中字段(Field)的可选项和必选项**



| 字段与选项（必选项为黄色标注)                                |
| ------------------------------------------------------------ |
| CharField() 字符字段max_length = xxx or None如不是必填项，可设置blank = True和default = ''如果用于username, 想使其唯一，可以设置unique = True如果有choice选项，可以设置 choices = XXX_CHOICES |
| TextField() 文本字段max_length = xxx如不是必填项，可设置blank = True和default = '' |
| DateField() and DateTimeField() 日期与时间字段一般建议设置默认日期default date.For DateField: default=date.today - 先要from datetime import dateFor DateTimeField: default=timezone.now - 先要from django.utils import timezone对于上一次修改日期(last_modified date)，可以设置: auto_now=True |
| EmailField() 邮件字段如不是必填项，可设置blank = True和default = ''一般Email用于用户名应该是唯一的，建议设置unique = True |
| IntegerField(), SlugField(), URLField()，BooleanField()可以设置blank = True or null = True对于BooleanField一般建议设置defautl = True or False |
| FileField(upload_to=None, max_length=100) - 文件字段upload_to = "/some folder/"max_length = xxxx |
| ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,) upload_to = "/some folder/"其他选项是可选的. |
| ForeignKey(to, on_delete, **options) - 单对多关系 to必需指向其他模型，比如 Book or 'self' .必需指定on_delete options（删除选项): i.e, "on_delete = models.CASCADE" or "on_delete = models.SET_NULL" .可以设置"default = xxx" or "null = True" .如果有必要，可以设置 "limit_choices_to = "，如下面例子。staff_member = models.ForeignKey( User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, )可以设置 "related_name = xxx" 便于反向查询。 |
| ManyToManyField(to, **options) - 多对多关系to 必需指向其他模型，比如 User or 'self' .设置 "symmetrical = False " if 多对多关系不是对称的设置 "through = 'intermediary model' " 如果需要建立中间模型来搜集更多信息可以设置 "related_name = xxx" 便于反向查询。 |



**一个复杂点的Django Model模型**

**
**

我们现在来看一个更复杂点的Django模型。假设我们要开发一个餐厅(restaurant)的在线点评网站，允许用户(user)上传菜肴(dish)的图片并点评餐厅，我们就可以设计如下模型。用户与餐厅，餐厅与菜肴，及用户与菜肴都是单对多的关系。我们可以这样理解：一个用户可以访问点评多个餐厅，一个餐厅有多个菜肴，一个用户可以上传多个菜肴的图片。

```
# models.py

from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Restaurant(models.Model):
    name = models.TextField()
    address = models.TextField(blank=True, default='')
    telephone = models.TextField(blank=True, default='')
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.nameclass Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True,  default='')
    price = models.DecimalField('USD amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
# Related name "dishes" allows you to use restaurant.dishes.all to access all dishes objects
# instead of using restaurant.dish_set.all
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# This Abstract Review can be used to create RestaurantReview and DishReview

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} review".format(self.restaurant.name)
```



**你观察到Django模型设计里的细节了吗?**

**
**

我们的Dish模型里有一个restaurant的字段，建立了一个单对多的关系。我们可以通过dish.restaurant.name直接查询到菜肴所属的餐厅的名字。然而我们Restaurant模型里并没有dish的字段，我们如何根据restaurant查询到某个餐厅的所有菜肴呢？Django非常聪明，可以通过在dish小写后面加上'_set'进行反向查询。我们本来可以直接通过restaurant.dish_set.all的方法来进行查找的，然而这个方法并不直观。为了解决这个问题，我们在dish模型里设置'related_name = dishes", 这样我们就可以直接通过restaurant.dishes.all来反向查询所有菜肴了。注意一但你设置了related name, 你将不能再通过_set方法来反向查询。



```
restaurant = models.ForeignKey(Restaurant, related_name='dishes', on_delete=models.CASCADE)
```



第2个细节你需要关注的是Review模型里，我们设置了META选项: Abstract = True。这样一来Django就会认为这个模型是抽象类，而不会在数据库里创建review的数据表。实际上Model自带的META选项还有很多，都非常有用。见下文。



**常见的Django Model META类选项**



```
# models.py
from django.db import models

class Meta:
    # 按Priority降序, order_date升序排列.
    get_latest_by = ['-priority', 'order_date']
    # 自定义数据库里表格的名字
    db_table = 'music_album'
    # 按什么排序
    ordering = ['pub_date']
    # 定义APP的标签
    app_label = 'myapp'
    # 声明此类是否为抽象
    abstract = True
    # 添加授权
    permissions = (("can_deliver_pizzas", "Can deliver pizzas"),)
```



未完待续。Django自带的models里有两个非常重要的类，一个是models.Model, 另一个是models.Manager。下次我们将介绍models.Manager类是什么东东以及如何使用它。