// var ages = [3, 10, 18, 20];

// // 第一种可以实现的办法
// function myindexfind(fn) {

//     for (i = 0; i < ages.length; i++) {
//         var a = fn(ages[i])
//         if (a != "没有")
//             break
//     }
//     return a
// }

// let rz = myindexfind((a) => {
//     return a > 3 ? a : "没有"
// })

// console.log(rz);

//第二种办法 未解决的
//Array.prototype.a = function() {
//   // 方法逻辑
// };
var ages = [3, 10, 18, 20];
ages.myindexfind1 = function (fn) {
    var a = []
    ages.forEach(item => {
        a.push(fn(item))
    })
    return a.indexOf(true)

}
//如上是定义对象的myindexfind1方法.这个方法是一个方法函数.这个函数有一个函数参数fn
//这个方法函数调用执行过程如下:
//1 声明一个a数组
//2 按数组的长度,执行参数函数,并默认传递数组的对象item给这个参数函数 fn为参数.
//3 fn 的实现为一个条件
//4 将fn 的条件结果使用 a数组记录
//5 返回条件结果成立的第一个index

var q = ages.myindexfind1((age) => {
    return age >= 19;
})

console.log(q);


// 如上等价
console.log(ages.findIndex((age) => {
    return age >= 19
}));


//===============================================================================================
// console.log(ages.indexOf(3));  这个是根据值去查索引

console.log(ages.filter((age) => {
    return age >= 19
}));