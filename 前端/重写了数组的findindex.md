```
*var* ages = [3, 10, 18, 20];

ages.myindexfind1 = *function* (*fn*) {

  *var* a = []

  ages.forEach(*item* *=>* {

​    a.push(fn(*item*))

  })

  return a.indexOf(true)

}

*var* q = ages.myindexfind1((*age*) *=>* {

  return *age* >= 9;

})

console.log(q);
```

//如上是定义对象的myindexfind1方法.这个方法是一个方法函数.这个函数有一个函数参数fn

//这个方法函数调用执行过程如下:

//1 声明一个a数组

//2 按数组的长度,执行参数函数,并默认传递数组的对象item给这个参数函数 fn为参数.

//3 fn 的实现为一个条件

//4 将fn 的条件结果使用 a数组记录

//5 返回条件结果成立的第一个index



