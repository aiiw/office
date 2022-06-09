# Django实现任意文件上传（最简单的方法）

利用Django实现文件上传并且保存到指定路径下，其实并不困难，完全不需要用到django的forms，也不需要django的models，就可以实现，下面开始实现。

第一步：在模板文件中，创建一个form表单，需要特别注意的是，在有文件上传的form表单中，method属性必须为post，而且必须指定它的enctype为"multipart/form-data"，表明不对字符进行编码，具体的代码如下：

    <form enctype="multipart/form-data" action="/uploadFile/" method="post">
       <input type="file" name="myfile" />
       <br/>
       <input type="submit" value="upload"/>
    </form>

第二步：设置urls.py文件，指定相应的视图函数进行处理

第三步：最重要的，在视图函数中做处理，先把代码贴出来，一共就这么点，可以实现任何格式文件的上传

def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            returnHttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        returnHttpResponse("upload over!")
代码就是上面这些。

这里需要对上面视图函数中的代码进行详细的解释一番：

首先，对于上传的文件，虽然是通过POST的方式上传的，但是不能通过request.POST["myfile"]或者request.POST.get("myfile", None)，这两种方式来访问，这里需要使用另外一种方式，就是：

           request.FILES["myfile"]或者request.FILES.get("myfile", None)

因为上传的文件是保存在FILES这个字典中的，可以在if request.method =="POST"之前加上一句assert False，再运行浏览器，就可以看到结果。


接下来，需要判断用户是不是真的上传了文件，如果用户仅仅只是点了 一下upload按键，那么就提示他没有上传文件。


下面是最重要的部分，现在已经得到了文件了，但是文件在内存中，没有写到硬盘里面去，接下里需要完成的就是把文件写入到硬盘，那到底该怎么写，我看了很多人的博客，写的云里雾里的，都没有说清楚，把我搞糊涂了。

其实上传文件，就是把硬盘里面某个文件的数据，写入到服务器指定的文件中，在最底层不管是txt文件还是exe文件等，全都是二进制的数据，这里所要做的只是将已经上传了的文件的数据，以二进制的方式写入到服务器指定的文件中，这个文件可以随意命名。

比如可以将上传的123.exe文件，保存为abc.txt，但是这毫无意义，对于上传的123.exe，在服务器上也应该是123.exe。其实在这里所说的abc.txt和123.exe的内容是完全一样的，只需要将abc.txt的文件后缀改为exe就行了。

 

在进行进一步的代码解释之前，需要先讲几个关于上传文件的方法和属性：

    myFile.read()：从文件中读取整个上传的数据，这个方法只适合小文件；
    
    myFile.chunks()：按块返回文件，通过在for循环中进行迭代，可以将大文件按块写入到服务器中；

   myFile.multiple_chunks()：这个方法根据myFile的大小，返回True或者False，当myFile文件大于2.5M(默认为2.5M，可以调整)时，该方法返回True，否则返回False，因此可以根据该方法来选择选用read方法读取还是采用chunks方法：

      if myFile.multiple_chunks() == False:
    
         # 使用myFile.read()
    
      else:
    
         # 使用myFile.chunks()

   myFile.name：这是一个属性，不是方法，该属性得到上传的文件名，包括后缀，如123.exe；

   myFile.size：这也是一个属性，该属性得到上传文件的大小。

 

接下来的一行代码是：

   destination = open(os.path.join("E:\\upload",myFile.name), 'wb+')

这一行代码需要用到os模块，import os。对于os.path.join("E:\\upload", myFile.name)，如果上传的文件为123.exe，那么将得到E:\\upload\\123.exe这个路径，以写二进制的方式打开这个文件。接下来是分块写入数据：

   for chunk in myFile.chunks():      # 分块写入文件

      destination.write(chunk)

数据写完之后关闭文件就可以了，destination.close()。


首先选择文件：


点击upload，显示upload over!


查看指定目录下是否有相应的上传文件：

 

最后需要说明：网上很多博客在讲django上传文件的时候都使用了django的forms，那其实不是必须的；还有就是models，它的作用仅仅只是用于保存上传文件的路径，与之相应的还有settings.py文件中的MEDIA_ROOT，这个值也只是在使用models的时候才有用。对于我这样的初学者而言，还是先单独的把上传功能实现，其余的功能在实现了基础功能后在附加上去就行了。
————————————————
版权声明：本文为CSDN博主「JiangPF1992」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/jiangpf1992/article/details/49406879/