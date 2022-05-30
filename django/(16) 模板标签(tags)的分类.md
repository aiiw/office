**什么是模板标签(tags)**

模板标签都是放在{% %}括号里的，常见的模板标签有{% load xxxx %}, {% block xxxx %}, {% if xxx %}, {% url 'xxxx' %}。这些模板标签的本质也是函数，标签名一般即为函数名。这些标签的主要作用包括载入代码渲染模板或对传递过来的参数进行一定的逻辑判断或计算后返回。



比如下例中的url标签接收两个参数，一是命名的url, 一个是文章id，将其进行反向解析，生成一个类似blog/article/4/的链接。

```html
<a href="{% url 'blog:article_detail' article.id  %}">详情</a>
```



***\*Django模板标签(tags)的分类\****

Django的模板标签（tag)一共分2类：

- simple_tag (简单标签 : 处理数据，返回一个字符串或者给context设置或添加变量。
- inclusion_tag (包含标签) : 处理数据，返回一个渲染过的模板。



熟悉Django的都知道，我们一般在视图view里设置context，然后通过它来传递数据给模板。 一个context是一系列变量和它们值的集合。通过使用simple_tag, 我们可以在视图外给context设置或添加变量。注: Django 1.9以后不再支持assignment_tag了，均使用simple_tag。



**如何自定义模板标签**

首先你要在你的app目录下新建一个叫templatetags的文件夹(不能取其它名字), 里面必需包含__init__.py的空文件。在该目录下你还要新建一个python文件专门存放你自定义的模板标签函数，本例中为blog_extras.py，当然你也可以取其它名字。整个目录结构如下所示:

```
blog/
   __init__.py
   models.py
   templatetags/
       __init__.py
       blog_extras.py
   views.py
```

在模板中使用自定义的模板标签时，需要先使用{% load blog_extras %}载入自定义的过滤器，然后通过{% tag_name %} 使用它。



**自定义模板标签的3个简单例子**

我们将定义3个简单模板标签，一个返回string, 一个给模板context传递变量，一个显示渲染过的模板。我们在blog_extra.py里添加下面代码。



\#blog_extra.py

```python
from django import template
import datetime
from blog.models import Article

register = template.Library()

# use simple tag to show string
@register.simple_tag
def total_articles():
    return Article.objects.filter(status='p').count()

# use simple tag to set context variable
@register.simple_tag
def get_first_article():
    return Article.objects.filter(status='p').order_by('-pub_date')[0]

# show rendered template
@register.inclusion_tag('blog/latest_article_list.html')
def show_latest_articles(count=5):
    latest_articles = Article.objects.filter(status='p').order_by('-pub_date')[:count]
    return {'latest_articles': latest_articles, }
```

\# latest_article_list.html

```html
<ul>
{% for article in latest_articles %}
<li>{{ article.title }} </li>
{% endfor %}
</ul>
```

\# index.html (使用我们自定义的模板标签)

```html
{% extends "blog/base.html" %}
{% load blog_extras %}

{% block content %}

<p>文章数: {% total_articles %}</p>
{% show_latest_articles %}

{% get_first_article as first_article %}
<p>第一篇文章: </p>
<p>{{ first_article.title }}</p>

{% endblock %}
```

最后展示效果图如下所示:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAA5uvryh4XV8JtjXj8CG1qGsz6tegWPnh3zrSbbhTyxUHM2yc2BoIy1k7M3k1ibVXmmT2xyicvSOwQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**
**

**一个复杂的例子: 从模板或context接收参数后返回结果**

上述3个简单例子的信息传递都是单向的，更常见的情况是标签函数接收从模板或context传递过来的参数，处理后再返回字符串或渲染过的模板。



下例中show_results标签需要接收模板传递的poll这个参数，才能返回poll结果。

```
{% show_results poll %}
```

这时我们可以这样写show_results函数。

```python
@register.inclusion_tag('results.html')
def show_results(poll):
    choices = poll.choice_set.all()
    return {'choices': choices}
```

当然poll这个变量出现在模板中并不是必需的，很多时候一个对象或一个对象清单已经存在全局变量context里，我们可以使用takes_context=True来直接使用context里的变量。假设poll已经存在context里，我们上面代码可以改为:

```python
@register.inclusion_tag('results.html', takes_context=True)
def show_results(context):
    choices = context['poll'].choice_set.all()
    return {'choices': choices}
```

此时模板可以简化为如下代码，不再需要poll这个参数，即可显示poll的结果。

```
{% show_results %}
```



**如何处理从模板中传递过来的多个参数**

{% show_results poll %}中我们自定义的标签函数只接收了从模板传递过来的一个poll参数。一个模板也可以传递多个参数，如果参数名字或数量已知，Django的tag函数是可以按位置处理传递过来的参数的。

```python
{% my_tag "abcd" book.title warning=message profile=user.profile %}

@register.inclusion_tag('my_template.html')
def my_tag(a, b, *args, **kwargs):
    warning = kwargs['warning']
    profile = kwargs['profile']
    ...
    return ...
```



但类似{% url "article_detail" article.id article.slug %}中的url标签显然要复杂得多。它可以接收未知数量的参数和未知名字的参数, 而且参数中有的带双引号，有的不带双引号。

对于这种情况Django的做法是先对标签所在的节点进行解析(parser), 把接收过来的字符串整体作为一个token，先对token进行split拆分，然后再分别处理。



我们现在来看看{% format_time %}这个标签是如何时间日期的格式化的。

```
<p>Published at at {% format_time article.pub_date "%Y-%m-%d %I:%M %p" %}.</p>
```



自定义的format_time标签函数完整代码如下。

```python
from django import template

register = template.Library()

@register.tag(name="format_time")
def do_format_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, date_to_be_formatted, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly two arguments" % token.contents.split()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return FormatTimeNode(date_to_be_formatted, format_string[1:-1])


class FormatTimeNode(template.Node):
    def __init__(self, date_to_be_formatted, format_string):
        self.date_to_be_formatted = template.Variable(date_to_be_formatted)
        self.format_string = format_string

    def render(self, context):
        try:
            actual_date = self.date_to_be_formatted.resolve(context)
            return actual_date.strftime(self.format_string)
        except template.VariableDoesNotExist:
            return ''
```

我们现在来着重看下上面这段代码是如何工作的。

- Django模板解析器扫描整个模板，碰到了format_time这个标签，把其当作一个新的节点Node，获取了format_time article.pub_date "%Y-%m-%d" 这一长串字符串作为token
- get_format_time方法利用token自带的split_contents方法把上述字符串拆分成三部分: 标签名(tag_name), 需要格式化的日期(date)和指定格式(format), 并返回需要格式化的日期和格式交由FormatTimeNode处理。format_string[1:-1]的作用是去掉双引号。
- FormatTimeNode这个节点类负责渲染节点，通过render方法渲染新的节点，还可以通过context给模板传递其它的变量（如下所示)。当render方法不返回一个具体的值的时候，需要返回一个空字符串。

```python
def render(self, context):
    actual_date = self.date_to_be_formatted.resolve(context)
    context['formatted_time'] = actual_date.strftime(self.format_string)
    return ''
    
```



**利用parse方法连续解析**

有时你还会碰到{% comment %}和{% endcomment %}这样的标签。这时你就需要利用parse方法解析真个nodelist了。这个非常复杂，以后分析Django源码时会再做讲解。