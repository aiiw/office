

**redirect方法**

**redirect是URL重新定向的便捷方法，在django.shortcuts模块里。HttpResponseRedirect能支持的URL重定向，redirect都支持。比如下面3种重定向是redirect的常规用法。**

```python
from django.shortcuts import redirect
from django.urls import reverse

# 案例1
def my_view(request):
    ...
    return redirect('/index/')

# 案例2
def my_view(request):
    ...
    return redirect('https://www.baidu.com/')

# 案例3
def my_view(request):
    ...
    return redirect(reverse('blog:article_list'))
```



**redirect真正NB的地方在于，它不仅能根据URL重定向，还可以根据对象Object重定向和根据视图view重定向**，根据视图重定向的时候还可以传递额外的参数。



1. 根据对象Object重定向

使用该方法的前提是模型里已经定义了get_asbolute_url方法，使用redirect会自动调用get_absolute_url方法。

```python
from django.shortcuts import redirect

def my_view(request):
    ...
    obj = MyModel.objects.get(...)
    return redirect(obj)
```



2. 根据视图view重定向

使用该方法的前提已对URL进行了命名，且对应了相应的视图。下面案例中redirect会先根据视图函数的名字查找对应url，在传递额外参数。后台工作还是由reverse方法来完成的。

```python
def my_view(request):
    ...
    return redirect('some-view-name', foo='bar')
```



**HttpResponseDirect方法**

**HttpResponseRedirect是django首选的URL重定向方法**，在django.http模块里。该方法的第一个参数是必要的，是用来重定向的URL地址。这个URL可以是完整的链接（比如’http://www.baidu.com‘），也可以是一个不包含域名的静态链接（例如‘/index/’）。



我们下面以新闻博客(blog)为例来看看如何使用HttpResponseDirect方法。假如我们有如下3个urls, 一个展示文章，一个添加文章，一个展示文章详情。我们需要使用该方法在视图中实现两种URL重定向:

- 转向不含参数的URL: 用户添加文章完成后转向文章列表(/index/); 或

- 转向包含参数的URL: 用户添加文章完成后转向文章详情(/article/2/new-day/)

  

```python
from django.urls import path, re_path
from . import views

# namespace
app_name = 'blog'
urlpatterns = [
    # 展示所有文章
    path('/index/', views.ArticleListView.as_view(), name='article_list'),
    # 展示文章详情
    re_path(r'^article/(?P<pk>\d+)/(?P<slug1>[-\w]+)/$',
            views.ArticleDetailView.as_view(), name='article_detail'),
    # 添加文章
    re_path(r'^article/create/$',
            views.ArticleCreateView.as_view(), name='article_create'),
]
```



1. 在视图views.py中利用HttpResponse重新定向至不含参数的URL

```python
from .models import Article, 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ArticleForm

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect("/index/")
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create_form.html', {'form': form})
```

如果/index/页面有分页功能， 你还可以通过使用HttpResponseRedirect('/index/?page=2')直接获取第2页的文章列表。



**HttpReponseDirect只支持hard coded urls(硬编码链接), 不能直接使用命名的URL，如使用HttpResponseDirect('blog:article_list‘)是错误的。**在使用URL命名时，我们需要先通过URL反向解析方法reverse先对命名URL(article_list)进行解析，然后再使用HttpReponseRedirect定向(如下面的代码)。背后的逻辑是reverse('blog:article_list')='/index/'。

```python
......
from django.http import HttpResponseRedirect
from django.urls import reverse
.....

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:article_list'))
   ....
```



2. 在视图views.py中利用HttpResponseDirect重新定向至包含参数的URL

对于包含参数的URL(/article/2/new-day/)，使用HttpResponseDirect定向前一般需要先使用reverse方法对命名的URL(如'article_detail')进行解析，同时传递参数(如id, slug等）。

```python
from .models import Article
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import ArticleForm

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect(reverse('blog:article_detail', args=[str(article.pk), article.slug]))
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create_form.html', {'form': form})
```



其中最重要的一行代码如下所示。大家可以仔细看下参数是如何传递到url的。

```
reverse('blog:article_detail', args=[str(article.pk), article.slug]
```



**reverse方法**

reverse方法的作用是对已命名的URL进行反向解析，还传递相应的参数（args或带key的参数kargs)。该方法位于django.urls模块。reverse方法一般有2种应用场景:

- 在模型中自定义get_absolute_url时使用，传递参数
- 在视图中对命名URL进行解析，传递参数，再使用HttpResponseDirect和redict进行重定向



1. 模型中自定义get_absolute_url，并传递参数args

```python
def get_absolute_url(self):
    return reverse('blog:article_detail', args=[str(self.pk), self.slug])
```



2. 在视图中配合URL重定向使用，并传递kargs

```python
from django.urls import reverse
from django.shortcuts import redirect

def my_view(request):
    ...
    return redirect(reverse('admin:app_list', kwargs={'app_label': 'auth'}))
```



还有一点容易被人们忽略的是reverse方法**不仅能对命名的urls进行反向解析，还可以对视图函数进行反向解析**，找到需要重新定向的url, 如下面代码所示。当然但这个方法我们并不推荐使用。与此功能相反的是resolve方法，该方法可以根据url找到对应视图函数。

```python
from django.urls import reverse
from blog import views
reverse(views.index)
```



**小结**

HttpResponseDirect, redirect和reverse三个方法都非常常用，在使用它们前忘了import进来哦。注意它们在不同的模块。

- HttpResponseDirect - django.http
- redirect - django.shortcuts
- reverse - django.urls