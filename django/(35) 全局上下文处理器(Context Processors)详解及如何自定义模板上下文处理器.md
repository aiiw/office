**什么情况下需要使用全局上下文处理器(Context Processors)？**

当你需要向所有模板传递一个可以被全局使用的变量时。在编写Django视图函数时，我们一般会在视图函数中以Python字典(dict)形式向模板中传递需要被调用或使用的变量并指定渲染模板。通常情况下，我们向模板的传递的字典变量与模板是一一对应的关系。有时我们还需要向模板传递全局变量，即每个模板都需要使用到的变量(比如站点名称, 博客的最新文章列表)。如果每个视图函数分别去查询数据库，然后向每个模板传递这些变量，不仅造成代码冗余，而且会造成对数据库的重复查询。**一个更好的解决方案就是使用自定义的上下文处理器(Context Processors)给模板传递全局变量，一次查询全局使用，完美解决了这些问题**。



**Django内置的全局上下文处理器(Context Processors)**

你或许没有自定义过自己的全局上下文处理器(Context Processors)，但你一定使用过Django内置的全局上下文处理器(Context Processors)。举个例子，虽然你没有向某个模板中传递过权限perms对象，你却可以在所有模板中随时调用它（如下所示)。**同样可以在模板中全局使用的变量还有request和user对象。**

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoBvu4DIvTeEHicry9rWbJpsJcoILzia3XibaJM64hym1SRicsqibf0PicunJqoMFJZ6PjHJyuOF2koBQicvQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

为什么？因为Django的settings.py里已经包含了django.template.context_processors.request和django.contrib.auth.context_processors.auth这两个全局上下文处理器。如果你把他们移除， 看看还能不能在模板中调用 {{ user }}和{{ perms }}?



```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ # 以下包含了4个默认的全局上下文处理器
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myapp.custom_context_processors.xxx',  # 自定义全局上下文处理器# 自定义全局上下文处理器# 自定义全局上下文处理器# 自定义
            ],
        },
    },
]
```



Django一般包含了上述4个默认全局上下文处理器，它们作用如下所示：

- #### django.template.context_processors.debug：在模板里面可以直接使用settings的DEBUG参数以及强大的sql_queries:它本身是一个字典，其中包括当前页面执行SQL查询所需的时间

- #### django.template.context_processors.request：在模板中可以直接使用request对象

  #### django.contrib.auth.context_processors.auth：在模板里面可以直接使用user，perms对象。

- #### django.contrib.messages.context_processors.messages：在模板里面可以直接使用message对象。

####  

另外Django还提供了几个全局上下文处理器：

- #### django.template.context_processors.i18n：在模板里面可以直接使用settings的LANGUAGES和LANGUAGE_CODE

- #### django.template.context_processors.media：可以在模板里面使用settings的MEDIA_URL参数

- #### django.template.context_processors.csrf : 给模板标签 {% csrf_token %}提供token值，默认总是开启。

- #### django.template.context_processors.tz: 可以在模板里面使用 TIME_ZONE参数。

#### 



**如何自定义全局上下文处理器**

**自定义的全局上下文处理器本质上是个函数，使用它必须满足3个条件：**

**1. 传入参数必须有request对象 **

**2.返回值必须是个字典 **

**3, 使用前需要在settings的context_processors里申明。**

**我们通常会把自定义的上下文处理器函数放在单独命名的context_processors.py里，这个python文件可以放在project目录下，也可以放在某个app的目录下。**



接下来我们来看一个具体例子。我们需要向所有模板传递一个叫site_name的全局变量以便在所有模板中直接使用 {{ site_name }}输出站点名称，我们可以在blog(应用名)的目录下新建context_processors.py，新增如下代码：



*# blog/context_processors.py*

```python
from django.conf import settings
def global_site_name(request):
    return {'site_name': settings.SITE_NAME,}
```

然后可以在settings.py里声明：

```python
'context_processors': [ # 以下包含了4个默认的全局上下文处理器
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
'blog.context_processors.global_site_name',  # 自定义全局上下文处理器
]
```

**注意模板中全局变量与本地变量的优先级**

全局上下文处理器提供的变量优先级高于单个视图函数给单个模板传递的变量。这意味着全局上下文处理器提供的变量可能会覆盖你视图函数中自定义的本地变量，因此请注意避免本地变量名与全局上下文处理器提供的变量名称重复。这些变量名包括perms, user和debug等等。



如果你希望单个视图函数定义的变量名覆盖全局变量，请使用以下强制模式：

```python
from django.template import RequestContext
high_priority_context = RequestContext(request)
high_priority_context.push({"my_name": "Adrian"})
```