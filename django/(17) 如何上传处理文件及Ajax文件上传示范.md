**Django文件上传需要考虑的重要事项**



文件一般通过表单进行。用户在前端点击文件上传，然后以POST方式将数据和文件提交到服务器。服务器在接收到POST请求后需要将其存储在服务器上的某个地方。Django默认的存储地址是相对于根目录的/media/文件夹，存储的默认文件名就是文件本来的名字。上传的文件如果不大于2.5MB，会先存入服务器内存中，然后再写入磁盘。如果上传的文件很大，Django会把文件先存入临时文件，再写入磁盘。



Django默认处理方式会出现一个问题，所有文件都存储在一个文件夹里。不同用户上传的有相同名字的文件可能会相互覆盖。另外用户还可能上传一些不安全的文件如js和exe文件，我们必需对允许上传文件的类型进行限制。因此我们在利用Django处理文件上传时必需考虑如下3个因素:

- 设置存储上传文件的文件夹地址
- 对上传文件进行重命名
- 对可接受的文件类型进行限制(表单验证)

本文将会讲解在Django示范代码中如何实现上述3个功能。



**Django文件上传的3种常见方式**



Django文件上传一般有3种方式(如下所示)。我们会针对3种方式分别提供代码示范。

- 使用一般的表单上传，在视图中手动编写代码处理上传的文件
- 使用由模型创建的表单(ModelForm)上传，使用form.save()方法自动存储
- 使用Ajax实现文件异步上传，上传页面无需刷新即可显示新上传的文件



**项目创建与设置**

我们先使用django-admin startproject命令创建一个叫file_project的项目，然后cd进入file_project, 使用python manage.py startapp创建一个叫file_upload的app。



我们首先需要将file_upload这个app加入到我们项目里，然后设置/media/和/STATIC_URL/文件夹。我们上传的文件都会放在/media/文件夹里。我们还需要使用css和js这些静态文件，所以需要设置STATIC_URL。

\#file_project/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'file_upload',
]
```

\#file_project/settings.py

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]

# specify media root for user uploaded files,
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

\#file_project/urls.py

```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', include("file_upload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



**创建模型**

