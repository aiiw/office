class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("wowo")
        
    # 定义一个build方法，返回一个person实例对象，这个方法等价于Person()。
    @classmethod
    def build(cls):
        # cls()等于Person()
        p = cls("Tom", 18)
        return p
    def qq(self):
        self.number="10776663700000"
        def res():
            return self.number
        return res
 
if __name__ == '__main__':
    person = Person.build()
    qq=person.qq()
    print(str(qq()))

    class xue(Person):
        """docstring for xue"""
        def __init__(self, name, age,arg):
            super().__init__(name, age)
            self.arg = arg
        def qq(self):
            print("223")
            a=super().qq()
            return a
            
    xue1=xue("aiiw","1","test")
    a=xue1.qq()
    print(type(a))
    print(a())
