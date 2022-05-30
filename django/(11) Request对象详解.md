**个极简的包含request的视图函数**

下面是一个极简的Django视图函数代码，用于显示hello world。你会注意到request是灰色的。这是因为index函数包含了request这个变量，然而你却没有使用它。



\# views.py

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")
```

\# urls.py

```python
from django.urls import re_path
from . import views

app_name = "request_demo"
urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
]
```

因为我们本例中不需要使用数据库，所以不需要创建模型(models)。当你访问http://127.0.0.1:8000/index/你就应该能看到hello world字样。



现在我们将视图函数稍微改下，使用request变量打印出请求路径。

```python
# views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("请求路径:{}" .format(request.path))
```

再次访问/index/页面，刷新浏览器，这时你会看到:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAorrKcDhYmrF0kRpFWzt56icyVSq7tAvQ6pLWP3laWjwvUyQwSiat3zggWJicjTA0icKKKG1ACR0sAgw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**Request对象方法和属性**

Request对象包括了如下属性和方法。

- **`request.method``：`获取请求方法(e.g. `GET`, `POST`).**
- **`request.GET` or `request.POST``：`获取GET or POST请求参数，字典形式。**
- **`request.POST.get('name',default=None)``：`获取POST请求参数**
- **`request.GET.getlist('name',default=None)``: `获取GET参数列表**
- **`request.META``:`包含当前HTTP请求的Headers头部信息, 字典形式。键值KEY都是大写。比如`request.META['REMOTE_ADDR']`可获取用户远程IP地址。**
- **`request.user``：`获取当前访问用户的所有信息。**
- **`request.path``：`获取当前访问路径。**



**常用request.META属性**

request.META 是一个Python字典，包含了所有本次HTTP请求的Header信息，常用属性包括:

- REQUEST_METHOD: 当前请求方法, GET或POST
- HTTP_USER_AGENT: 用户浏览器的字符串, 比如Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36。注意
- REMOTE_ADDR: 客户端IP地址，比如54.489.102.201 。
- PATH_INFO: 当前路径信息，如"/index", 等同于request.path



注意有些用户的User Agent的字符串获取不了，所以使用python的get方法request.META.get('HTTP_USER_AGENT', 'unknown') 要好于request.META['HTTP_USER_AGENT']，防止抛出错误异常。



**打印出所有request.META所有属性**

如果你想了解当前请求request对象的所有属性，我们可以写一个简单的view函数来显示 request.META 的所有信息。代码如下所示:

```python
# Create your views here.
from django.http import HttpResponse


def index(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
```

输出结果是这样的:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAorrKcDhYmrF0kRpFWzt56O4K9kAVzNZ4oYqibkmrdfSDLJgrSBUrQG8GKibcBM0ay63bIwt4UafSA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**开发显示用户名，用户IP地址和浏览器的APP**

我们现在来正式利用request对象来开发一个叫request_demo的app，用来显示当前访问用户是谁，用户的IP地址及其所使用的浏览器。代码如下:



\# urls.py

```python
from django.urls import re_path
from . import views

app_name = "request_demo"
urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
]
```



\# views.py

```python
from django.shortcuts import render


def index(request):
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    ip = request.META['REMOTE_ADDR']

    context = {'user': user, 'user_agent': user_agent, 'ip': ip, }

    return render(request, "request_demo/index.html", context)
```



\# request_demo/index.html

```python
{% block content %}
<h3>Simple Django APP</h3>
<ul>
    <li>User: {{ user }}</li>
    <li>User_Agent: {{ user_agent }}</li>
    <li>IP Address: {{ ip }}</li>
</ul>
{% endblock %}
```

访问/index/展示效果如下图所示。如果你已登录就会显示具体的登录用户的用户名。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAorrKcDhYmrF0kRpFWzt56HvR4jibxZiblMdHfNxjACUic66OhuRwvdnF3AxoFIVugsgaAibZ35CaeiaQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**获取远程用户的真实IP地址**

一般情况下request.META['REMOTE_ADDR']足以获取用户真实IP地址。对于部署在负载平衡proxy(如nginx)上Django应用而言，这种方法将不适用。因为每个request中的远程IP地址(request.META["REMOTE_IP"])将指向该负载平衡proxy的地址，而不是发起这个request的用户的实际IP。负载平衡proxy处理这个问题的方法在特殊的 X-Forwarded-For 中设置实际发起请求的IP。 因此，需要一个中间件来确保运行在proxy之后的站点也能在request.META['REMOTE_ADDR']中得到正确的IP。



解决办法如下:

\1. 在settings.py中需要添加如下这个中间件（即middleware）：

django.middleware.http.SetRemoteAddrFromForwardedFor

\2. 视图views.py改为:

```python
from django.shortcuts import render


def index(request):
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip

    context = {'user': user, 'user_agent': user_agent, 'ip': ip, }

    return render(request, "request_demo/index.html", context)
```

本例中，我们没用nginx代理，所以显示的ip地址依然是127.0.0.1。