使用Django上传文件创建模型不是必需，然而如果我们需要对上传文件进行系统化管理，模型还是很重要的。我们的File模型包括file和upload_method两个字段。我们通过upload_to选项指定了文件上传后存储的地址，并对上传的文件进行了重命名。如果你想了解如何自定义用户上传文件夹地址和对上传文件进行重命名，请阅读[这里](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483887&idx=2&sn=3d8531c15ffda4faa32bde775bfd61fb&chksm=a73c61d7904be8c1621603284549aa7eca6e144d8603e6759172d6b5a6b92a0bf6e08ab2d672&scene=21#wechat_redirect)。



\#file_upload/models.py

```python
from django.db import models
import os
import uuid

# Create your models here.
# Define user directory path

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)
    upload_method = models.CharField(max_length=20, verbose_name="Upload Method")
```

注意：

- 如果你不使用ModelForm，你还需要手动编写代码存储上传文件。



**URLConf配置**

本项目一共包括5个urls, 分别对应普通表单上传，ModelForm上传和Ajax上传。还有两个urls，一个用来显示文件清单，一个专门处理ajax请求。

\#file_upload/urls.py

```python
from django.urls import re_path, path
from . import views

# namespace
app_name = "file_upload"

urlpatterns = [

    # Upload File Without Using Model Form
    re_path(r'^upload1/$', views.file_upload, name='file_upload'),

    # Upload Files Using Model Form
    re_path(r'^upload2/$', views.model_form_upload, name='model_form_upload'),

    # Upload Files Using Ajax Form
    re_path(r'^upload3/$', views.ajax_form_upload, name='ajax_form_upload'),

    # Handling Ajax requests
    re_path(r'^ajax_upload/$', views.ajax_upload, name='ajax_upload'),

    # View File List
    path('', views.file_list, name='file_list'),

]
```



**使用一般表单上传文件**

我们先定义一个一般表单FileUploadForm，并通过clean方法对用户上传的文件进行验证，如果上传的文件名不以jpg, pdf或xlsx结尾，将显示表单验证错误信息。关于表单的自定义和验证更多内容见[Django基础(5): 表单forms的设计与使用](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483813&idx=1&sn=bda48ff63fd4cc3b2cc0de408e7a1fa1&chksm=a73c619d904be88b13d9c27bc4afb5ca45c76473c5d56cf3b5a0f7f9cf7a57775168ff6150f1&scene=21#wechat_redirect)。

\#file_upload/forms.py

```python
from django import forms
from .models import File


# Regular form
class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    upload_method = forms.CharField(label="Upload Method", max_length=20,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "xlsx"]:
            raise forms.ValidationError("Only jpg, pdf and xlsx files are allowed.")
        # return cleaned data is very important.
        return file
```

注意： 

- 使用clean方法对表单字段进行验证时，别忘了return验证过的数据，即cleaned_data。只有返回了cleaned_data, 视图中才可以使用form.cleaned_data.get('xxx')获取验证过的数据。

  

对应一般文件上传的视图file_upload方法如下所示。当用户的请求方法为POST时，我们通过form.cleaned_data.get('file')获取通过验证的文件，并调用自定义的handle_uploaded_file方法来对文件进行重命名，写入文件。如果用户的请求方法不为POST，则渲染一个空的FileUploadForm在upload_form.html里。我们还定义了一个file_list方法来显示文件清单。

\#file_upload/views.py

```python
from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat

# Create your views here.


# Show file list
def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'file_upload/file_list.html', {'files': files})


# Regular file upload without using ModelForm
def file_upload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get cleaned data
            upload_method = form.cleaned_data.get("upload_method")
            raw_file = form.cleaned_data.get("file")
            new_file = File()
            new_file.file = handle_uploaded_file(raw_file)
            new_file.upload_method = upload_method
            new_file.save()
            return redirect("/file/")
    else:
        form = FileUploadForm()

    return render(request, 'file_upload/upload_form.html', {'form': form,
                                                            'heading': 'Upload files with Regular Form'})


def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    # file path relative to 'media' folder
    file_path = os.path.join('files', file_name)
    absolute_file_path = os.path.join('media', 'files', file_name)

    directory = os.path.dirname(absolute_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(absolute_file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path
```

注意： 

- handle_uploaded_file方法里文件写入地址必需是包含/media/的绝对路径，如果/media/files/xxxx.jpg，而该方法返回的地址是相对于/media/文件夹的地址，如/files/xxx.jpg。存在数据中字段的是相对地址，而不是绝对地址。
- 构建文件写入绝对路径时请用os.path.join方法，因为不同系统文件夹分隔符不一样。
- 写入文件前一个良好的习惯是使用os.path.exists检查目标文件夹是否存在，如果不存在先创建文件夹，再写入。



上传表单模板upload_form.html代码如下。

\#file_upload/templates/upload_form.html

```python
{% extends "file_upload/base.html" %}
{% block content %}
{% if heading %}
<h3>{{ heading }}</h3>
{% endif %}
<form action="" method="post" enctype="multipart/form-data" >
  {% csrf_token %}
  {{ form.as_p }}
 <button class="btn btn-info form-control " type="submit" value="submit">Upload</button>
</form>
{% endblock %}
```

注意： 

- 发送<form>必需有属性enctype="multipart/form-data"，否则表单不能发送文件，request.FILES为空。
- 我们的模板继承了base.html, 别忘了添加哦， 目的是为了显示更漂亮。

\#file_upload/templates/base.html

```python
{% load static %}

<html lang="en">
<head>
<title>{% block title %}Django File Upload and Download{% endblock %} </title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>

<body>
 <!-- Page content of course! -->
<main class="container-fluid">
<div class="container">

 {% block content %} {% endblock %}

</div> 
</main>

<!-- Bootstrap core JavaScript
================================================== -->

<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

{% block js %} {% endblock %}

</body>
</html>
```



普通表单上传文件页面显示如下所示:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAqicYJNgHJmcvzmGhqK0RyoWAjia0OiaeG9W8uRSVvKkoia0jszVhyxJGOpvuiaez8wFnGab5yGjJmR4Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

显示文件清单模板file_list.html代码如下所示:

\#file_upload/templates/file_list.html

```python
{% extends "file_upload/base.html" %}

{% block content %}
<h3>File List</h3>
<p> <a href="/file/upload1/">RegularFormUpload</a> | <a href="/file/upload2/">ModelFormUpload</a>
    | <a href="/file/upload3/">AjaxUpload</a></p>
{% if files %}
<table class="table table-striped">

    <tbody>
    <tr>
        <td>Filename & URL</td>
        <td>Filesize</td>
        <td>Upload Method</td>
    </tr>
    {% for file in files %}
    <tr>
        <td><a href="{{ file.file.url }}">{{ file.file.url }}</a></td>
        <td>{{ file.file.size | filesizeformat }}</td>
        <td>{{ file.upload_method }}</td>
    </tr>
    {% endfor %}
    </tbody>
</table>

{% else %}
<p>No files uploaded yet. Please click <a href="{% url 'file_upload:file_upload' %}">here</a>
    to upload files.</p>
{% endif %}

{% endblock %}
```



注意： 

- 对于上传的文件我们可以调用file.url, file.name和file.size来查看上传文件的链接，地址和大小。
- 上传文件的大小默认是以B显示的，数字非常大。使用Django模板过滤器filesizeformat可以将文件大小显示为人们可读的方式，如MB，KB。

文件清单显示效果如下所示:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAqicYJNgHJmcvzmGhqK0RyodUXJA9T3L5zibAnqFpnrYeQBr6uWauOxnbamKcrLfkgeHpXyWLkK5TA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**使用ModelForm上传文件**

使用ModelForm上传是小编我推荐的上传方式，前提是你已经在模型中通过upload_to选项自定义了用户上传文件存储地址，并对文件进行了重命名。



我们首先要自定义自己的FileUploadModelForm，由模型重建的。代码如下所示:

\#file_upload/forms.py

```python
from django import forms
from .models import File


# Model form
class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'upload_method',)

        widgets = {
            'upload_method': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ["jpg", "pdf", "xlsx"]:
            raise forms.ValidationError("Only jpg, pdf and xlsx files are allowed.")
        # return cleaned data is very important.
        return file
```

使用ModelForm处理文件上传的视图model_form_upload方法非常简单，只需使用form.save()即可，无需再手动编写代码写入文件。

\#file_upload/views.py

```python
from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm, FileUploadModelForm
import os
import uuid
from django.http import JsonResponse
from django.template.defaultfilters import filesizeformat

# Create your views here.


# Upload File with ModelForm
def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/file/")
    else:
        form = FileUploadModelForm()

    return render(request, 'file_upload/upload_form.html', {'form': form,
                                                            'heading': 'Upload files with ModelForm'})
```

上传表单模板也是upload_form.html，和前例供用的。

\#file_upload/templates/upload_form.html

```python
{% extends "file_upload/base.html" %}
{% block content %}
{% if heading %}
<h3>{{ heading }}</h3>
{% endif %}
<form action="" method="post" enctype="multipart/form-data" >
  {% csrf_token %}
  {{ form.as_p }}
 <button class="btn btn-info form-control " type="submit" value="submit">Upload</button>
</form>
{% endblock %}
```

显示效果如下所示:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAqicYJNgHJmcvzmGhqK0RyoiacNzich9w9OsmYwlrbcweEnbMkuYvjkqTeFVPwT5kgiaIhM6DAib2OWdQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**使用Ajax上传文件**

使用Ajax上传文件的好处是，你上传文件后无需刷新页面或跳转即可立刻显示新上传的文件信息(如下所示)。Ajax应用场景还是非常普遍的，比如用户上传头像后无需刷新实时显示新上传的头像。或则用户添加评论后无需刷新页面直接显示新增的评论。

**
**

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoAqicYJNgHJmcvzmGhqK0RyohLwbAvvicLw6nsiciaMPGZ8tp0a7CaicFV3vibicatia382bT0U5lgPl8g1Vg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

AJAX文件上传代码最重要的部分在前端（代码如下所示)。我们构建了FormData对象，添加了file和upload_method, 并通过设置processData=False告诉jQuery不要处理上传的文件，交由后台处理。由于发送POST请求还需要提供csrftoken，我们还通过jQuery的cookie库获取crsftoken，添加到请求头里，一起发到服务器上。如果后台返回的data没有error_msg, 就显示后台返回的更新过的文件清单。处理ajax的请求地址是/file/ajax_upload/, 对应的视图方法是ajax_upload.

\#file_upload/templates/ajax_upload_form.html

```python
{% extends "file_upload/base.html" %}
{% block content %}

{% if heading %}
<h3>{{ heading }}</h3>
{% endif %}

<form action="" method="post" enctype="multipart/form-data" id="form">
    <ul class="errorlist"></ul>
    {% csrf_token %}
{{ form.as_p }}
 <input type="button" class="btn btn-info form-control" value="submit" id="btn" />
</form>
<table class="table table-striped" id="result">
</table>
{% endblock %}


{% block js %}
<script src=" https://cdn.jsdelivr.net/jquery.cookie/1.4.1/jquery.cookie.min.js ">
</script>
<script>
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function(){
   $('#btn').click(function(e){
        e.preventDefault();
        // 构建FormData对象
      var form_data = new FormData();
        form_data.append('file', $('#id_file')[0].files[0]);
        form_data.append('upload_method', $('#id_upload_method').val());
        $.ajax({
        url: '/file/ajax_upload/',
        data: form_data,
        type: 'POST',
        dataType: 'json',
        // 告诉jQuery不要去处理发送的数据, 发送对象。
      processData : false,
        // 告诉jQuery不要去设置Content-Type请求头
      contentType : false,
        // 获取POST所需的csrftoken
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }},
        success: function (data) {
            if(data['error_msg']) {
                var content = '<li>Only jpg, pdf and xlsx files are allowed.</li>';
                $('ul.errorlist').html(content);
            }
            else
            {
            var content= '<thead><tr>' +
            '<th>Name and URL</th>' +
            '<th>Size</th>' +
            '<th>Upload Method</th>' +
            '</tr></thead><tbody>';

             $.each(data, function(i, item) {
                  content = content +
                  '<tr><td>' +
                  "<a href= ' " +
                  item['url'] +
                  " '> " +
                  item['url'] +
                  '</a></td><td>' +
                  item['size'] +
                  '</td><td>' +
                  item['upload_method'] +
                   '</td><tr>'
                });
             content = content + "</tbody>";
             $('#result').html(content);
             }
           },
        });
   });
 });
  </script>
{% endblock %}
```

注意： 

- Ajax代码部分代码请注意不要随意变动，尤其评论//部分要特别注意。



负责处理Ajax请求的视图ajax_upload方法如下所示。该方法将ajax发过来的数据于FileUploadModelForm先结合，然后直接调用form.save方法存储，最后以json格式返回更新过的文件清单。如何用户上传文件不符合要求，返回错误信息。

\#file_upload/views.py

```python
# Upload File with ModelForm
def ajax_form_upload(request):
    form = FileUploadModelForm()
    return render(request, 'file_upload/ajax_upload_form.html', {'form': form,
                                                            'heading': 'File Upload with AJAX'})

# handling AJAX requests
def ajax_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # Obtain the latest file list
            files = File.objects.all().order_by('-id')
            data = []
            for file in files:
                data.append({
                    "url": file.file.url,
                    "size": filesizeformat(file.file.size),
                    "upload_method": file.upload_method,
                    })
            return JsonResponse(data, safe=False)
        else:
            data = {'error_msg': "Only jpg, pdf and xlsx files are allowed."}
            return JsonResponse(data)
    return JsonResponse({'error_msg': 'only POST method accpeted.'})
```



**GitHub源码**

https://github.com/shiyunbo/django-file-upload-download