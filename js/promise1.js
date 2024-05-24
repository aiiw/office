function timeOut(delay = 100) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(
                "第一次"
            ); //A:这个地方是一个传出函数,理解下:传出函数一般是先出现在参数,然后再出现在函数体,出现在函数体是以触发调用形式. 实际要执行什么函数是在调用的时候落实.
            //其实也好理解 ,将传出函数理解为参数函数,参数函数=形参.在定义函数的时候只占位,实际参数在使用的时候赋值.
            //resolve的形参，就是than函数的实参
        }, delay)
    })
}



function id1() {
    let p = timeOut(2000)
    p.then((data) => { //then(传入函数),理解下:这里的传入函数.实际就是一个函数的定义.这里使用了箭头函数.(参数)=>{函数体}
        console.log(data + "234");
        return "123"; //如果不返回 promise 对象,则这里不会向下个then传值.
    }).then(() => {
        console.log('第二次');
    })
}
id1()

// id1() {
// /* <button onclick="id1()">id1第一个promise例子</button>
// <!-- 这个地方的注释 call 函数() -->
// <div>这里只会输出,两个结果,分别是"第一次"与"第二次"</div>