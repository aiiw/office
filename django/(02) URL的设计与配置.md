Django网络应用开发的**5项基础核心技术**包括[模型（Model）的设计](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483679&idx=2&sn=9e3db4167e408a2a0c3a1037c4f7266a&chksm=a73c6127904be831aee7abe13980fbea5e2d611ceb48e346dc0fc083c0a8725b52ebb3b8106f&scene=21#wechat_redirect)，URL的设计与配置，View（视图）的编写，Template（模板）的设计和Form(表单)的使用。今天小编我就来给你来介绍下第二项Django核心基础知识之URL的设计与配置吧。想持续了解后续Django Web开发技术请订阅我的公众号【**Python与Django大咖之路**】。



**Django的URL是如何工作的**

**
**

URL通常与视图(View）一起工作的。服务器收到用户请求后，会根据urls.py里的关系条目，去视图View里查找到与请求对应的处理方法，从而返回给客户端http页面数据。这和其它web开发的路由机制(Router）是一个道理。如果你还不知道视图是什么，那么你只需要记住：视图收到用户的请求后，展示给用户看得见的东西。



我们来看看下面一个新闻博客的例子:



```
# blog/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.index),
      path('blog/article/<int:id>/', views.article),
]

# blog/views.py
def index(request):
    # 展示所有文章
    
def article(request, id):
    # 展示某篇具体文章
```



那么这段代码是如何工作的？

- 当用户在浏览器输入/blog/时，URL收到请求后会调用视图views.py里的index方法，展示所有文章。
- 当用户在浏览器输入/blog/article/<int:id>/时，URL不仅调用了views.py里的article方法，而且还把参数文章id通过<>括号的形式传递给了视图。int这里代表只传递整数，传递的参数名字是id。



注意当你配置URL时，别忘了把你的app（比如blog）urls加入项目的URL配置里(mysite/urls.py), 如下图所示:



```
from django.conf.urls import url, include

urlpatterns = [
    url(r'^/', include('blog.urls')),
] 
```



**Django URL传递参数的方法path和_re_path**



写个URL很简单，但如何通过URL把参数传递给给视图view是个技术活。Django URL提供了两种匹配方式传递参数: path和re_path。path是正常参数传递，re_path是采用正则表达式regex匹配。path和re_path传递参数方式如下:



- path方法：采用双尖括号<变量类型:变量名>或<变量名>传递，例如<int:id>, <slug:slug>或<username>。
- re_path方法: 采用命名组(?P<变量名>表达式)的方式传递参数。



下图两种传递文章id给视图函数的方式是一样的。re_path里引号前面的小写r表示引号里为正则表达式, 请忽略'\'不要转义，^代表开头，$代表以结尾，\d+代表正整数。

```
# blog/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('blog/article/<int:id>/', views.article, name = 'article'),
   re_path(r'^blog/article/(?P<id>\d+)/$', views.article, name='article'),
]

# View (in blog/views.py)

def article(request, id):
    # 展示某篇文章
```



**URL的命名及reverse()方法**



你注意到没？我们在上述代码中还给URL取了一个名字 'article'。这个名字大有用处，相当于给URL取了个全局变量的名字。它可以让你能够在Django的任意处，尤其是模板内显式地引用它。假设你需要在模板中通过链接指向一篇具体文章，下面那种方式更好？

```
方法1: 使用命名URL
<a href="{% url 'article' id %}">Article</a>

方法2: 使用常规URL - 不建议
<a href="blog/article/id">Article</a>
```



如果你还没意识到方法1的好处，那么想想吧，假设你需要把全部模板链接由blog/article/id改为blog/articles/id, 那种方法更快？改所有模板，还是改URL配置里的一个字母?



可惜的是命名的URL一般只在模板里使用，不能直接在视图里使用。如果我们有了命名的URL，我们如何把它转化成常规的URL在视图里使用呢？Django提供的reverse()方法很容易实现这点。假设不同的app（比如news和blog)里都有article这个命名URL, 我们怎么区分呢？ 我们只需要在article前面加上blog这个命名空间即可。



```
from django.urls import reverse

# output blog/article/id
reverse('blog:article', args=[id])
```



**URL如何指向基于类的视图(View)**



目前path和re_path都只能指向视图view里的一个函数或方法，而不能指向一个基于类的视图(Class based view)。Django提供了一个额外as_view()方法，可以将一个类伪装成方法。这点在当你使用Django在带的view类或自定义的类时候非常重要。具体使用方式如下:



```
# blog/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [
      path('', views.ArticleList.as_view(), name='article_list'),
    path('blog/article/<int:id>/', views.article, name = 'article'),
    re_path(r'^blog/article/(?P<id>\d+)/$', views.article, name='article'),
]

# View (in blog/views.py)
from django.views.generic import ListView
from .views import Article

class ArticleList(ListView):

    queryset = Article.objects.filter(date__lte=timezone.now()).order_by('date')[:5]
    context_object_name = 'latest_article_list'
   template_name = 'blog/article_list.html'

def article(request, id):
    # 展示某篇文章
```



**通过URL方法传递额外的参数**



在你配置URL时，你还可以通过字典的形式传递额外的参数给视图, 而不用把这个参数写在链接里。如下面案例所示:



```
# blog/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [

    path('', views.ArticleList.as_view(), name='article_list', {'blog_id': 3}),
    re_path(r'^blog/article/(?P<id>\d+)/$', views.article, name='article'),
]
```