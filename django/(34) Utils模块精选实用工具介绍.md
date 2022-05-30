## **django.utils.dateparse模块**

在日常开发工作中我们经常需要将用户输入的字符串格式的时间和日期转化为日期和时间对象，django.utils.dateparse提供了如下几个方法供我们使用:

- `parse_date`(*value*)

接收字符串，比如'2020-04-30'，返回datetime.date类型的数据。

- `parse_time`(*value*)

接收字符串，比如'12:35:20'返回datetime.time类型的数据。

- `parse_datetime`(*value*)

接收字符串，比如'2020-04-40 12:35:20', 返回datetime.datetime类型的数据。



## **django.utils.decorators模块**

给基于类的视图(CBV)使用装饰器时，我们需要借助于该模块的method_decorator方法实现。它还支持decorators列表, 如下所示:

```python

from django.utils.decorators import method_decorator

decorators = [login_required, check_user_permission]

@method_decorator(decorators, name='dispatch')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_manage_form.html'
```


另外该模块的另外两个有用方法是：

- decorator_from_middleware(middleware_class)： 该方法将一个Middleware类转变为一个装饰器，可以用于单个视图函数上。

- decorator_from_middleware_with_args(middleware_class): 与上一方法作用相同，只不过支持传递额外的参数。

我们常用的@cache_page装饰器就是从中间件CacheMiddleware转换过来的。

```

cache_page = decorator_from_middleware_with_args(CacheMiddleware)

@cache_page(3600)
def my_view(request):
    pass
```

##  

## **django.utils.encoding模块**

```
smart_str(obj, encoding='utf-8', strings_only=False, errors='strict')
```

该方法可以将一个obj对象转化为str类型的表示形式。如果strings_only设置为True，意味着不转换非字符串类型的对象obj。如果对象里包含中文字符串，设置encoding="etf-8"可以避免乱码。



## **django.utils.safestring模块**

在前端模板里如果我们希望Django避免对一个字符串进行转义，我们可以|safe模板过滤器或autoescape标签。而在视图里如果我们希望Django避免对一个字符串转义，就需要使用该模块提供的mark_safe方法了。

```python

from django.utils.safestring import mark_safe
def index(request):
    content = "<a href='http://www.baidu.com'>百度</a>"
    marked_content = mark_safe(content)
    return render(request, 'indext.html', {'content': marked_content})
```



## **django.utils.timezone模块**

###### 在现实开发环境中，存在有多个时区，用户之间很有可能存在于不同的时区，所以每个用户当前时间都是不一样的。Django在存储和操作日期时间类型数据的最佳实践是在数据库中统一存储UTC标准时间，在与用户打交道时使用用户所在时区的时间。

##  

###### datetime.datetime.now()获取的时间是不带任何时区信息的，不便于与数据表中的日期时间类型数据进行直接比对，而借助于timezone模块提供的now方法，我们可以总是可以获取当前UTC标准时间。借助timezone模块提供的localtime方法，我们还以很快获得当地时间。

## 借助于该模块提供的now方法，你可以获得用户当前时区的时间，非常有用。

```python
# settings.py
TIME_ZONE = 'Asia/Shanghai'
# python manage.py shell
>>> from django.utils import timezone
>>> now1 = timezone.now() # 获得带时区信息的UTC时间
datetime.datetime(2016, 12, 7, 1, 41, 36, 685921, tzinfo=<UTC>)
>>> local_now = timezone.localtime(now1) # 获得上海时区所在时间
datetime.datetime(2016, 12, 7, 9, 41, 36, 685921, tzinfo=<UTC>)xxxxxxxxxx8 1# settings.py2TIME_ZONE = 'Asia/Shanghai'3# python manage.py shell4>>> from django.utils import timezone5>>> now1 = timezone.now() # 获得带时区信息的UTC时间6datetime.datetime(2016, 12, 7, 1, 41, 36, 685921, tzinfo=<UTC>)7>>> local_now = timezone.localtime(now1) # 获得上海时区所在时间8datetime.datetime(2016, 12, 7, 9, 41, 36, 685921, tzinfo=<UTC>)# settings.pyTIME_ZONE = 'Asia/Shanghai'# python manage.py shell>>> from django.utils import timezone>>> now1 = timezone.now() # 获得带时区信息的UTC时间datetime.datetime(2016, 12, 7, 1, 41, 36, 685921, tzinfo=<UTC>)>>> local_now = timezone.localtime(now1) # 获得上海时区所在时间datetime.datetime(2016, 12, 7, 9, 41, 36, 685921, tzinfo=<UTC>)
```

## **django.utils.text模块**

该模块提供的最常用的方法莫过于slugify方法了。使用allow_unicode=True选项还允许生成含有中文的slug哦。

```python
from django.utils.text import slugify
>>> slugify(' Joel is a slug ')
'joel-is-a-slug'
>>> slugify('你好 World', allow_unicode=True)
'你好-world'xxxxxxxxxx6 12from django.utils.text import slugify3>>> slugify(' Joel is a slug ')4'joel-is-a-slug'5>>> slugify('你好 World', allow_unicode=True)6'你好-world'from django.utils.text import slugify>>> slugify(' Joel is a slug ')'joel-is-a-slug'>>> slugify('你好 World', allow_unicode=True)'你好-world'
```