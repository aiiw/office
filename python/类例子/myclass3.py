
class people:
    #定义基本属性
    name = 'ww'
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,a,n):
        self.name = n
        self.age = a
        self.speak()  #有些函数会在初始化对象的时候执行了,就是在这个位置定义了函数
        # self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = '11'
   
    def speak(self):
        print("我在读 %s 年级"%(self.grade))
 
 
 
p=people(6,'a')
s = student(3,'a')
# print (s.speak())
