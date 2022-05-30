**settings.py的默认设定与工作原理**

Django设置文件settings.py包含的选项非常多，但好消息是大部分不需要我们手动去设置。当我们使用django-admin.py startproject xxx命令创建一个Django项目时，你会发现生成的settings.py已经包含了部分基本的默认设定，我们只需要修改和添加我们需要使用的设定就好了。



一个项目完整的全局默认设置在django/conf/global_settings.py文件中。Django在编译时，会先载入global_settings.py中的全局默认配置值，然后加载用户指定的settings文件，重写部分全局默认设置。



下面我们就来看看一些常用设置选项及它们背后的含义。



**BASE_DIR** 

默认值os.path.dirname(os.path.dirname(os.path.abspath(__file__)))。这个是Django项目文件夹所在目录得绝对路径，一般不要修改。

**
**

**DEBUG**

默认值是True。在本地开发测试环境下设置DEBUG=True可以显示bug信息，便于开发者找出代码错误所在。当你在部署项目在生产环境时，请切记设置DEBUG=False。因为生成环境下打开Debug会暴露很多敏感设置信息（比如数据库密码)。注意: 当你设置DEBUG=False, 你一定要设置ALLOWED_HOSTS选项, 否则会抛出异常。



**ALLOWED_HOSTS**

默认值为空[]。设置ALLOWED_HOSTS是为了限定用户请求中的host值，以防止黑客构造包来进行头部攻击。该选项正确设置方式如下:

- DEBUG=True: ALLOWED_HOSTS可以为空，也可设置为['127.0.0.01', 'localhost']
- DEBUG=False: ALLOWED_HOSTS=['46.124.78.xx', 'www.bat.com'，'127.0.0.1']



当你关闭DEBUG时，HOST一般为服务器公网IP或者注册域名。 当你还需要使用子域名时，你可以用'.bat.com'。它将匹配bat.com, www.bat.com和news.bat.com。在正式部署项目时，请尽量不要设置ALLOWED_HOSTS=['*']。



**SECRET_KEY**

SECRET_KEY是Django根据自己算法生成的一大串随机数，本质是个加密盐，用于防止CSRF（Cross-site request forgery）跨站请求伪造攻击。当部署Django项目到生产环境中时，Django文档建议不直接在settings.py里输入字符串，而是采取下面两种方法读取SECRET_KEY。

```
# 方法一: 从环境变量中读取SECRET_KEY
import os
SECRET_KEY = os.environ['SECRET_KEY']

# 方法二: 从服务器上Django项目文件价外的某个文件读取
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
```



**INSTALLED_APPS**

这个设置比较简单，也比较常用，用于增删一个项目(Project)所包含的应用(APP)。只有对列入此项的APP, Django才会生成相应的数据表。

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',  # 自定义的APP
]
```



**AUTH_USER_MODEL**

默认为auth.user。也可以为自定义用户模型。



**STATIC_ROOT和STATIC_URL**

这两个选项是关于静态文件(如CSS, JS,和图片)的最重要的设置，一般设置如下。STATIC_URL是静态文件URL，设置后可以通过使用{% static 'img/xxx.jpg' %}方式直接访问/static/文件夹里的静态文件。如果你设置了STATIC_ROOT, 当你运行"python manage.py collectstatic"命令的时候，Django会将各app下所有名为static的文件夹及其子目录复制收集到STATIC_ROOT。把静态文件集中一起的目的是为了更方便地通过Apache或Nginx部署。



STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



一般情况下我们会尽量把静态文件只放在static文件夹或它的子目录下，所以上述两个设置对于一般项目是够的。那么问题来了，如果你还有一些文件夹中也有静态文件，可是文件夹并不是以static命名也不在static子目录里，此时你也希望搜集使用那些静态文件，你该怎么办呢？这时我们就要设置静态文件目录STATICFILES_DIRS值了。



**STATICFILES_DIRS**

默认值为空。当你设置该选项后，"python manage.py collectstatic"命令会把static文件夹及静态文件目录STATICFILES_DIRS里的静态文件都复制到一份到STATIC_ROOT。比如下例中Django会将下面两个文件夹内容也复制到STATIC_ROOT。注意里面的路径必需是绝对路径哦。



```
STATICFILES_DIRS = [    "/home/user/pictures",
    "/opt/webfiles/myfiles",
]
```





**MEDIA_ROOT和MEDIA_URL**

media文件价一般用于放置用户上传的文件。对于此文件夹的权限设置异常重要，因为用户可能会上传可执行的文件，影响网站和服务器的安全。我们后续会专题介绍文件上传过程中应考虑的安全因素。

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





```
国际化(语言与时间)TIME_ZONE = 'Asia/Shanghai' # 设置时区
USE_I18N = True # 默认为True，是否启用自动翻译系统
USE_L10N = True # 默认False，以本地化格式显示数字和时间
USE_TZ = False  # 默认值True。若使用了本地时间，必须设为False
```





```
邮箱服务配置EMAIL_HOST = 'smtp.qq.com'   # 发送者邮箱服务器
EMAIL_PORT = 25 # 端口
EMAIL_HOST_USER = ''        # 发送者用户名（邮箱地址）
EMAIL_HOST_PASSWORD = ''    # 发送者密码
EMAIL_USE_SSL = TrueDEFAULT_FROM_EMAIL = 'xxx@qq.com'
```





**数据库设置**

当然小编我并不建议在settings.py直接写入数据库密码，而是采取读取外部配置文件的方式，更安全。下面以MYSQL为例介绍了基本配置方式。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'mydb',         # 你要存储数据的库名，事先要创建之
        'USER': 'xxs',         # 数据库用户名
        'PASSWORD': 'xxxx',     # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 数据库使用的端口
    }
}
```

