**自定义字段属性和错误信息**

对于每个字段你可以设置其是否为必需，最大长度和最小长度。你还可以针对每个属性自定义错误信息，见下面代码。

```python
from django import forms


class LoginForm(forms.Form):  
    username = forms.CharField(
        required=True,
        max_length=20,
        min_length=6,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '用户名长度不得超过20个字符',
            'min_length': '用户名长度不得少于6个字符',
        }
    )
    password = forms.CharField(
        required=True,
        max_length=20,
        min_length=6,
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码长度不得超过20个字符',
            'min_length': '密码长度不得少于6个字符',
        }
    )
```



对于基继承ModelForm类的表单, 我们可以在Meta选项下widget中来自定义错误信息，如下面代码所示:

```python
from django.forms import ModelForm, Textarea
from myapp.models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),  # 关键是这一行
        }
        labels = {
            'name': _('Author'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
```

**
**

**自定义表单输入的widget和css属性**

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

**
**

**表单数据初始化和实例化**

有时我们需要对表单设置一些初始数据，我们可以通过initial方法，如下所示。



```python
form = ContactForm(
    initial={
        'name': 'First and Last Name',
    },)
```

其编辑修改类应用场景中，我们还要给表单提供现有对象的数据，而不是渲染一张空表单。这个过程叫表单与数据的结合。



对于由继承ModelForm类的表单，我们可以按如下方法对表单进行实例化，如下面代码所示:

```python
contact = Contact.objects.get(id=1)
form =  ContactForm(instance = contact)
```



对于自定义的表单，可以设置default_data。对于用户提交的数据，括号里可以使用request.POST。

```python
default_data = {'name': 'John', 'email': 'someone@hotmail.com', }
form = ContactForm(default_data)
```



**自定义表单验证validators**

对于表单验证除了通过clean方法自定义验证外，你还可以选择自定义validators。例如下面案例中，如果用户输入的手机号不符合要求，表单就会返回手机号码格式错误的验证信息。

```python
from django.core.exceptions import ValidationError
import re


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class UserInfo(forms.Form):
    email = forms.EmailField(error_messages={'required': u'邮箱不能为空'},)
    mobile = forms.CharField(validators=[mobile_validate, ],
                             error_messages={'required': u'手机不能为空'},
                             widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'手机号码'}),)
```



**一个页面同时提交2张或多张表单**

很多情况下我们希望用户在同一页面上点击一个按钮能同时提交2张或多张表单，这时我们可以在模板中给每个表单取不同的名字，如form1和form2（如下面代码所示)。注: form1和form2分别对应forms.py里的Form1()和Form2()。

```python
<form >
    {{ form1.as_p }}
    {{ form2.as_p }}
</form>
```

然后用户点击提交后，我们就可以在视图里了对用户提交的数据进行分别处理了，如下面代码所示。

```python
if request.method == 'POST':
        form1 = Form1( request.POST,prefix="form1")
        form2 = Form2( request.POST,prefix="form2")
        
        if form1.is_valid() or form2.is_valid(): 
            pass
else:
        form1 = Form1(prefix="form1")
        form2 = Form2(prefix="form2")
```