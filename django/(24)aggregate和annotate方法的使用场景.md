**aggregate和annotate方法的使用场景**

Django的aggregate和annotate方法属于高级查询方法，主要用于组合查询，是Django高手们必需要熟练掌握的。当我们需要对查询集(queryset)的某些字段进行计算或进行先分组再计算或排序, 我们就需要使用aggregate和annotate方法了。



假如我们有如下一个模型，其中Student与Hobby(爱好)是多对多的关系。我们想要知道所有学生的平均年龄，我们常规做法一般是利用for循环从数据库中把符合查询条件的student对象一个一个取出，把他们年龄相加，然后再除以总人数。当人数非常多而我们又只需要平均年龄这条信息时，把所有符合查询条件的学生对象都载入内存后再进行计算是非常浪费资源的，效率也非常低。一个更好的方法是在数据库层面提取查询数据时就直接返回我们所需要的信息。因为这个查询涉及到对整个queryset的age字段进行统计计算，此时django的聚合函数方法aggregate就可以帮我们大大提升查询效率了[见后文]。

```
class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hobbies = models.ManyToManyField(Hobby)
    
class Hobby(models.Model):
    name = models.CharField(max_length=20)
```

另一个例子是统计最受学生欢迎的5个爱好，常规做法是先将所有hobby对象提取出来，载入内存。然后利用for循环统计每组爱好对应的学生人数，再构建一个新的查询集，按每组人数从大到小进行排序。这个查询需要根据hobby先进行分组，再统计每个爱好组里学生的数量，然后进行排序。对于这个复杂查询, django的annotate方法一句话就可以解决问题。



**aggregate()方法详解**

aggregate的中文意思是聚合, 源于SQL的聚合函数。Django的aggregate()方法作用是对一组值(比如queryset的某个字段)进行统计计算，并以字典(Dict)格式返回统计计算结果。django的aggregate方法支持的聚合操作有AVG / COUNT / MAX / MIN /SUM 等。



我们现在来看下几组实际使用案例。使用前别忘了import Avg, Max, Min或者Sum方法哦

```
from django.db.models import Avg, Max, Min
```



\# 计算学生平均年龄, 返回字典。age和avg间是双下划线哦

Student.objects.all().aggregate(Avg('age'))

{ 'age__avg': 12 }



\# 学生平均年龄，返回字典。all()不是必须的。

Student.objects.aggregate(Avg('age'))

{ 'age__avg: 12' }



\# 计算学生总年龄, 返回字典。

Student.objects.aggregate(Sum('age'))

{ 'age__sum': 144 }



\# 学生平均年龄, 设置字典的key

Student.objects.aggregate(average_age = Avg('age'))

{ 'average_age': 12 }



\# 学生最大年龄，返回字典

Student.objects.aggregate(Max('age'))

{ 'age__max': 12 }



\# 同时获取学生年龄均值, 最大值和最小值, 返回字典

Student.objects.aggregate(Avg('age‘), Max('age‘), Min('age‘))

{ 'age__avg': 12, 'age__max': 18, 'age__min': 6, }



\# 根据Hobby反查学生最大年龄。查询字段student和age间有双下划线哦。

Hobby.objects.aggregate(Max('student__age'))

{ 'student__age__max': 12 }



你注意到了吗? aggregate方法返回Dict类型数据和django的内容对象(context object)是一样的哦。你可以很轻松地将结果传递给模板, 在模板中显示。



**annotate()方法详解**

annotate的中文意思是注释，小编我觉得是非常地词不达意，一个更好的理解是分组(Group By)。如果你想要对数据集先进行分组然后再进行某些聚合操作或排序时，需要使用annotate方法来实现。与aggregate方法不同的是，annotate方法返回结果的不仅仅是含有统计结果的一个字典，而是包含有新增统计字段的查询集(queryset）.



我们接下来也看下几个实际使用案例。



\# 按学生分组，统计每个学生的爱好数量

Student.objects.annotate(Count('hobbies'))



返回的结果依然是Student查询集，只不过多了hobbies__count这个字段。如果你不喜欢这个默认名字，你当然可以对这个字段进行自定义从而使它变得更直观。



\# 按学生分组，统计每个学生爱好数量，并自定义字段名

Student.objects.annotate(hobby_count_by_student=Count('hobbies'))



\# 按爱好分组，再统计每组学生数量。

Hobby.objects.annotate(Count('student'))



\# 按爱好分组，再统计每组学生最大年龄。

Hobby.objects.annotate(Max('student__age'))


**Annotate方法与Filter方法联用**

有时我们需要先对数据集先筛选再分组，有时我们还需要先分组再对查询集进行筛选。根据需求不同，我们可以合理地联用annotate方法和filter方法。注意: annotate和filter方法联用时使用顺序很重要。



\# 先按爱好分组，再统计每组学生数量, 然后筛选出学生数量大于1的爱好。

Hobby.objects.annotate(student_num=Count('student')).filter(student_num__gt=1)





\# 先按爱好分组，筛选出以'd'开头的爱好，再统计每组学生数量。

Hobby.objects.filter(name__startswith="d").annotate(student_num=Count('student‘))



**Annotate与order_by()联用**

我们同样可以使用order_by方法对annotate方法返回的数据集进行排序。



\# 先按爱好分组，再统计每组学生数量, 然后按每组学生数量大小对爱好排序。

Hobby.objects.annotate(student_num=Count('student‘)).order_by('student_num')



\# 统计最受学生欢迎的5个爱好。

Hobby.objects.annotate(student_num=Count('student‘)).order_by('-student_num')[:5]



**Annotate与values()联用**



我们在前例中按学生对象进行分组，我们同样可以按学生姓名name来进行分组。唯一区别是本例中，如果两个学生具有相同名字，那么他们的爱好数量将叠加。



\# 按学生名字分组，统计每个学生的爱好数量。

Student.objects.values('name').annotate(Count('hobbies'))



你还可以使用values方法从annotate返回的数据集里提取你所需要的字段，如下所示:

\# 按学生名字分组，统计每个学生的爱好数量。

Student.objects.annotate(hobby_count=Count('hobbies')).values('name', 'hobby_count')