//简单理解闭包就是为了封装变量,使变量只在函数内作用,不污染环境
//如果一个函数用到了它作用域外面的变量，那么这个变量和这个函数之间的环境就叫闭包。
function fun1() {
    let a = 10;
    let b = 20;

    function fun2() {
        return a + b
    }
    return fun2
}

let obj = fun1() //闭包是一个环境，是指一个函数里定义的一个函数，而内函数使用了外函数的变量，这样的环境。
//正常的函数执行完了，变量会消失，但是闭包使用了的变量不会。简单理解闭包就是为了封装变量,使变量只在函数内作用,不污染环境
let txt = obj()

console.log(txt)

//如上的例子不够清晰，主要闭包主要是防止不使用太多全局变量
//不使用闭包的方式
let num = 0

function myfun() {
    return num++
}


for (let x = 0; x < 10; x++) {
    const a = myfun()
    console.log(a);

}

//使用闭包的写法
function myfun1() {
    let a = 0

    function myfun2() {
        return a++
    }
    return myfun2
}
const a = myfun1()
for (let x = 0; x < 10; x++) {

    console.log(a());

}