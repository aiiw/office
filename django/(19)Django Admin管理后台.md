**为什么要使用Django Admin**

**
**

使用Django Admin可以快速对数据库的各个数据表进行增删查改。一行代码即可增加对一个模型(数据表)的增删查改。试想如果你要自己手动编写后台对一个模型进行增删查改，你一般需要4个urls, 4个视图函数或通用视图和4个模板。当一个项目比较大包含多个app时，而每个app又包含多个模型(数据表)时, 那么编写和维护整个项目管理后台的工作量可想而知。Django Admin所做就是将所有需要管理的模型(数据表)集中在一个平台，你不仅可以选择性地管理模型(数据表), 你还可以快速订制数据条目查询，过滤和搜索条件。



**创建超级用户superuser**



使用django admin的第一步是创建超级用户(superuser)。进入你的项目文件夹, 使用如下命名，输入用户名和密码即可创建管理员。

```
$ python manage.py createsuperuser
```

此时你访问http://127.0.0.1:8000/admin/, 你就可以看到登录界面了。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjg7UHRDyJ4OPWmBENmQ4cVLZc7fzs7oFlqaXak91unD4K4iaLQZQn1GlA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**
**

**注册模型(数据表)**



假设你有一个叫blog的APP, 里面包含了一个叫Article(文章)的模型, 你想对文章进行管理, 你只需找到blgo的admin.py，使用admin.site.register方法注册Article模型。代码如下所示:

\#blog/admin.py

```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```

此时你登录后看到Article数据表默认是这样的，点击标题即可对文章进行修改。只有Title字段被显示，太简单。没有显示作者，没有显示发布日期，也没有分页，没有过滤条件。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjg3olpK4mAibWBaa80DLMHD5dy7EX2TOsOsxJX6ib6rwD5vv5yh3BJib6Fg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**
**

**自定义数据表显示选项**



我们需要自定义数据表中哪些字段可以显示，哪些字段可以编辑，并对数据表中的条目进行排序，同时定义过滤选项。Django的ModelAdmin自带的list_display, list_filter, list_per_page, list_editable, date_hierarchy和ordering选项可以轻松帮我们做到。



要自定义数据表显示字段，我们只需对上述代码做出如下改进。我们先定义ArticleAdmin类，然后使用admin.site.register(Article, ArticleAdmin)方法即可。

\#blog/admin.py

```python
from django.contrib import admin
from .models import Article, 

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ('title', 'author',  'status', 'mod_date',)

    '''设置过滤选项'''
    list_filter = ('status', 'pub_date', )

    '''每页显示条目数'''
    list_per_page = 5

    '''设置可编辑字段'''
    list_editable = ('status',)

    '''按日期月份筛选'''
    date_hierarchy = 'pub_date'

    '''按发布日期排序'''
    ordering = ('-mod_date',)

admin.site.register(Article, ArticleAdmin)
```

新的展示效果如下，是不是好多了? 试想下, 如果你要手动编写代码实现同样的功能，你需要多编写多少代码?

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgVHzzT0gxnEvMvzJ290nMtJibHAAu1fhA3p1A80t2GicWVSLnANSbNwNQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

另外两个常用选项是 list_display_links和search_fields。前者设置带链接的字段，比如本例中带链接的字段为('title'), 后期设置可以搜索的字段，如('title', 'body')，方便快速查询需要修改的数据表条目。**注意**: list_display不能用在多对多字段上哦。



**单对多关系的选择之raw_id_fields选项**

**
**

假设我们有一个Category模型如下所示， 其有一个父类(ForeignKey)，因为一个父类可能有多个子类。

```python
class Category(models.Model):
    """文章分类"""
    name = models.CharField('分类名', max_length=30, unique=True)
    slug = models.SlugField('slug', max_length=40)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True, on_delete=models.CASCADE)
```

我们现在把Category模型添加如admin，由于我们需要根据类别名(name)生成slug，我们所以还使用了prepopulated_fields选项。

\#blog/admin.py

```python
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
```

效果图如下左图所示。由于Django admin默认的单对多关系的选择器是下拉菜单，假设ForeignKey非常的多，那么下拉菜单将非常长，不便于用户选择。一个更好的方法是对ForeignKey使用raw_id_fields选项(如右图所示)。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgf7Qk7735HYUAoUnnn9wZ6GOVLzIuOdKIRS7dCcYN9Viciaam40cvP7BQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

改进过的代码如下所示，我们将看到下来菜单变成了放大镜。

