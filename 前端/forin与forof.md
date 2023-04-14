```
1.循环数组

区别一：for in 和 for of 都可以循环数组，for in 输出的是数组的index下标，而for of 输出的是数组的每一项的值。

const arr = [1,2,3,4]
 
// for ... in
for (const key in arr){
    console.log(key) // 输出 0,1,2,3
    }
 
// for ... of
for (const key of arr){
    console.log(key) // 输出 1,2,3,4
    }
2.循环对象

区别二：for in 可以遍历对象，for of 不能遍历对象，只能遍历带有iterator接口的，例如Set,Map,String,Array

const object = { name: 'lx', age: 23 }
    // for ... in
    for (const key in object) {
      console.log(key) // 输出 name,age
      console.log(object[key]) // 输出 lx,23
    }
 
    // for ... of
    for (const key of object) {
      console.log(key) // 报错 Uncaught TypeError: object is not iterable
    }
3.数组对象

const list = [{ name: 'lx' }, { age: 23 }]
    for (const val of list) {
      console.log(val) // 输出{ name: 'lx' }, { age: 23 }
      for (const key in val) {
        console.log(val[key]) // 输出 lx,23
      }

————————————————
版权声明：本文为CSDN博主「艾迪蛋·」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_43796489/article/details/119566594
```

