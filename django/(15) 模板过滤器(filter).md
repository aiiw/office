**模板过滤器(filter)的作用**

Django模板中的变量是用双括号如{{ variable }}显示的。通过使用模板过滤器(filter)来可以改变变量在模板中的显示形式，比如{{ article.title | lower }} 中lower过滤器可以让文章的标题转化为小写。Django的模板提供了许多内置过滤器，一些常用的过滤器如下。



| **过滤器** | **例子**                                |
| ---------- | --------------------------------------- |
| lower      | {{ article.title \| lower }} 大小写     |
| length     | {{ name \| length }} 长度               |
| default    | {{ value \| default: "0" }} 默认值      |
| date       | {{ pub_date \| date:"Y-m-d" }} 日期格式 |

**
**

**过滤器(filter)的本质和工作原理**

Django模板过滤器(filter)的本质是一个函数，过滤器的名字就是函数名。该函数接收竖线" | "前的变量值(value)**和**冒号" **:** " 后的参数(args)，返回一个值, 其中args可选。比如lower过滤器接收一个字符串，将其全部转化为小写后返回。date过滤器调用strftime方法将DateTime格式的数据转化为指定格式的字符串返回。



我们自定义过滤器本质就是自定义一个名叫my_filter_name(value, args)的函数，用来处理模板中传递过来的变量和参数。在使用自定义过滤器时时我们需要遵循先载入再使用的原则。



**如何自定义模板过滤器**

首先你要在你的app目录下新建一个叫templatetags的文件夹(不能取其它名字), 里面必需包含__init__.py的空文件。在该目录下你还要新建一个python文件专门存放你自定义的过滤器函数，本例中为blog_extras.py，当然你也可以取其它名字。整个目录结构如下所示:

```python
blog/
   __init__.py
   models.py
   templatetags/
       __init__.py
       blog_extras.py
   views.py
```

在模板中使用自定义的过滤器(filter)时，需要先使用{% load blog_extras %}载入自定义的过滤器，然后通过使用{{ variable | my_filter_name }} 使用。



**案例1 - 自定义过滤器显示中文格式日期**

Django自带的过滤器date:"Y-m-d" 可以将日期类型的数据转化为”2018-09-01“。如果使用date:"Y年-m月-d日", 则日期将显示为"2018年-09年-01日", 这显然不是我们想要的。我们现在希望自定义一个名叫chinese_date_format的过滤器，在模板中使用{{ pub_date | chinese_date_format }}即可将博文发布日期转化为“2018年9月1日”显示。



此时我们只需要在blog_extras.py文件中添入如下代码。

```python
from django import template

register = template.Library()


@register.filter
def chinese_date_format(value):
    return "{}年{}月{}日".format(value.year, value.month, value.day)
```



我们从先建立模板的register，然后使用@register.filter过滤器注册我们自定义的过滤器chinese_date_format。在模板中先使用{% load blog_extras %}载入自定义的过滤器，然后在模板中使用{{ article.pub_date | chinese_date_format }} 即可显示中文格式日期了。



但上述代码有个问题，该过滤器只有当value为datetime格式的数据时才会工作。如果用户把它用在一个字符串上则会出现`AttributeError。`我们现在可以对上述代码进行改进，先增加对value格式的判断。当value格式不为datetime时，该过滤器直接返回value本身。

```python
from django import template
import datetime
register = template.Library()


@register.filter
def chinese_date_format(value):
    if isinstance(value, datetime.datetime):
        return "{}年{}月{}日".format(value.year, value.month, value.day)
    else:
        return value
```



**案例2 - 自定义过滤器给标题添加"最新"和"推荐"描述**



案例1中我们只使用了竖线"|"前的变量值作为参数，我们还可以通过冒号**:**给过滤器函数传递更多的参数。我们现在要自定义一个叫add_description的过滤器。当我们在模板中使用{{ article.title | add_description:"最新" }}时，标题后面会加上"最新"字样。当我们在模板中使用{{ article.title | add_description:"最热" }}时，标题后面会加上"最热"字样。



blog_extras.py中代码如下所示。

```python
from django import template
register = template.Library()


@register.filter
def add_description(value, args):
    return "{} ({})".format(value, args)
```

