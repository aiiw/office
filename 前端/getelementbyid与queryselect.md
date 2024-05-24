getElementById与querySelector的区别
首先对获取元素的几个方法有所了解

getElementById()：返回对拥有指定id的第一个对象的引用
getElementsByName()：返回带有指定名称name的对象的集合。返回的是元素的数组，而不是一个元素（由于name不唯一）
getElementsByTagName()：返回带有指定标签名的对象集合

querySelector()：返回文档中匹配指定CSS选择器的第一个元素
querySelectorAll() ：返回文档中匹配的CSS选择器的所有元素节点列表（h5新增）
document.querySelector("p")      //获取文档中第一个 <p> 元素：
document.querySelector("#demo")     //获取文档中id="demo"的元素
document.querySelector(".example");   //获取文档中第一个 class="example" 的元素
document.querySelector("p.example");    //获取文档中 class="example"的第一个 <p> 元素
...... 
还可以写CSS的并集选择器、复合选择器等等。按照css规范来实现。
1
2
3
4
5
6
要知道的是querySelector()方法仅仅返回匹配指定选择器的第一个元素。你可以使用querySelectorAll() 方法替代去返回匹配指定选择器的所有的元素。返回的是节点列表NodeList 对象，可以通过索引访问，索引值从0开始。

例如：

// 获取文档中所有的 <p> 元素
var x = document.querySelectorAll("p"); 
// 通过索引访问，设置第一个 <p> 元素的背景颜色
x[0].style.backgroundColor = "red";
1
2
3
由于querySelector是按css规范来实现的，所以它传入的字符串中第一个字符不能是数字。

## 前三种getxxxByxxx获取的是动态集合，而querySelector获取的是静态集合。

简单的说就是，动态就是选出的元素会随文档改变，静态的不会，取出来之后就和文档的改变无关了。

getElementById性能更好，而querySelector按照CSS选择器规范，当在多级查找时，更为方便。
————————————————

