// JavaScript中的三个点（…）名叫扩展运算符，是在ES6中新增加的内容，它可以在函数调用/数组构造时，
//将数组表达式或者string在语法层面展开；还可以在构造字面量对象时将对象表达式按照key-value的方式展开
// 数组
var number = [1, 2, 1, 2, 4, 30, 4, 5, 6]
console.log("-------------------findIndex--------------------------")
const vy = number.findIndex((item) => {
    return item > 1 //这个是找索引,索引是从0开始
})
console.log(vy, number.findIndex((item) => {
    return item > 25
}))
console.log("--------------------三个点（…）--------------------------------")
console.log(...number) //1 2 3 4 5 6
console.log(number)
//对象
var man = {
    name: '蔡',
    height: 180
}
console.log({
    ...man
})
console.log({
    man //打印对象会是 这个格式{对象类型:{对象的属性构成}}
})
console.log("----------------------------------------------------")
//
//数组的复制
var arr1 = [1, 2, 3, 4, 5, 6]
var arr2 = [...arr1, 7]
arr2 // ['hello']
console.log("arr1.length", arr1.length, arr1[5], arr1 == arr2)
console.log("arr2.length", arr2.length, arr2[6], arr1 == arr2)
console.log(arr2[1].toString())
//对象的复制
var obj1 = {
    name: 'Steven'
}
var obj2 = {
    ...obj1,
    'a': 'b'
}
obj2 //  {name:'Steven'}
console.log("----------------------------------------------------")

console.log(obj1)
console.log(obj2)