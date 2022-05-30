**什么是表单？何时使用表单？**

在web开发里表单的使用必不可少。表单用于让用户提交数据或上传文件，表单也用于让用户编辑已有数据。Django的表单Forms类的作用是把用户输入的数据转化成Python对象格式，便于后续操作（比如存储，修改）。

###  

**自定义表单**

类似模型，Django表单也由各种字段组成。表单可以自定义(forms.Form)，也可以由模型Models创建(forms.ModelForm)。值得注意的是模型里用的是verbose_name来描述一个字段, 而表单用的是label。



下面是两个ContactForm的例子。一个自定义，一个从Model创建。





```python
from django import forms
from .models import Contact


class ContactForm1(forms.Form):
    
    name = forms.CharField(label="Your Name", max_length=255)
    email = forms.EmailField(label="Email address")


class ContactForm2(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email',)

```

### Django的常用做法是在app文件夹下创建一个forms.py，专门存放app中所定义的各种表单，这样方便集中管理表单。如果要使用上述表单，我们可以在视图views.py里把它们像模型一样import进来直接使用。



### **表单实例化**

下面方法可以实例化一个空表单，但里面没有任何数据，可以通过 {{ form }}在模板中渲染。

```python
form = ContactForm()
```

用户提交的数据可以通过以下方法与表单结合，生成与数据结合过的表单(Bound forms)。Django只能对Bound forms进行验证。

```python
form = ContactForm(data=request.POST, files=request.FILES)
```

### **模板文件中使用form**

模板文件中我们可以通过{{ form.as_p }}, {{ form.as_li }} 和 {{ form.as_table }}中渲染表单。如果你想详细控制每个field的格式，你可以采取以下方式。

```python
{% block content %}
<div class="form-wrapper">
   <form method="post" action="" enctype="multipart/form-data">
      {% csrf_token %}
      {% for field in form %}
           <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
             <p class="help">{{ field.help_text|safe }}</p>
        {% endif %}
           </div>
        {% endfor %}
      <div class="button-wrapper submit">
         <input type="submit" value="Submit" />
      </div>
   </form>
</div>
{% endblock %}
```

``

### ** **

### **表单实际使用案例**

我们现在需要设计一个表单让用户完成注册。我们先在app目录下新建forms.py, 然后创建一个RegistrationForm。代码如下:



```python
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email',)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
```





当然你也可以不用新建forms.py而直接在html模板里写表单，但我并不建议这么做。用forms.py的好处显而易见: 

- 所有的表单在一个文件里，非常便于后期维护，比如增添或修订字段。
- forms.py可通过clean方法自定义表单验证，非常便捷（见后文）。



我们使用RegistrationForm的视图views.py是这样子的。



```python
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password, email=email)
            # 如果直接使用objects.create()方法后不需要使用save()
            return HttpResponseRedirect("/accounts/login/")

    else:
        form = RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})
```

模板是registration.html这样子的。如果你需要通过表单上传图片或文件，一定不要忘了给form加enctype="multipart/form-data"属性。



```python
<form action=”.” method=”POST”>
{{ form.as_p }}
</form>
```







我们来看下RegistrationForm是怎么工作的:





- 当用户通过POST方法提交表单，我们将提交的数据与RegistrationForm结合，然后验证表单RegistrationForm的数据是否有效。
- 如果表单数据有效，我们先用Django User模型自带的create_user方法创建user对象，再创建user_profile。用户通过一张表单提交数据，我们实际上分别存储在两张表里。
- 如果用户注册成功，我们通过HttpResponseRedirect方法转到登陆页面
- 如果用户没有提交表单或不是通过POST方法提交表单，我们转到注册页面，生成一张空的RegistrationForm

###  

### **表单的验证**

每个forms类可以通过clean方法自定义表单验证。如果你只想对某些字段进行验证，你可以通过clean_字段名方式自定义表单验证。如果用户提交的数据未通过验证，会返回ValidationError，并呈现给用户。如果用户提交的数据有效form.is_valid()，则会将数据存储在cleaned_data里。



在上述用户注册的案例里，我们在RegistrationForm通过clean方法添加了用户名验证，邮箱格式验证和密码验证。代码如下。



```python
from django import forms
from django.contrib.auth.models import User
import re


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email',)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("Your username must be at least 6 characters long.")
        elif len(username) > 50:
            raise forms.ValidationError("Your username is too long.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your username already exists.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your email already exists.")
        else:
            raise forms.ValidationError("Please enter a valid email.")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("Your password is too short.")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long.")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch. Please enter again.")

        return password2
```



**通用视图里使用表单**

在Django基于类的视图(Class Based View)里使用表单也非常容易，只需定义form_class就好了。下面是一个创建一篇新文章的例子。



```python
from django.views.generic.edit import CreateView
from .models import Article
from .forms import ArticleForm


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_create_form.html'
```



**自定义表单输入的widget**

Django forms的每个字段你都可以选择你喜欢的输入widget，比如多选，复选框。你还可以定义每个widget的css属性。如果你不指定，Django会使用默认的widget，有时比较丑。



比如下面这段代码定义了表单姓名字段的输入控件为Textarea，还指定了其样式css。



```python
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={'class': 'custom'},
        ),
    )
```



设置widget可以是你的表单大大美化，方便用户选择输入。比如下面案例里对年份使用了SelectDateWidget，颜色则使用了复选框CheckboxSelectMultiple。单选可以用RadioSelect和Select。常见文本输入可以用TextInput和TextArea。



```python
from django import forms

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=COLORS_CHOICES,
    )
```

**表单数据初始化**

有时我们需要对表单设置一些初始数据，我们可以通过initial方法，如下所示。



```python
form = ContactForm(
    initial={
        'name': 'First and Last Name',
    },)
```

其编辑修改类应用场景中，我们还要给表单提供现有对象的数据，而不是渲染一张空表单，这时我们可这么做。该方法仅适用于由模型创建的ModelForm，而不适用于自定义的表单。



```python
contact = Contact.objects.get(id=1)
form =  ContactForm(instance = contact)
```

对于自定义的表单，可以设置default_data。



```python
default_data = {'name': 'John', 'email': 'someone@hotmail.com', }
form = ContactForm(default_data)
```

**
**

**Formset的使用**

有的时候用户需要在1个页面上使用多个表单，比如一次性提交添加多本书的信息，这时我们可以使用formset。这是一个表单的集合。



创建一个FormSet我们可以这么做:



```python
from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField()
    pub_date = forms.DateField(required=False)


# forms.py - build a formset of books

from django.forms import formset_factory
from .forms import BookForm

# extra: 额外的空表单数量
# max_num: 包含表单数量（不含空表单)

BookFormSet = formset_factory(BookForm, extra=2, max_num=1)
```





在视图文件views.py里，我们可以像使用form一样使用formset。

```python
# views.py - formsets example.
from .forms import BookFormSet
from django.shortcuts import render

def manage_books(request):
    if request.method == 'POST':
        formset = BookFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = BookFormSet()
    return render(request, 'manage_books.html', {'formset': formset})
```

模板里可以这样使用formset。



```
<form action=”.” method=”POST”>
{{ formset }}
</form>
```