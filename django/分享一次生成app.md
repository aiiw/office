# 分享一次生成app.md



本次是根据数据库已经有的表进行反向生成app页面。

1. ###### 进行命令行，输入：python manage.py startapp mywx

2. ###### 在setting文件，注册app

3. ###### 反向生成model 参考文件

   ```
   python manage.py inspectdb wxuser> mywx/123.model
   ```

4. ###### 将123.model文件内容拷贝到 mywx/model

5. ###### 生成模型关系文件d

   ```
   $ python manage.py makemigrations mywx  # 让 Django 知道我们在我们的模型有一些变更
   $ python manage.py migrate mywx   # 创建表结
   ```

6. 

7. 编辑应用下的admin.py

   ```
   from django.contrib import admin
   
   # Register your models here.
   import xadmin
   from .models import WxUser
   # class test2():
   #     list_display=['周期','员工编号','平时加班时数','周末加班时数','节日加班时数','有薪假时数','法定假时数','基本工资','平均时薪','法定日平均工资','平时加班费','公休日加班费','节日加班费','有薪假工资','法定假工资','最低工资补助','计件工资','全勤奖','应发工资','工龄奖','公积金','社保','实发工资','个税','保健补助','应税额','id']
   #     search_fields = ['周期','员工编号','平时加班时数','周末加班时数','节日加班时数','有薪假时数','法定假时数','基本工资','平均时薪','法定日平均工资','平时加班费','公休日加班费','节日加班费','有薪假工资','法定假工资','最低工资补助','计件工资','全勤奖','应发工资','工龄奖','公积金','社保','实发工资','个税','保健补助','应税额','id']
   #     list_filter = ['周期','员工编号','平时加班时数','周末加班时数','节日加班时数','有薪假时数','法定假时数','基本工资','平均时薪','法定日平均工资','平时加班费','公休日加班费','节日加班费','有薪假工资','法定假工资','最低工资补助','计件工资','全勤奖','应发工资','工龄奖','公积金','社保','实发工资','个税','保健补助','应税额','id']
   #     show_detail_fields = ['员工编号']
   #     list_filter =['周期','员工编号',]
   #     refresh_times = (3,5)     # 数据刷新时间
   #     actions_on_bottom = True
   
   class wx():
       list_display=['oa部门','工号','姓名','微信旧部门id','微信旧部门',u'newdeptid']
   
   xadmin.site.register(WxUser,wx)
   
   ```

   