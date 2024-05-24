**什么是View视图? Django的View是如何工作的**

**
**

Django的Web开发也遵循经典软件设计开发的[MVC模式](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483665&idx=1&sn=19875184517f6513e53bec3b91c10202&chksm=a73c6129904be83f13ff0501c1159b4e3b776f086613ce4e3fdff2b525aa361cee819f5ebd77&scene=21#wechat_redirect)。View (视图) 主要根据用户的请求返回数据，用来展示用户可以看到的内容(比如网页，图片)，也可以用来处理用户提交的数据，比如保存到数据库中。Django的视图(View）通常和URL路由一起工作的。服务器在收到用户通过浏览器发来的请求后，会根据urls.py里的关系条目，去视图View里查找到与请求对应的处理方法，从而返回给客户端http页面数据。



我们先看一个最简单的视图View。当用户发来一个请求request时，我们通过HttpResponse打印出Hello， World!

```
# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello， World!")
```



这个例子过于简单。在实际Web开发过程中，我们的View不仅要负责从数据库提取数据，还需要指定显示内容的模板，并提供模板渲染页面所需的内容对象(context object)。



我们再来看看下面一个新闻博客的例子。/blog/展示所有博客文章列表。/blog/article/<int:id>/展示一篇文章的详细内容。

```
# blog/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
   path('blog/article/<int:id>/', views.article_detail, name='article_detail'),
]


# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article


# 展示所有文章
def index(request):
    latest_articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/article_list.html', {"latest_articles": latest_articles})


# 展示所有文章
def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'blog/article_detail.html', {"article": article})
```



```
那么这段代码是如何工作的？
```

- 当用户在浏览器输入/blog/时，URL收到请求后会调用视图views.py里的index方法，展示所有文章。
- 当用户在浏览器输入/blog/article/<int:id>/时，URL不仅调用了views.py里的article方法，而且还把参数文章id通过<int:id>括号的形式传递给了视图里的article_detail方法。。
- views.py里的index方法先提取要展示的数据对象列表latest_articles, 然后通过render方法传递给模板blog/article_list.html.。
- views.py里的article_detail方法先通过get_object_or_404方法和id调取某篇具体的文章对象article，然后通过render方法传递给模板blog/article_detail.html显示。

```
在本例中，我们使用了views里常用的2个便捷方法render()和get_object_or_404()。
```

- render方法有4个参数。第一个是request, 第二个是模板的名称和位置，第三个是需要传递给模板的内容, 也被称为context object。第四个参数是可选参数content_type（内容类型), 我们什么也没写。
- get_object_or_404方法第一个参数是模型Models或数据集queryset的名字，第二个参数是需要满足的条件（比如pk = id, title = 'python')。当需要获取的对象不存在时，给方法会自动返回Http 404错误。



下图是模板的代码。模板可以直接调用通过视图传递过来的内容。



```
# blog/article_list.html
{% block content %}
{% for article in latest_articles %}
     {{ article.title }}
     {{ article.pub_date }}
{% endfor %}
{% endblock %}

# blog/article_detail.html
{% block content %}
{{ article.title }}
{{ article.pub_date }}
{{ article.body }}
{% endblock %}
```



**一个更复杂点案例: View视图处理用户提交的数据**

视图View不仅用于确定给客户展示什么内容，以什么形式展示，而且也用来处理用户通过表单提交的数据。



我们再来看个用户修改个人资料的常见视图views.py。



```
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
   
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            return HttpResponseRedirect(reverse('users:profile', args=[user.id]))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,
                    }
        form = ProfileForm(default_data)

    return render(request, 'users/profile_update.html', {'form': form, 'user': user})
```



**views.profile_update是如何工作的?**





- 我们先从url获取user的主键pk(id), 利用get_object_or_404方法获取需要修改个人资料的用户对象user。
- 当用户通过POST方法提交个人资料修改表单，我们利用is_valid()方法先验证表单ProfileForm的数据是否有效。如果有效，我们将更新过的first_name和last_name数据存入user对象。更新成功返回个人信息页。
- 如果用户没有提交表单或不是通过POST方法提交表单，我们先获取现有数据生成default_data，利用ProfileForm显示。



ProfileForm实际上是非常简单的，包含了我们允许用户修改的字段。在这个案例里，我们没允许用户修改用户名和电子邮件，所以没有加进去。

```
# users/forms.py
from django import forms

class ProfileForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
```



**基于函数的视图(Function Based View)和基于类的视图(Class Based View)**



Django的视图有两种: 基于函数的视图(Function Base View)和基于类的视图(Class Based View)。上述案例中的index，article_detail和profile_update的方法都是基于函数的视图。优点是直接，容易读者理解。缺点是不便于继承和重用。在实际Web开发过程中，我们对不同的对象总是反复进行以下同样的操作，应该需要简化的。

