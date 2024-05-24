//其实js的参数，是一个对应关系，就算没有形参，也可以实参，不会报错。当然定义了形参，没有传递实参也不会报错。
function abc(fun) {
    function abc() {
        console.log("我也是一个嵌套函数");
    }
    fun(abc)
}

function go(a) {
    a()
}

abc(go)