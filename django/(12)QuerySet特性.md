**什么是QuerySet**

QuerySet是Django提供的强大的数据库接口(API)。正是因为通过它，我们可以使用filter, exclude, get等方法进行数据库查询，而不需要使用原始的SQL语言与数据库进行交互。**从数据库中查询出来的结果一般是一个集合，这个集合叫就做 queryset**。



## uerySet是惰性的**

Django的QuerySet是惰性的。下例中article_list试图从数据库查询一个标题含有django的全部文章列表。

```python
article_list = Article.objects.filter(title__contains="django")
```

但是当我们定义article_list的时候，Django的数据接口QuerySet并没有对数据库进行任何查询。无论你加多少过滤条件，Django都不会对数据库进行查询。只有当你需要对article_list做进一步运算时（比如打印出查询结果，判断是否存在，统计查询结果长度)，Django才会真正执行对数据库的查询(见下例1)。这个过程被称为queryset的执行(evaluation)。Django这样设计的本意是尽量减少对数据库的无效操作，比如查询了结果而不用是计算资源的很大浪费。

```python
# example 1
for article in article_list:
    print(article.title)
    
```


**Django的QuerySet自带缓存(Cache)**

在例1中，当你遍历queryset(article_list)时，所有匹配的记录会从数据库获取。这些结果会载入内存并保存在queryset内置的cache中。这样如果你再次遍历或读取这个article_list时，Django就不需要重复查询了，这样也可以减少对数据库的查询。



下例中例2比例3要好，因为在你打印文章标题后，Django不仅执行了查询，还把查询到的article_list放在了缓存里。这个article_list是可以复用的。例3就不行了。

```python
# Example 2: Good
article_list = Article.objects.filter(title__contains="django")
for article in article_list:
    print(article.title)

# Example 3: Bad
for article in Article.objects.filter(title__contains="django"):
    print(article.title)
```



**用if也会导致queryset的执行**

不知道你注意到上述例2中有个问题没有？万一article_list是个空数据集呢? 虽然for....in...用到空集合上也不会出现raise什么错误，但专业优秀的我们怎么能允许这样的低级事情发生呢？最好的做法就是在loop前加个if判断（例4）。因为django会对执行过的queryset进行缓存(if也会导致queryset执行, 缓存article_list)，所以我们在遍历article_list时不用担心Django会对数据库进行二次查询。

```python
# Example 4: Good
article_list = Article.objects.filter(title__contains="django")
if article_list:
    for article in article_list:
        print(article.title)
else:
    print("No records")
```

但有时我们只希望了解查询的结果是否存在，而不需要使用整个数据集，这时if触发整个queryset的缓存变成了一件坏事情。哎，程序员要担心的事情着不少。这时你可以用exists()方法。与if判断不同，exists只会检查查询结果是否存在，返回True或False，而不会缓存article_list(见例5）。

```python
# Example 5: Good
article_list = Article.objects.filter(title__contains="django")
if article_list.exists():
    print("Records found.")
else:
    print("No records")
```

**注意**: 判断查询结果是否存在到底用if还是exists取决于你是否希望缓存查询数据集复用，如果是用if，反之用exists。



**统计查询结果数量优选count方法**

len()与count()均能统计查询结果的数量。一般来说count更快，因为它是从数据库层面直接获取查询结果的数量，而不是返回整个数据集，而len会导致queryset的执行，需要将整个queryset载入内存后才能统计其长度。但事情也没有绝对，如果数据集queryset已经在缓存里了，使用len更快，因为它不需要跟数据库再次打交道。



下面三个例子中，只有例7最差，尽量不要用。

```python
# Example 6: Good
count = Article.objects.filter(title__contains="django").count()

# Example 7:Bad
count = Article.objects.filter(title__contains="django").len()

# Example 8: Good
article_list = Article.objects.filter(title__contains="django")
if article_list:
    print("{} records found.".format(article_list.len()))
```



**当queryset非常大时，数据请按需去取**

当查询到的queryset的非常大时，会大量占用内存(缓存)。我们可以使用values和value_list方法按需提取数据。比如例1中我们只需要打印文章标题，这时我们完全没有必要把每篇文章对象的全部信息都提取出来载入到内存中。我们可以做如下改进（例9）。

```python
# Example 9: Good
article_list = Article.objects.filter(title__contains="django").values('title')
if article_list:
    print(article.title)


article_list = Article.objects.filter(title__contains="django").values_list('id', 'title')
if article_list:
    print(article.title)
```

**注意**: values和values_list返回的是字典形式字符串数据，而不是对象集合。如果不理解请不要乱用。



另外还可以使用iterator()方法可以优化程序对内存的使用，其工作原理是不对queryset进行缓存，而是采用迭代方法逐一返回查询结果，但这有时会增加数据库的访问次数，新手一般也驾驭不了。我这里就不细讲了。



**更新数据库部分字段请用update方法**

如果需要对数据库中的某条已有数据或某些字段进行更新，更好的方式是用update，而不是save方法。我们现在可以对比下面两个案例。例10中需要把整个Article对象的数据(标题，正文.....)先提取出来，缓存到内存中，变更信息后再写入数据库。而例11直接对标题做了更新，不需要把整个文章对象的数据载入内存，显然更高效。尽管单篇文章占用内存不多，但是万一用户非常多呢，那么占用的内存加起来也是很恐怖的。

```python
# Example 10: Bad
article = Article.objects.get(id=10)
Article.title = "Django"
article.save()

# Example 11: Good
Article.objects.filter(id=10).update(title='Django')
```

update方法还会返回已更新条目的数量，这点也非常有用。当然事情也没有绝对，save方法对于单个模型的更新还是很有优势的，比如save(commit=False), article.author = request.user等等事情update都做不来。



**专业地使用explain方法**

Django 2.1中QuerySet新增了explain方法，可以统计一个查询所消耗的执行时间。这可以帮助程序员更好地优化查询结果。

```python
print(Blog.objects.filter(title='My Blog').explain(verbose=True))

# output
Seq Scan on public.blog  (cost=0.00..35.50 rows=10 width=12) (actual time=0.004..0.004 rows=10 loops=1)
  Output: id, title
  Filter: (blog.title = 'My Blog'::bpchar)
Planning time: 0.064 ms
Execution time: 0.058 ms
```