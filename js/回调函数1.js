const fn = () => {
    setTimeout(console.log(), 5200)
}
//如上有问题，一般箭头函数是用来返回的

// const fn0 = () => {
//     console.log("hewll world!!");
// }

// function fn1() {
//     setTimeout(fn0, 3000)
// }

// let rs = fn1() //这样直接是拿不到数据的

// function fn2(date) {
//     return date
// }
//=============================================================================
// function tea(fn) {
//     setTimeout(fn, 5000) //标志为【函数的定义】  注意这里的fn是不能写参数.
// };
// tea(() => {
//     console.log("dfsdfas");
// }) //这样写是没有问题，不传参数的话，如果要传参数，可能要打包了。因为在【函数的定义】写fn("参数")，别人以为（）是已经exceute了，所以改进
// console.log('=============================================================================');
// ((date) => {
//     console.log(date);
// })()  
//自调


function tea1(fn) {
    function fn1() {
        fn("在这里写实参数咯！！") //这里就打包了一层
    }
    setTimeout(fn1, 5000)
}

// tea1((date) => {
//     console.log("在这里写的是形参" + date);
//     return date;
// })
//如下没办法给rz赋值的
const rz = tea1((date) => {
    // console.log("在这里写的是形参" + date);
    return date;
})

console.log(typeof (rz));

const rz1 = tea1
console.log(rz1 == tea1);

//=============================================================================



//定义 一个普通 函数
// function abc() {
//     console.log("理解下settimeout");
// }
// setTimeout(abc, 3000);