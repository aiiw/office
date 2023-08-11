from django.http import HttpResponse
from django.shortcuts import render

def hello(request):

    return HttpResponse("Hello world ! ")
def r1(request):
    vt1 = 'Hello World!'
    return render(request, 'tp1.html', {'vt':vt1})
def r2(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "tp1.html", {"vt": views_list})
def r3(request):
    views_dict = {"name": "菜鸟教程"}
    return render(request, "tp1.html", {"vt": views_dict})
def req(request):
    dict1={'path1':request.path, 'meta1':request.META,'m1':request.method}
    return render(request,'testrequest.html',{"dict2":dict1})