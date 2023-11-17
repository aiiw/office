//测试settimeout 
function longRunningCallback() {
    console.log("开始执行长时间运行的回调函数");
    // 模拟长时间运行的操作
    const endTime = Date.now() + 1 * 1 * 1000; // 60分钟后的时间戳
    while (Date.now() < endTime) {
        // 空循环，模拟长时间运行的操作
    }
    console.log("长时间运行的回调函数执行结束");
    return ("这个是异步返回的数据")
}



function getsyndata() {
    setTimeout(() => {
        return longRunningCallback()
    }, 6000);
}


synjg = getsyndata()
console.log("hell", synjg);




// 一 同步的获取数据
let target = "hell wrold"

function getdata() {
    return target
}

const rz = getdata()
console.log(rz)

//二 异步的获取数据,,由于一般的getdata 是异步,所以仿真下这个环境测试下

// let target = "hell wrold"

// function getdata() {
//     setTimeout(() => {
//         return target
//     }, 3000)
// }

// const rz = getdata()
// console.log(rz)
//如上rz 是获取不到数据的
//通过回调函数实现，回调函数就是将函数当参数

// let target1 = "hell wrold"

// function getdata1(fnc) {
//     setTimeout(() => {
//         fnc(target1) //retrun 只能返回同步的数据
//     }, 6000)
// }

// const rz2 = getdata1((a) => {
//     // return a //retrun 是同步的，立即返回的
//     console.log(a)

// })
// console.log(rz2)
// console.log(b)

//第二种方法这个是使用 Promise
let target1 = "hell wrold1"

function getdata2() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(target1) //这里有一个疑问,如果写成settimeout(resolve,5000) 会是同步,立即执行.
        }, 5000)
    })
}
let p = getdata2()

p.then((data) => {
    console.log(data)
})


//第三种方法,使用 async await

async function fun() {
    let pthen = await getdata2() //这样就不用那么麻烦去取 resolve的中target1的数据了
    console.log(pthen)
}
fun()




//如下是一个同步的定时任务
// function abc() {
//     setTimeout(() => {
//         console.log("aaaaaaaaaaaaa")
//     }, 5000)
// }
// abc()
//一个同步的定时任务
//如下是将匿名函数抽出来
// function a() {
//     console.log("aaaaaaaaaaaaaaaaaaaa")
// }

// function abc() {
//     setTimeout(a, 5000)
// }
// abc()
// //一个同步的定时任务