
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):#这里去了people也没报错
    grade = ''
    def __init__(self,g):
        #调用父类的构函
       
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("我在读 %d 年级"%(self.grade))
        print(bbb)
 
 

s =student(3)#new 
a="aaa"
bbb="32323" #这就有点奇怪了
s.speak()