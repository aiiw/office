from django.shortcuts import render,HttpResponse
from . import models 
def add_book(request):
    books = models.Book.objects.all() 
    print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    vt=books
    return HttpResponse("<p>{{ vt }}</p>")