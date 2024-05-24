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

module.exports = timeOut