```python
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ("parent_category", )

admin.site.register(Category, CategoryAdmin)
```



**多对多关系的选择之filter_horizontal选项**



由于Django admin默认的多对多关系(ManyToMany)选择器是复选框，非常的不好用。一个更好的方法是使用filter_horizontal或filter_vertical选项，如下图所示:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgHcQoJVGheJHI4xa1ppGUXqThs9wmIdK4oaonLVTsYbesQrYp8Thviag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)



**显示多个数据表数据在同一页面上之InlineModelAdmin类**



一个类别包含多篇文章，假设我们希望在查看编辑某个类别信息时，一同显示并编辑同属该类别下的所有文章信息，我们可以定义先定义ArticleInline类，然后把其附在CategoryAdmin里。这样我们就可以实现在同一页面上编辑类别和所属文章信息了，是不是很帅?

\#blog/admin.py

```python
from django.contrib import admin
from .models import Article, Category, Tag

class ArticleInline(admin.TabularInline):
    model = Article
    '''设置列表可显示的字段'''
    fields = ('title', 'author',  'status', 'mod_date',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ("parent_category", )
    inlines = [ArticleInline, ]

admin.site.register(Category, CategoryAdmin)
```

展示效果如下所示。试想下，你想手动编写同样代码又要花多长时间？估计使用Mixins和Formsets早就让你心烦意乱了吧。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgibfB65pXd7d5lnh4dIbX9HvIiaSMSich6sJvGoqUjoQdOjfzHJvoug4mg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Django提供了两个InlineModelAdmin的子类:TabularInline和StackedInline，区别在于使用的模板, 一个横着，一个竖着，选项是一样的。InlineModelAdmin和ModelAdmin共同的常用options有：

form
fieldsets
fields
exclude
filter_horizontal
filter_vertical
ordering
prepopulated_fields
get_queryset()
radio_fields
readonly_fields
raw_id_fields



额外增加的options有：

InlineModelAdmin.model
inline使用的model，必需。

InlineModelAdmin.fk_name
model的name，当有多个外键时使用。

InlineModelAdmin.formset
缺省BaseInlineFormSet。

InlineModelAdmin.form
缺省ModelForm。当创建formset时传递给inlineformset_factory()。

InlineModelAdmin.extra
inline的额外数目。

InlineModelAdmin.get_extra()也返回inline的额外数目。

InlineModelAdmin.max_num
可展示得最大数目。

InlineModelAdmin.get_max_num()也返回此数字。

InlineModelAdmin.min_num
可展示的最小数目。

InlineModelAdmin.get_min_num()也返回此数目。

InlineModelAdmin.raw_id_fields



使用InlineModelAdmin一定要注意以下几点哦。

- InlineModelAdmin不支持使用list_display选项，而要使用fileds或exclude选项来设置所数据表需要显示的字段。
- 当一个model有多个ForeignKey时，必需使用fk_name来设置主键。


**修改Admin的标题Title(标题)和Header(头部)**



你是否早已厌倦了Django Admin模板里的Django Administration这句话? 要修改这句话也非常简单，在你的blog/admin.py里加入下面两句话即可，无需修改什么模板。

\#blog/admin.py

```python
admin.site.site_header = 'Blog Administration'
admin.site.site_header = 'Blog Administration'
```

展示效果如下:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgBhdsmDjhWG5qmAkKSCfElvWAuXEKiah9D9htp5DdGnQ9wGeicmEz44yw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**小结**

本文详细总结了如何使用Django自带的admin快速开发管理后台，设置数据表显示选项，如何处理单对多和多对多关系的选择， 如何在同一页面上显示多个数据表，以及修改admin的标题。下文我们将介绍admin后台save方法的重写及其它高级知识，欢迎关注我们的微信。



# 中篇

**自定义list_display**

**
**

前文中我们已经介绍过django admin的list_display选项不能用于显示多对多的字段(如tags)。如果需要通过list_display选项显示多对多的字段或模型中原本不存在的字段或方法，我们需要新增自定义的list_play方法。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgVHzzT0gxnEvMvzJ290nMtJibHAAu1fhA3p1A80t2GicWVSLnANSbNwNQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

我们现在ArticleAdmin里重新定义一个show_tags方法，该方法有2个变量self和obj。我们先调用obj.tags.all()获取某篇文章obj的所有tags，然后使用join方法将它们连接成字符串。由于show_tags这个名字作为表单的header读起来并不友好，我们可以通过设置该方法的short_description属性来设置表头显示为"标签".

