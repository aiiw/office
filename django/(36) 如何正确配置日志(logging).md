# (36): 如何正确配置日志(logging)

**日志基础知识**

日志与我们的软件程序密不可分。它记录了程序的运行情况，可以给我们调试程序和故障排查提供非常有用的信息。每一条日志信息记录了一个事件的发生。具体而言，它包括了：

- 事件发生时间
- 事件发生位置
- 事件的严重程度--日志级别
- 事件内容



日志的级别又分为：

- DEBUG：用于调试目的的低级系统信息
- INFO：一般系统信息
- WARNING：描述已发生的小问题的信息。
- ERROR：描述已发生的主要问题的信息。
- CRITICAL：描述已发生的严重问题的信息。



在Django项目中，我们可以针对日志的不同级别设置不同的处理方式。比如INFO级别及以上的日志我们写入到log文件里保存，Error级别及以上的日志我们直接通过邮件发送给系统管理员。



**Django的日志模块**

Django的日志模块其实就是python的logging模块。它由4部分组成：

- Logger 记录仪：生成和记录每条日志信息及级别
- Handler处理程序: 根据日志信息级别交由相应处理程序处理（比如生成文件或发送邮件）
- Filters 过滤器：日志交由处理程序处理前需要满足的过滤条件(比如Debug=True或False)
- Formaters 格式化程序：决定每条日志的打印输出格式，可以有完整版的，也有简单版的

一个logger记录仪的例子如下所示。当程序运行出现错误时，它生成了一条级别为error的日志信息。这条记录产生后就会交由Handler处理。

```python

# import the logging library
import logging
# 获得logger实例
logger = logging.getLogger(__name__)
def my_view(request, arg1, arg):
    ...
    if error_happens:
        # Log an error message
        logger.error('Something went wrong!')
```

当Debug=True时，日志信息默认在console输出。现在我们还需要在django配置文件里配置日志(logging)相关内容，使得当Debug=False时，日志信息会输出到日志文件里或发送给系统管理员。



**settings.py推荐日志配置信息**

以下基本配置信息在django cookiecutter推荐使用的logging配置信息上做了修改，可适合大部分项目使用。如果真的希望发送和接收到邮件还需在settings.py正确配置电子邮箱Email。

```python
# 给ADMINS发送邮件需要配置
ADMINS = (
 ('admin_name','your@gmail.com'),
)
MANAGERS = ADMINS
# 创建log文件的文件夹
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 基本配置，可以复用的
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": { # 定义了两种日志格式
        "verbose": { # 标准
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
        'simple': { # 简单
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
    },
    "handlers": { # 定义了三种日志处理方式
        "mail_admins": { # 只有debug=False且Error级别以上发邮件给admin
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        'file': { # Info级别以上保存到日志文件
            'level': 'INFO', 
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
            'filename': os.path.join(LOG_DIR,"info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 10,  # 日志大小 10M
            'backupCount': 2,  # 备份数为 2
            'formatter': 'simple', # 简单格式
            'encoding': 'utf-8',
        },
        "console": { # 打印到终端console
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": { # Django的request发生error会自动记录
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,  # 向不向更高级别的logger传递
        },
        "django.security.DisallowedHost": { # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}
```

