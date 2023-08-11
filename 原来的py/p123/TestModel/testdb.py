from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    #abc=request.GET[aiiw]
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    print(type(request.GET))
    print(abc)
    return HttpResponse("<p>数据添加成功！</p>"+message)