更多阅读: [2019新年第一篇: SQLite的优缺点及Django配置MySQL数据库](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247484200&idx=1&sn=f81da7b856e6b5bd737d675659f17d5e&chksm=a73c6310904bea061a51f1de1c17fabab2c36100c680506e3c34915854c194082233d2aafb45&scene=21#wechat_redirect)



# **缓存设置（CACHE)**

Django中提供了多种缓存方式，如果要使用缓存，需要先在settings.py中进行配置，然后应用。根据缓存介质的不同，你需要设置不同的缓存后台Backend。



Memcached缓存

Memcached是基于内存的缓存，Django原生支持的最快最有效的缓存系统。对于大多数场景，我们推荐使用Memcached，数据缓存在服务器端。使用前需要通过pip安装memcached的插件python-memcached和pylibmc，可以同时支持多个服务器上面的memcached。



下面是使用pyhon-memcached的设置。

```
# localhost
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# unix soket
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}   

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '172.19.26.240:11211',
            '172.19.26.242:11211',
        ]
        # 我们也可以给缓存机器加权重，权重高的承担更多的请求，如下
        'LOCATION': [
            ('172.19.26.240:11211',5),
            ('172.19.26.242:11211',1),
        ]
    }
 }
```



数据库缓存

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
```



文件系统缓存

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',#这个是文件夹的路径
        #'LOCATION': 'c:\foo\bar',#windows下的示例
    }
}
```



本地内存缓存

```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}
```

阅读更多: [Django基础(8): 缓存Cache应用场景及工作原理，Cache设置及如何使用](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483914&idx=1&sn=368657c4efc342d7d8e26a23f8209eb0&chksm=a73c6232904beb249bd3705fdd09176b97fac5f49f152f846d5d10a3dac34e9ae88614f4e43d&scene=21#wechat_redirect)



```
中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```



**COOKIE与SESSION设置**



SESSION_ENGINE = 'django.contrib.sessions.backends.db' # 引擎（默认）

SESSION_COOKIE_NAME = "sessionid" # Session的cookie保存在浏览器上时的key，

SESSION_COOKIE_PATH = "/" # Session的cookie保存的路径（默认）

SESSION_COOKIE_DOMAIN = None # Session的cookie保存的域名（默认）

SESSION_COOKIE_SECURE = False # 是否Https传输cookie（默认）

SESSION_COOKIE_HTTPONLY = True # 是否Session的cookie只支持http传输（默认）

SESSION_COOKIE_AGE = 60 * 30 # Session的cookie失效日期（30min）（默认）

SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 是否关闭浏览器使得Session过期（默认）

SESSION_SAVE_EVERY_REQUEST = True # 是否每次请求都保存Session，默认修改之后才保存