\#blog/admin.py

```python
class ArticleAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ('title', 'author',  'status', 'mod_date', 'show_tags')

    '''展示tags'''
    def show_tags(self, obj):
        tag_list = []
        for tag in obj.tags.all():
            tag_list.append(tag.name)
        return ','.join(tag_list)

    show_tags.short_description = '标签'  # 设置表头
```

显示效果如下:![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoA41hJD2jnm9H7DpsL8gu3EoscXouEZT7aKyYnRbTgrM7myVqia5tMYDZicdveM8zFsBbdTfo0dta7w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

你注意到上面图片有个问题没有？当标签为空的时候，显示内容为空白。有的时候我们需要设置空白值(empty value)来更好地提示用户，有的时候我们还要以不同颜色显示提示信息。下面我们就要对admin.py做些改进，当文章没有标签时，我们以红色字体显示没有"没有标签"。在下面中我们使用了format_html方法对字符串添加了样式。

\#blog/admin.py

```python
from django.contrib import admin
from .models import Article, Category, Tag
from django.utils.html import format_html

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ('title', 'author',  'status', 'mod_date', 'show_tags')

    '''展示tags'''
    def show_tags(self, obj):
        tag_list = []
        tags = obj.tags.all()
        if tags:
            for tag in tags:
                tag_list.append(tag.name)
            return ','.join(tag_list)
        else:
            return format_html(
                '<span style="color:red;">文章{}无标签</span>',
                obj.id,)

    '''设置表头'''
    show_tags.short_description = '标签'  # 设置表头
    
admin.site.register(Article, ArticleAdmin)
```

改进的展示效果如下:

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoA41hJD2jnm9H7DpsL8gu3E9icuWUE118ZO8xyLJrPbQFWhOp0r61gOOdnONCp5x6xSibNfXMfHyS5g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**注意**:

- 尽管我们实现了在列表中显示多对多的字段，但在实际项目中我们并不建议这么做，因为这额外地增加了许多数据库查询的工作量。

- 获取某篇文章obj所对应的tags正确方法是使用obj.tags.all()而不是obj.tags.all, 否则会出现tags is not iterable的错误。你需要了解，obj.tags.all方法仅限于在模板中使用，在admin或view中使用时，千万别忘了加括号。

  

- 

在本例中我们手动编写了需要显示的empty value。Django实际上是允许我们给所有的空字段设置显示名字的，我们只需要使用empty_value_display选项即可。我们还可以通过设置admin_order_field选项设置需要排序的字段。设置了admin_order_field选项的字段表头会出现一个小三角按钮，用户可以点击三角按钮实现正序或逆序排列。使用例子如下所示:

```
empty_value_display = "空值"
admin_order_field = ('title', 'mod_date')
```



**自定义list_filter**



自定义list_filter也是一个非常有用的Django技术，可以让用户快速找到自己需要查看或编辑的对象。在之前的案例中，我们的list_filter已经实现了按文章状态和发布时间对文章进行过滤。现在我们需要自定义一个过滤器，按文章标题所含的关键词(比如python, django)对所有文章进行过滤, 并显示在右边的过滤条件栏目里。

**![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoCQlOFHhVqSFzEHPPIzzLjgVHzzT0gxnEvMvzJ290nMtJibHAAu1fhA3p1A80t2GicWVSLnANSbNwNQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)**

完整代码如下。我们定义了一个TitleKeywordFilter类，该类继承了admin的SimpleListFilter类。我们设置了过滤器的标题和参数名(keyword), 并通过lookups方法定义了过滤参数元组，并调用queryset方法返回符合查询条件的查询数据集。



```
from django.contrib import admin
from .models import Article, Category, Tag

class TitleKeywordFilter(admin.SimpleListFilter):
    #  右侧栏人为可读的标题
   title = '标题关键词'

    # 在url中显示的参数名，如?keyword=xxx.
    parameter_name = 'keyword'

    """
    自定义需要筛选的参数元组. 
    """
    def lookups(self, request, model_admin):
        return (
            ('python', '含python文章'),
            ('django', '含django文章'),
             )

    def queryset(self, request, queryset):
        """
        调用self.value()获取url中的参数， 然后筛选所需的queryset.
        """
        if self.value() == 'python':
            return queryset.filter(title__icontains='python')
        if self.value() == 'django':
            return queryset.filter(title__icontains='django')


class ArticleAdmin(admin.ModelAdmin):

    '''设置过滤选项'''
    list_filter = ('status', TitleKeywordFilter, 'pub_date', )
```

展示效果如下所示, 是不是很帅?

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoA41hJD2jnm9H7DpsL8gu3EcuYHriaq2gDqu28G8E9n4ibeXicRIfKpaz5UZWEFtyl4dxiaib0vFA3GUJw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**注意:**

- 自定义的Filter类的代码必需放在ModelAdmin类的前面，否则无法使用。
- 自定义的Filter参数名parameter_name不要使用q和next，这两个参数已作为django admin的默认参数使用了。



**重写Django admin的save_model方法**



很多时候，我们需要重写Django自带的save_model方法。比如在文章创建时我们希望在后台自动添加作者，而不是允许用户自己选择作者是谁，我们可以选择在创建文章的表单里把作者隐藏，而在后台添加作者。如下所示:

```
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
```

在我们[世界那么大，我想去看看。Django仿制微信朋友圈九宫格相册(1)](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483833&idx=1&sn=b75c1c2adfbafbb1356f8a078218c206&chksm=a73c6181904be897b32c043920b0407053789ac73ddcc65fcdfb161351fac30ac265a6193cbb&scene=21#wechat_redirect)一文中我们也展示了save_model方法的重写，该方法作用是允许用户在创建Album对象时，还上传一个zip文件包。上传后对zip文件包进行解压存储，并与每个Image对象想关联。

\# album/forms.py

```
from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)
```

\# album/admin.py

```
import os
import uuid
import zipfile
from django.contrib import admin
from django.core.files.base import ContentFile
from .models import Album, AlbumImage
from .forms import AlbumForm


@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    form = AlbumForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'thumb')
    list_filter = ('create_date',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save()

            if form.cleaned_data['zip'] is not None:
                zip = zipfile.ZipFile(form.cleaned_data['zip'])
                for filename in sorted(zip.namelist()):

                    file_name = os.path.basename(filename)
                    if not file_name:
                        continue

                    data = zip.read(filename)
                    contentfile = ContentFile(data)

                    img = AlbumImage()
                    img.album = album
                    filename = '{0}{1}.jpg'.format(album.slug[:8], str(uuid.uuid4())[-13:])
                    img.alt = filename
                    img.image.save(filename, contentfile)

                    img.thumb.save('thumb-{0}'.format(filename), contentfile)
                    img.save()
                zip.close()
            super().save_model(request, obj, form, change)
```

还记得我们[Django 2.0 项目实战: 扩展Django自带User模型，实现用户注册与登录](http://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483696&idx=1&sn=6c01e4f01dd274b05a0887a1ff04ad8a&chksm=a73c6108904be81e369adea15cfec39ced7cac33e4c68564477b2755c7fb0b11c7419b2a28eb&scene=21#wechat_redirect)中对django的User模型做的扩展吗？我们新建了一个UserProfile模型，其与User是一对一的关系。我们现在希望在admin中创建一个User对象时，也同时创建一个UserProfile对象，这时我们就需要用到save_model方法的重写了。代码如下所示:

\#myaccount/admin.py

```
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    exclude = ["uid", "join_date", "mod_date"]


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.save()

        super().save_model(request, obj, form, change)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'org', 'join_date')
    exclude = []
    ordering = ('-join_date',)


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
```

展示效果如下。我们使用了Inlines使UserProfile与User展示在同一页面上。由于我们重写了save_model方法，这样可以自动在创建User时也创建UserProfile，避免了只创建User而未创建UserProfile的错误，这对1对1的关系非常重要。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoA41hJD2jnm9H7DpsL8gu3EtUkKCBGJTa63hcXJCTB0O6aQHJ1KqibduibyXTukn53XSKdicxvgsrnicQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**重写Django admin的get_queryset方法**



Django的admin默认会展示所有对象。通过重写get_queryset方法，我们可以控制所需要获取的对象。比如下例中，我们先对用户进行判定，如果用户是超级用户就展示所有文章，如果不是超级用户，我们仅展示用户自己所发表的文章。

```
class ArticleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
```

## 下篇

**谓action及如何自定义action**

action即动作，是你对一个选定查询集(queryset)要进行的操作。当你选定一个查询集(queryset)后，你可以点击action下拉菜单选择action，然后点击Go对其进行批量操作(如下所示)。Django admin默认的action只有删除(delete)。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoDokCEibyp9VFE624sQssH97jrluuS95o6ibwaxjRiaLibW27k3vibgExV7uASasxbYibybIKQoXticEmw4Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

现在如果你要将文章由草案(draft)状态变为发表(published)状态，你只能一个一个地修改, 很麻烦。现在我们可以自定义一个action，实现文章状态的批量修改。代码如下所示:

\#blog/admin.py

```python
class ArticleAdmin(admin.ModelAdmin):
   
    '''设置列表可显示的字段'''
    list_display = ('title', 'author',  'status', 'mod_date', 'show_tags')

    '''自定义actions'''
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='p')

    make_published.short_description = "发布所选文章"
```

我们自定义了一个名为make_published的方法，并将其加入到了ArticleAdmin的actions属性(别忘了加引号哦)。我们还给该方法添加了一个简单描述(short_description)。现在如果你刷新页面，你就可以看到action下面多了一个"发布所选文章的"选项了。

![Image](https://mmbiz.qpic.cn/mmbiz_png/buaFLFKicRoDokCEibyp9VFE624sQssH97rc61Jn6Ceic7LJXLkzPWXAmuvEaVhd2bl7bfKhlY4af7lvNRn4FsXkg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

本例中使用了queryset.update方法实现了数据批量更新, 提升了工作效率。如果你想对queryset中的对象一个一个修改或导出，你应该怎么办呢? 此时你可以遍历queryset，对单个obj逐一处理, 如下所示:

```
def action_func(self, request, queryset):
    for obj in queryset:
        do_something(obj)
```



**action的权限管理**

一个网站可能有多个人员有权限登录管理后台，如果每个人都有delete或导出数据的权限，是件挺可怕的事情。万一哪天某人对公司不满意清空数据或导出所有客户数据跑路呢？ 所以我们必需对action也设定一定的权限。实现这个只需定义allowed_permissions属性即可。下例中要求只有change权限的管理人员才能更改文章发表状态。

```
make_published.allowed_permissions = ('change',)
```

下例中我们重写了get_actions方法，只给了用户名为John批量删除对象的权限。如果用户名不为John，我们把delete_selected动作从下拉菜单中删除。

```python
class ArticleAdmin(admin.ModelAdmin):

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.use.username != 'John':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions
```



**自定义显示表单**

如果我们想实现根据不同的用户显示不同表单form，我们可以通过重写get_form方法实现。如下例中给Superuser显示了不同的表单。

```python
class MyModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = MySuperuserForm
        return super().get_form(request, obj, **kwargs)
```



**自定义显示表单的ForeinKey字段**

django admin对于一个字段默认会显示所有的ForeignKey(比如文章类别)。下利中通过重写formfiled_for_foreignkey方法可只显示用户自己创建的文章类别。

```python
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "cateogry":
            kwargs["queryset"] = Category.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
```



**自定义显示表单的多对多字段**

通过重写formfiled_for_manytomany方法可只显示用户自己创建的多对多字段。

```
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "cars":
            kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
```



**自定义显示表单的Choice字段**

下例中通过重写formfiled_for_choice_field方法给superuser多了一个选择。

```
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "status":
            kwargs['choices'] = (
                ('accepted', 'Accepted'),
                ('denied', 'Denied'),
            )
            if request.user.is_superuser:
                kwargs['choices'] += (('ready', 'Ready for deployment'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)
```



**自定义搜索选项search_field**

如果你定义了搜索选项search_field, django admin上就会出现一个搜索框，允许你按定义的字段快速搜索一个对象。注意search_field只能用于CharField或TextField。

```
search_fields = ['title', 'user__email'] # 按文章title和用户email搜索
search_fields = ['user__first_name'] # 按用户first name模糊查询icontains
search_fields = ['user__first_name__iexact'] # 按用户first name精确匹配
```



**如何美化Django的admin**

**如果你不使用第三方的库如django-xadmin, 你唯一能够美化django admin的方法就是覆盖它本来的模板。默认的django模板是放在contrib/admin/templates/admin目录下的**。django的模板美化可以针对某个项目(project), 某个应用(app)或某个模型(model)来进行，提供了非常大的灵活度。



\1. 针对项目(**project**)全站美化。

按如下顺序新建目录，**拷**入新的模板修改即可。

**my_project/templates/admin/**

**
**

**2. 针对应用(app)美化。**

***\*按如下顺序新建目录，拷入新的模板修改即可。\****

***\**\*my_project/templates/admin/my_app\*\**\***

***\**\*
\*\**\***

**2. 针对模型(model)美化。**

***\*按如下顺序新建目录，放入新的模板即可。\****

***\*my_project/templates/admin/my_app/model_name\****