class Animal():
    ##类里定义的属性称为类属性
    count=0
 
    ##构造函数,实例化的时候会自动调用该函数
    def __init__(self,name,age,sex):
        ##构造函数里定义的字段称为实例属性
        self.name=name
        self.age=age
        self.sex=sex
        self.__class__.count+=1
        self.count+=1
        print('名字叫:'+self.name+',年龄'+str(self.age)+'岁,性别品种是:'+self.sex)
        print('类动物数量:'+str(self.__class__.count))
        print('实例动物数量:'+str(self.count))
        print("*"*150)

if __name__ == '__main__':
    ##实例化Animal
    a1=Animal('狮子1',2,'公') #类中的()是继承,实例的()是参数,并且执行构造函数里的内容
    a2=Animal('狮子2',3,'公')
    a3=Animal('狮子3',4,'公')