- 展示对象列表（比如所有用户，所有文章）
- 查看某个对象的详细信息（比如用户资料，比如文章详情)
- 通过表单创建某个对象（比如创建用户，新建文章）
- 通过表单更新某个对象信息（比如修改密码，修改文字内容）
- 用户填写表单提交后转到某个完成页面
- 删除某个对象



Django提供了很多通用的基于类的视图(Class Based View)，来帮我们简化视图的编写。这些View与上述操作的对应关系如下:



- 展示对象列表（比如所有用户，所有文章）- ListView

- 展示某个对象的详细信息（比如用户资料，比如文章详情) - DetailView

- 通过表单创建某个对象（比如创建用户，新建文章）- CreateView

- 通过表单更新某个对象信息（比如修改密码，修改文字内容）- UpdateView

- 用户填写表单后转到某个完成页面 - FormView

- 删除某个对象 - DeleteView

  

上述常用通用视图一共有6个，前2个属于展示类视图(Display view), 后面4个属于编辑类视图(Edit view)。下面我们就来看下这些通用视图是如何工作的，如何简化我们代码的。一旦你用上通用视图，你就会爱上她。

**
**

**重要**：如果你要使用Edit view，请务必在[模型models](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483679&idx=2&sn=9e3db4167e408a2a0c3a1037c4f7266a&chksm=a73c6127904be831aee7abe13980fbea5e2d611ceb48e346dc0fc083c0a8725b52ebb3b8106f&scene=21#wechat_redirect)里定义get_absolute_url()方法，否则会出现错误。这是因为通用视图在对一个对象完成编辑后，需要一个返回链接。



**Django通用视图之ListView**



ListView用来展示一个对象的列表。它只需要一个参数模型名称即可。比如我们希望展示所有文章列表，我们的views.py可以简化为:



```
# Create your views here.
from django.views.generic import ListView
from .models import Article

class IndexView(ListView):

    model = Article
```

上述代码等同于:

```
# 展示所有文章
def index(request):
    queryset = Article.objects.all()
    return render(request, 'blog/article_list.html', {"object_list": queryset})
```

尽管我们只写了一行model = Article, ListView实际上在背后做了很多事情：

- 提取了需要显示的对象列表或数据集queryset: Article.objects.all()
- 指定了用来显示对象列表的模板名称(template name): 默认app_name/model_name_list.html, 即blog/article_list.html.
- 指定了内容对象名称(context object name):默认值object_list



**ListView的自定义**

**
**

你或许已经注意到了2个问题：需要显示的文章对象列表并没有按发布时间逆序排列，内容对象名称object_list也不友好。或许你也不喜欢默认的模板名字，还希望通过这个视图给模板传递额外的内容(比如现在的时间)。你可以轻易地通过重写queryset, template_name和context_object_name来完成ListView的自定义。如果你还需要传递模型以外的内容，比如现在的时间，你还可以通过重写get_context_data方法传递额外的参数或内容。

```
# Create your views here.
from django.views.generic import ListView
from .models import Article
from django.utils import timezone

class IndexView(ListView):

    queryset = Article.objects.all().order_by("-pub_date")
    template_name = 'blog/article_list.html'
    context_object_name = 'latest_articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

如果上述的queryset还不能满足你的要求，比如你希望一个用户只看到自己发表的文章清单，你可以通过更具体的get_queryset方法来返回一个需要显示的对象列表。



```
# Create your views here.
from django.views.generic import ListView
from .models import Article
from django.utils import timezone

class IndexView(ListView):

    template_name = 'blog/article_list.html'
    context_object_name = 'latest_articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

**
**

**URL如何指向基于类的视图(View)**



目前urls.py里path和re_path都只能指向视图view里的一个函数或方法，而不能指向一个基于类的视图(Class Based View)。Django提供了一个额外as_view()方法，可以将一个类伪装成方法。这点在当你使用Django在带的view类或自定义的类时候非常重要。更多内容见Django基础技术知识(2)[URL的设计与配置](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483716&idx=2&sn=2c0ac2f977c063c67503a9ff3f8d4d0c&chksm=a73c617c904be86a16e7389c3d66760b86e06dd2f5f2f0f0ef6007b38d32647d8700e2a0a48a&scene=21#wechat_redirect)。



具体使用方式如下:



```
# blog/urls.py
from django.urls import path, re_path

from . import views

urlpatterns = [
      path('blog/', views.IndexView.as_view(), name='index'),
]
```



**Django通用视图之DetailView**

DetailView用来展示一个具体对象的详细信息。它需要URL提供访问某个对象的具体参数（如pk, slug值）。本例中用来展示某篇文章详细内容的view可以简写为:



```
# Create your views here.
from django.views.generic import DetailView
from .models import Article

class ArticleDetailView(DetailView):

    model = Article
```

DetailView默认的模板是app/model_name_detail.html, 默认的内容对象名字context_object_name是model_name。本例中默认模板是blog/article_detail.html, 默认对象名字是article, 在模板里可通过 {{ article.title }}获取文章标题。



你同样可以通过重写queryset, template_name和context_object_name来完成DetailView的自定义。你还可以通过重写get_context_data方法传递额外的参数或内容。如果你指定了queryset, 那么返回的object是queryset.get(pk = id), 而不是model.objects.get(pk = id)。

```
# Create your views here.
from django.views.generic import ListView，DetailView
from .models import Article
from django.utils import timezone

class ArticleDetailView(DetailView):

    queryset = Article.objects.all().order_by("-pub_date") # 
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```

在实际应用中，上述代码可能还不能满足你的要求。比如你希望一个用户只能看到自己发表的文章详情。当用户查看别人的文章详情时，返回http 404错误。这时候你可以通过更具体的get_object()方法来返回一个更具体的对象。代码如下:



```
# Create your views here.
from django.views.generic import DetailView
from django.http import Http404
from .models import Article
from django.utils import timezone

class ArticleDetailView(DetailView):

    queryset = Article.objects.all().order_by("-pub_date")
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.author != self.request.user:
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
```



**Django通用视图之CreateView**

CreateView一般通过某个表单创建某个对象，通常完成后会转到对象列表。比如一个最简单的文章创建CreateView可以写成：



```
from django.views.generic.edit import CreateView
from .models import Article

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body', 'pub_date']
```

CreateView默认的模板是model_name_form.html, 即article_form.html。默认的context_object_name是form。模板代码如下图所示:



```
# blog/article_form.html
<form method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save" />
</form>
```

如果你不想使用默认的模板和默认的表单，你可以通过重写template_name和form_class来完成CreateView的自定义。虽然form_valid方法不是必需，但很有用。当用户提交的数据是有效的时候，你可以通过定义此方法做些别的事情，比如发送邮件，存取额外的数据。



```
from django.views.generic.edit import CreateView
from .models import Article
from .forms import ArticleCreateForm

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_create_form.html'
    form_class = ArticleCreateForm

    def form_valid(self, form):
       form.do_sth()
       return super().form_valid(form)
```

form_valid方法一个常见用途就是就是将创建对象的用户与model里的user结合。见下面例子。

```
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_create_form.html'
    form_class = ArticleCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

**
**

**Django通用视图之UpdateView**

UpdateView一般通过某个表单更新现有对象的信息，更新完成后会转到对象详细信息页面。它需要URL提供访问某个对象的具体参数（如pk, slug值）。比如一个最简单的文章更新的UpdateView如下所示。



```
from django.views.generic.edit import UpdateView
from .models import Article

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body', 'pub_date']
```

UpdateView和CreateView很类似，比如默认模板都是model_name_form.html。但是区别有两点: 

- CreateView显示的表单是空表单，UpdateView中的表单会显示现有对象的数据。
- 用户提交表单后，CreateView转向对象列表，UpdateView转向对象详细信息页面。



你可以通过重写template_name和form_class来完成UpdateView的自定义。

- 本例中默认的form是article_form.html, 你可以改为article_update_form.html。
- 虽然form_valid方法不是必需，但很有用。当用户提交的数据是有效的时候，你可以通过定义此方法做些别的事情，比如发送邮件，存取额外的数据。

```
from django.views.generic.edit import UpdateView
from .models import Article
from .forms import ArticleUpdateForm

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog/article_update_form.html'
    form_class = ArticleUpdateForm

    def form_valid(self, form):
       form.do_sth()
       return super().form_valid(form)
```



**
**

**Django通用视图之FormView**

FormView一般用来展示某个表单，而不是某个模型对象。当用户输入信息未通过表单验证，显示错误信息。当用户输入信息通过表单验证提交成功后，转到其它页面。使用FormView一般需要定义template_name, form_class和跳转的success_url.



见下面代码。



```
# views.py - Use FormView
from myapp.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
```



**Django通用视图之DeleteView**

DeleteView一般用来删除某个具体对象。它要求用户点击确认后再删除一个对象。使用这个通用视图，你需要定义模型的名称model和成功删除对象后的返回的URL。默认模板是myapp/model_confirm_delete.html。默认内容对象名字是model_name,本例中为article。



本例使用了默认的模板blog/article_confirm_delete.html，删除文章后通过reverse_lazy方法返回到index页面。



```
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Article

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
```

模板内容如下:

```
# blog/article_confirm_delete.html
<form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ article }}"?</p>
    <input type="submit" value="Confirm" />
</form>
```

但这段代码还有个问题，你注意到没? 用户可以删除任意文章，包括别人发表的文章。如果我们想用户只能删除自己的文章，上述代码怎么改? 我们通过get_queryset方法筛选出作者自己的文章即可。views.py可改成下文:



```
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Article

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
```