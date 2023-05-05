

好的，以下是更详细的创建 Django DRF 项目步骤：

# 1安装 Django

确保您的机器上已安装 Python，并使用以下命令安装 Django：

```python
Copy Code
pip install django
```

#      2.创建 Django 项目

使用以下命令创建 Django 项目：

```python
Copy Code
django-admin startproject project_name
```

其中，project_name 是您要创建的项目名称。

# 3.创建 Django 应用

在项目文件夹中执行以下命令创建 Django 应用：

```python
Copy Code
python manage.py startapp myapi
```

其中，app_name 是您要创建的应用名称。

# 4.配置数据库

在项目的 [settings.py](http://settings.py/) 文件中配置数据库信息。Django 默认使用 SQLite 数据库，因此可以直接使用该默认设置。如果您需要使用其他数据库，请参考 Django 的官方文档进行配置。

例如，在 [settings.py](http://settings.py/) 中配置 mysql数据库：

```python
pythonCopy Code
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
            'NAME': 'dj3',  # 数据库名称
            'HOST': '127.0.0.1',  # 数据库地址，本机 ip 地址 127.0.0.1
            'PORT': 3306,  # 端口
            'USER': 'root',  # 数据库用户名
            'PASSWORD': '123456',  # 数据库密码
    }
}
```

1. 创建模型

在应用的 [models.py](http://models.py/) 文件中定义数据模型。例如，假设您要创建一个 Book 模型表示书籍信息：

```python
pythonCopy Code
from django.db import models

class Book(models.Model):
    # 定义Book模型类，继承自Django内置的models.Model类

    class Genre(models.TextChoices):
        # 枚举类型，定义了合法的图书类型
        NOVEL = 'NV', '小说'
        HISTORY = 'HI', '历史'
        BIOGRAPHY = 'BG', '传记'
        THRILLER = 'TH', '惊悚'

    title = models.CharField(max_length=100, verbose_name="书籍标题")
    # 字符串类型的书名，长度最大为100个字符，使用verbose_name参数定义了该字段在后台管理中显示的名称

    author = models.CharField(max_length=100, verbose_name="作者")
    # 字符串类型的作者名，长度最大为100个字符，使用verbose_name参数定义了该字段在后台管理中显示的名称

    description = models.TextField(blank=True, verbose_name="书籍描述")
    # 书籍描述，使用TextField类型表示，可以为空，使用verbose_name参数定义了该字段在后台管理中显示的名称

    genre = models.CharField(max_length=2, choices=Genre.choices, default=Genre.NOVEL, verbose_name="图书类型")
    # 图书类型，使用枚举类型Genre表示，使用choices参数指定所有可选值，使用default参数指定默认选项

    publish_date = models.DateField(verbose_name="出版日期", help_text="格式：YYYY-MM-DD")
    # 发布日期，使用DateField类型表示，使用verbose_name参数定义了该字段在后台管理中显示的名称，使用help_text参数添加了说明文本

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = "图书列表"
    # Meta类包含了一些模型的元数据（metadata），例如模型的名称、排序方式等。

    def __str__(self):
        return self.title
    # 定义__str__方法，返回书籍标题
这段代码与之前的版本相比，主要增加了以下内容：

Genre枚举类型：这个类型定义了合法的图书类型。我们使用了models.TextChoices来创建这个枚举类型，并将其他类型作为其成员。

genre属性：这个属性使用了CharField类型，但是它还指定了一个叫做choices的参数。该参数指定了可选的枚举值，这里是Genre.choices。我们也使用了default参数，指定了默认选项为Genre.NOVEL。

希望这些信息能够帮助您理解如何在Django模型中使用枚举类型，以及如何使用choices参数指定可选值。
```

```python
补充：
AutoField：自增长 ID 字段
BigAutoField：64 位自增长 ID 字段
BooleanField：布尔类型，True 或 False
CharField：字符串类型，通常用于短字符串
DateField：日期类型，格式为 YYYY-MM-DD
DateTimeField：日期时间类型，格式为 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
DecimalField：精度固定的小数类型
FloatField：浮点数类型
IntegerField：整数类型
BigIntegerField：大整数类型
PositiveIntegerField：正整数类型
SmallIntegerField：短整数类型
TextField：文本类型，通常用于长文本
TimeField：时间类型，格式为 HH:MM[:ss[.uuuuuu]]
FileField：文件类型，保存在上传目录中
ImageField：图片类型，保存在上传目录中
from myapp.models import Book, Publisher, Author
from datetime import date

# 1. 创建对象
# 使用构造函数创建新的模型实例，并使用 save() 方法将其保存到数据库中
book1 = Book(title='Python Crash Course', author='Eric Matthes', publish_date=date(2019, 5, 3))
book1.save()
book2 = Book(title='Python for Data Science Handbook', author='Jake VanderPlas', publish_date=date(2017, 10, 16))
book2.save()

publisher1 = Publisher(name='O\'Reilly Media', website='https://www.oreilly.com/')
publisher1.save()
publisher2 = Publisher(name='No Starch Press', website='https://nostarch.com/')
publisher2.save()

author1 = Author(name='Eric Matthes', email='eric@example.com')
author1.save()
author2 = Author(name='Jake VanderPlas', email='jake@example.com')
author2.save()

book1.authors.add(author1)
book2.authors.add(author2)

book1.publisher = publisher1
book1.save()
book2.publisher = publisher2
book2.save()

# 2. 获取单个对象
try:
    # 使用 get() 方法获取特定 ID 的模型实例
    book = Book.objects.get(id=1)
except Book.DoesNotExist:
    # 处理对象不存在的情况
    pass

# 3. 获取多个对象
# 使用 all() 方法获取所有模型实例
books = Book.objects.all()

# 4. 查询对象
# 4.1 使用 filter() 方法获取满足特定条件的多个模型实例
books = Book.objects.filter(author='Eric Matthes')

# 4.2 使用 exclude() 方法获取不满足特定条件的多个模型实例
books = Book.objects.exclude(author='Eric Matthes')

# 4.3 使用 order_by() 方法按照指定的字段排序查询多个模型实例，默认为升序
books = Book.objects.order_by('-publish_date')

# 4.4 使用 values() 或者 values_list() 方法返回特定字段的字典或者元组列表
books = Book.objects.values('title', 'author')
books = Book.objects.values_list('title', 'author')

# 4.5 使用 select_related() 或者 prefetch_related() 方法优化查询性能
# 使用 select_related() 方法可以在查询时一次性获取关联对象的数据，减少 SQL 查询次数
books = Book.objects.select_related('publisher').filter(author='Eric Matthes')

# 使用 prefetch_related() 方法可以预先获取相关对象的数据，避免每次访问时都执行额外的数据库查询
books = Book.objects.prefetch_related('authors').filter(publish_date__year=2019)

# 4.6 多表查询
# 可以通过 ForeignKey、ManyToManyField 等字段进行跨表查询，例如：
books = Book.objects.filter(publisher__name='O\'Reilly Media')  # 获取所有 O'Reilly Media 出版的书籍
books = Book.objects.filter(authors__name='Eric Matthes')  # 获取所有由 Eric Matthes 所著作的书籍

# 还可以使用 Q 对象实现复杂的查询逻辑，例如：
from django.db.models import Q

query = Q(title__icontains='Python') | Q(author__icontains='Eric Matthes')
books = Book.objects.filter(query)  # 获取标题中包含 Python 或者作者名中包含 Eric Matthes 的书籍

# 4.7 聚合查询
from django.db.models import Max, Min, Count, Sum, Avg

publishers_count = Publisher.objects.count()  # 查询 Publisher 表的数据总数
books_count = Book.objects.filter(publisher__name='O\'Reilly Media').count()  # 查询 O'Reilly Media 出版的书籍总数
max_price = Book.objects.aggregate(Max('price'))['price__max']  # 查询价格最高的书籍的价格
min_price = Book.objects.aggregate(Min('price'))['price__min']  # 查询价格最低的书籍的价格
total_pages = Book.objects.aggregate(Sum('pages'))['pages__sum']  # 查询所有书籍的总页数
avg_price = Book.objects.aggregate(Avg('price'))['price__avg']  # 查询所有书
```

```python
#实例
from books.models import Book
import datetime

data = [
    {
        "title": "Python编程入门",
        "author": "John Smith",
        "description": "一本介绍Python编程的书籍",
        "genre": "CS",
        "publish_date": datetime.date(2020, 1, 1)
    },
    {
        "title": "Django Web开发",
        "author": "Jane Doe",
        "description": "一本介绍Django框架的书籍",
        "genre": "CS",
        "publish_date": datetime.date(2019, 1, 1)
    }
]

for book_data in data:
    book = Book(**book_data)
    book.save()
```

在这个例子中，我们创建了一个 Book 类，并定义了 title、author、description 和 publish_date 四个字段。**str**() 方法用于在控制台中显示该模型的字符串表示形式。

# 5迁移数据库

执行以下命令将模型迁移到数据库中：

```python
Copy Code
python manage.py makemigrations
python manage.py migrate

##
python manage.py createsuperuser 
#按提示完成
```

第一条命令会生成迁移文件，第二条命令会将迁移文件应用到数据库中。如果您对 Django 的数据库迁移机制不熟悉，可以阅读 Django 官方文档进行学习和了解

# 6配置DRF

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'myapi',
    'rest_framework',
]
```

# 7重新迁移下数据库,因为添加了应用

```
python manage.py makemigrations
python manage.py migrate
```

# 8查django*版本及*DRF版本

```
>python -V
Python 3.8.8

python -m django --version
3.2.4

pip freeze | findstr djangorestframework
djangorestframework==3.12.4
```

------

# 9导入一些myapi的一些基本数据

```python
from myapi.models import Book
import datetime

data = [
    {
        "title": "红楼梦",
        "author": "曹雪芹",
        "description": "一部中国古典小说",
        "genre": "NV",
        "publish_date": datetime.date(1791, 1, 1)
    },
    {
        "title": "西游记",
        "author": "吴承恩",
        "description": "一部神话小说",
        "genre": "NV",
        "publish_date": datetime.date(1592, 1, 1)
    },
    {
        "title": "水浒传",
        "author": "施耐庵",
        "description": "一部英雄志小说",
        "genre": "NV",
        "publish_date": datetime.date(1368, 1, 1)
    },
    {
        "title": "资治通鉴",
        "author": "司马光",
        "description": "一部历史著作",
        "genre": "HI",
        "publish_date": datetime.date(1084, 1, 1)
    },
    {
        "title": "明朝那些事儿",
        "author": "当年明月",
        "description": "描述明朝历史事件的书籍",
        "genre": "HI",
        "publish_date": datetime.date(2006, 8, 1)
    },
    {
        "title": "毛泽东传",
        "author": "斯诺",
        "description": "详细介绍毛泽东生平的传记",
        "genre": "BG",
        "publish_date": datetime.date(1960, 1, 1)
    },
    {
        "title": "乔布斯传",
        "author": "沃尔特·艾萨克森",
        "description": "描写苹果公司创始人乔布斯生平的传记",
        "genre": "BG",
        "publish_date": datetime.date(2011, 10, 24)
    },
    {
        "title": "福尔摩斯探案集",
        "author": "阿瑟·柯南道尔",
        "description": "一部侦探小说集",
        "genre": "NV",
        "publish_date": datetime.date(1892, 1, 1)
    },
    {
        "title": "1984",
        "author": "乔治·奥威尔",
        "description": "一部反乌托邦小说",
        "genre": "TH",
        "publish_date": datetime.date(1949, 6, 8)
    },
    {
        "title": "尘埃落定",
        "author": "余华",
        "description": "描写人性的惊悚小说",
        "genre": "TH",
        "publish_date": datetime.date(2018, 2, 1)
    }
]

for book_data in data:
    book = Book.objects.create(**book_data)
    book.save()
```

------

# 10 创建一个serializer来序列化模型数据

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

# 11 授权

### 1 在`settings.py`文件中添加如下代码：

```python
pythonCopy CodeINSTALLED_APPS = [
    # 其他应用
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

该配置将会启用TokenAuthentication，并将其设置为默认的身份验证类。

### 2 运行以下命令，在数据库中生成Token表：

```python
Copy Code
python manage.py migrate
```

### 3 手动创建一个用户并为其生成Token：

```python
pythonCopy Code
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.create_user('username', password='password')
token = Token.objects.create(user=user)
print(token.key)
```

### 4在请求中添加Token：

在每次请求时，需要在请求头中添加Authorization字段，值为`Token <token>`，其中`<token>`为刚才生成的token值。

例如，使用curl进行GET请求：`curl -H "Authorization: Token <token>" http://localhost:8000/api/endpoint/`

以上是使用DRF自带的TokenAuthentication实现DRF后台认证的基本步骤，你可以根据实际需求进行相应的修改和优化。

```

import requests

url = 'http://127.0.0.1:9000/api/books/'
headers = {'Authorization': 'Token 89ed43be846c72e393877b7a044dd263de9f5fe2'}

response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == requests.codes.ok:
    # 处理响应数据
    data = response.json()
    print(data)
else:
    print('请求失败，状态码为：', response.status_code)
 
 结果:
 [{'id': 1, 'title': '红楼梦', 'author': '曹雪芹', 'description': '一部中国古典小说', 'genre': 'NV', 'publish_date': '1791-01-01'}, {'id': 2, 'title': '西游记', 'author': '吴承恩', 'description': '一部神话小说', 'genre': 'NV', 'publish_date': '1592-01-01'}, {'id': 3, 'title': '水浒传', 'author': '施耐庵', 'description': '一部英雄志小说', 'genre': 'NV', 'publish_date': '1368-01-01'}, {'id': 4, 'title': '资治通鉴', 'author': '司马光', 'description': '一部历史著作', 'genre': 'HI', 'publish_date': '1084-01-01'}, {'id': 5, 'title': '明朝那些事儿', 'author': '当年明月', 'description': '描述明朝历史事件的书籍', 'genre': 'HI', 'publish_date': '2006-08-01'}, {'id': 6, 'title': '毛泽东传', 'author': '斯诺', 'description': '详细介绍毛泽东生平的传记', 'genre': 'BG', 'publish_date': '1960-01-01'}, {'id': 7, 'title': '乔布斯传', 'author': '沃尔特·艾萨克森', 'description': '描写苹果公司创始人乔布斯生平的传记', 'genre': 'BG', 'publish_date': '2011-10-24'}, {'id': 8, 'title': '福尔摩斯探案集', 'author': '阿瑟·柯南道尔', 'description': '一部侦探小说集', 'genre': 'NV', 'publish_date': '1892-01-01'}, {'id': 9, 'title': '1984', 'author': '乔治·奥威尔', 'description': '一部反乌托邦小说', 'genre': 'TH', 'publish_date': '1949-06-08'}, {'id': 10, 'title': '尘埃落定', 'author': '余华', 'description': '描写人性的惊悚小说', 'genre': 'TH', 'publish_date': '2018-02-01'}, {'id': 11, 'title': '大话西游', 'author': '周星星', 'description': '讲述周星星的日子', 'genre': 'HI', 'publish_date': '2023-04-23'}, {'id': 12, 'title': '大话西游', 'author': '周星星', 'description': '讲述周星星的日子', 'genre': 'HI', 'publish_date': '2023-04-23'}, {'id': 13, 'title': '大话西游', 'author': '周星星', 'description': '122', 'genre': 'NV', 'publish_date': '2023-04-22'}]
[Finished in 0.9s]
```

# 12附一个jwt的例子

提供使用 `django-rest-framework-simplejwt` 库来实现 Token 过期功能的例子。

### 1首先，你需要安装该库：

```
Copy Codepip install djangorestframework_simplejwt
```

### 2然后，在 Django 的配置文件中进行相应的配置：

```
pythonCopy CodeREST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

这段代码会让 Django REST Framework 在处理请求时使用 `JWTAuthentication` 来进行身份验证，同时设置 Access Token 的过期时间为 30 分钟，Refresh Token 的过期时间为 1 天。你可以根据自己的需求调整这些时间。

### 3接下来，你需要在视图函数中使用 JWT 来生成 Token，并返回给客户端。

具体来说，你可以使用 `jwt_encode_handler` 函数和 `jwt_payload_handler` 函数来生成 Token 和 Payload：

```
pythonCopy Codefrom rest_framework_simplejwt.tokens import jwt_encode_handler, jwt_payload_handler
from django.contrib.auth.models import User
from django.http import JsonResponse

def get_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.get(username=username)
    if user.check_password(password):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Invalid credentials'})
```

### 4最后，在 API 视图函数中使用 `JWTAuthentication` 进行身份验证即可。

这个过程会自动检查 Token 是否过期，如果过期则返回错误响应。

需要注意的是，`django-rest-framework-simplejwt` 库提供了许多其他有用的功能，例如支持 Refresh Token、Blacklist Token 等。你可以查阅其官方文档以获取更多信息和使用示例。



# 13附一个路由

帮我列列，这样的代码最终生成的路由：

router.register(r'users', UserViewSet)    

path('setuser/', include(router.urls)),

使用 `router.register(r'users', UserViewSet)` 后，`UserViewSet` 中默认提供了以下 URL：

- `GET /users/`：获取所有用户的列表
- `POST /users/`：创建一个新用户

以及以下单个用户 URL：

- `GET /users/{pk}/`：获取特定用户信息
- `PUT /users/{pk}/`：更新特定用户信息
- `PATCH /users/{pk}/`：更新特定用户信息（部分更新）
- `DELETE /users/{pk}/`：删除特定用户

这些 URL 将由 Django REST framework 的路由器自动生成，并附加到 `/setuser/` 路径上。具体来说，它们是：

- `GET /setuser/users/`
- `POST /setuser/users/`
- `GET /setuser/users/{pk}/`
- `PUT /setuser/users/{pk}/`
- `PATCH /setuser/users/{pk}/`
- `DELETE /setuser/users/{pk}/`

# 14一个大坑

如果使用 Postman 的 x-www-form-urlencoded 格式进行 POST 请求可以成功，而使用 JSON 格式时不行，那么很可能是后端代码不能正确地解析 JSON 数据。

根据您提供的 Django 后端代码中的 *<h5>request.POST.get() 方法，它只能解析 x-www-form-urlencoded 格式的数据，而无法处理 JSON 格式的数据*<h5/>。因此，当您在请求正文中传递了一个 JSON 对象时，Django 会无法通过 request.POST.get() 方法获取您想要的数据。

您需要使用以下两行代码来获取 POST 请求中的 JSON 数据：

```
复制代码json_data = json.loads(request.body)
username = json_data.get('username', '')
password = json_data.get('password', '')
```

这里，我们首先使用 json.loads() 函数将请求正文中的 JSON 数据转换为 Python 中的字典类型，然后通过 get() 方法来获取其中的 username 和 password 属性值。

请尝试修改您的后端代码，并使用 Postman 发送 JSON 格式的 POST 请求，看是否能够成功接收并解析 JSON 数据。