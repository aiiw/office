# (30)：模型(Models)的继承详解

**抽象模型继承(abstract model)**



假如我们有如下两个模型Article（文章)和Course(课程)模型。它们的模型中有很多共同的字段，比如作者、标题、创建日期和更新日期。这样写会造成大量的代码重复，一个更好的方式是提取两个模型共同的字段建立一个父类抽象模型(abstract model)，再建立子类模型去继承父类。

```python
class Article(models.Model):
    owner = models.ForeignKey(User, related_name='articles_related',
            on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_related',
            on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```



我们现在可以建立一个叫ItemBase的父类抽象模型，再分别建立Article和Course模型去继承它。上述代码简化为如下所示。



```python
class ItemBase(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

       class Meta:
        abstract = True
    def __str__(self):
        return self.title

class Article(ItemBase):
    body = models.TextField()

class Course(ItemBase):
    description = models.TextField()
```



**建立一个父类抽象模型，只需要在父类模型Meta选项中设置abstract=True。Django不会为抽象模型在数据库中生成自己的数据表**。父类Meta中的abstract=True也不会传递给子类。尽管我们在这里建立了三个模型，Django只会为Article和Course模型生成两个数据表，且每个数据表均包含了共有字段和自己独特的字段(如body和description)。同时子类模型也会继承父类里的方法，比如这里的__str__方法。当然你也可以在子类中重写父类的__str__方法，并额外添加自己的odering选项。



但上述代码有个小问题owner字段的related_name属性在模型继承时丢失了。我们需要根据子类模型的名字，生成差异化的related_name。这时我们只需在父类模型中设置related_name时引用应用名app_label（%(app_label)s)或者子类的类名(%(class)s)。这里我们使用了%(class)s，表示小写形式的当前子类的类名。这样模型继承后，每个子类模型会生成自己专属的related_name, 比如articles_related和courses_related。

```python
class ItemBase(models.Model):
    owner = models.ForeignKey(User,
related_name='%(class)s_related',
on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```



**多表模型继承(multi-table inheritance)**

Django的多表模型也可用来简化代码，其与抽象模型继承最大的区别在于Django也会为父类模型建立自己的数据表，同时隐式地在父类和子类之间建立一个一对一关系。比如下例中，我们删除了父类模型Meta选项中的abstract=True, 这样Django就会创建3个数据表。其中共有字段部分会存储在父类模型对应的数据表里，每个子类模型专属的字段会存在每个子类对应的数据表里。尽管共有字段是存在父类模型对应的数据表里，每个子类对象可以像使用自己数据表里的字段一样使用那些字段，比如article.title, course.owner。

```python
class ItemBase(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Article(ItemBase):
    body = models.TextField()

class Course(ItemBase):
    description = models.TextField()
```

在多表继承中，一般父类的Meta属性不会继承到子类中，但是ordering和 get_latest_by是可以继承的。如果子类不想继承父类的ordering的Meta选项，则可以手动显式的指定ordering=[]或者任何自己想要的值。



注意：多表继承中如果一个父类有多个子类，且子类不在关系中显式地指定related_name字段，django会引发验证错误。这是因为多表继承的时候，Django隐式地在父类和子类之间建立一个一对一关系，有时候父类与其他类的关系会从父类下移到子类中。



**代理模型(proxy model)**



如果我们只想改变某个模型的行为方法，而不是添加额外的字段或创建额外的数据表，我们就可以使用代理模型(proxy model)。设置一个代理模型，需要在子类模型Meta选项中设置proxy=True， Django不会为代理模型生成新的数据表。比如下例中MyPerson模型继承了Person模型，并指定按last_name排序, django不会MyPerson生成新的数据表。

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True
ordering = ['last_name']
```



在这里代理模型MyPerson可以和Person模型一样对Person对应的数据表进行各种各样的骚操作。

```
>>> p = Person.objects.create(first_name="john")
>>> MyPerson.objects.get(first_name="john")
```

有时候你需要给子类代理模型自定义Manager方法，你可以按如下操作。

```
from django.db import models

class NewManager(models.Manager):
    # ...
pass
class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True
```

但上述操作有个问题，其覆盖了父类的操作方法，比如MyPerson.objects.all()。如果你希望保留父类自带方法，同时提供新的Manager方法，可以按如下操作。

```
# Create an abstract class for the new manager.
class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True
class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True
```



其实Django还提供了第4种模型继承方式多重继承(multi inheritance), 主要涉及mixin类的继承与使用，我们后面会专题介绍。



**小结**

- Django提供了3种常用模型继承方式，抽象模型继承、多表继承和代理模型继承。

- 当你的多个模型有大量相同字段时，可使用抽象模型(abstract model)继承简化代码。

- 多表继承会隐式地在父类和子类之间建立一个一对一关系。

  

- 如果我们只想改变某个模型的行为方法，而不是添加额外的字段或创建额外的数据表，可使用代理模型(proxy model)。

- Django不会为抽象模型或代理模型创建新的数据表，会为多表继承中的每个模型创建自己的数据表。