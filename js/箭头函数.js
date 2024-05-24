//常规的函数传参
//一 定义参数函数 这个是参数,充当变量
const abc = function a() {
    console.log("aaaa")
    console.log(arguments);
}

// 定义函数
function calla(vv) {
    vv("这里可以传递实际参数", "可以传递多个参数") //javascript 可以允许传递的 实际参数 与 函数 定义 的 接收 形参不对等.
}
//调用函数
calla(abc) //abc 也是一个参数,是一个实际参数,其实也可以直接在这里定义,常用剪头函数



//使用箭头函数,不用做如上例子的第一步,用的时候再定义

function callb(vv) {
    vv("date==============")
}

callb((a) => {
    console.log(a)
})


// 如下是将箭头函数当表达式,使用,直接等于 function fn3()
//其实将函数赋值看是否有(),有就是执行函数后再返回结果,没有是函数赋值
const fn3 = (a = 10, b = 20, c = 30) => {
    console.log("a =", a);
    console.log("b =", b);
    console.log("c =", c);
}

fn3(1, 2)




//对象
obj1 = {
    a: "123456",
    b: abc
}

// console.log(obj1)

function callobj1(obj1) {
    console.log(obj1.a)

    obj1.b = (() => { //这里需要注意下,将箭头函数放到一个对象,需要外加一个括号
        console.log("aaaaaaffffffffffffffffffff")
    })
    obj1.b()
}

function callobj2(obj1) {
    console.log(obj1.a)
    obj1.b()
    obj1.b = (() => { //这里需要注意下,将箭头函数放到一个对象,需要外加一个括号
        console.log("aaaaaaffffffffffffffffffff")
    })
    obj1.b()
}
// callobj(obj1)
callobj1({
    a: '1234',
    b: (() => {
        console.log("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc") //注意这里不会输出aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc,因为在函数定义的时候给覆盖了,所以建议一般在调用函数的时候再实现参数函数.
    })
})

callobj2({
    a: '1234',
    b: (() => {
        console.log("abc") //注意这里输出abc,因为在覆盖前调用了。
    })
})

obj3 = {
    name: "jian",
    say() {
        console.log("aaabbbb") // 等于 say:function(){} 匿名
    }
}

obj3.say();


(() => {
    console.log("这是通过匿名函数生成的立即执行函数") //在使用立即执行函数时，需要在前面加上个;号
})();
// (function () {
//     alert("aaaaaaaaaaaaaadaaa")
// })()