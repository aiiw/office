// function a(b) {
//     b();
//     console.log("aaa");
// }

// function b() {
//     console.log("bbbb");
// }

// a(b);
// // bbbb
// // aaa
//如果您在异步函数中使用 await 关键字等待一个函数，而该函数没有返回一个 Promise 对象，那么会导致语法错误。
async function a(b) {
    await b();
    console.log("aaa");
}

async function b() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("bbb");
            resolve();
        }, 3000);
    });
}

a(b);

// bbb
// aaa
//如下例如模仿了python的time.sleep 阻挡主进程
//由于js是单线程的
//所以需要通过 async 和 await

//在使用 await 的函数longRunningCallback，必须是一个返回 Promise 对象的异步函数。 但这个函数不一定有async修改.
//在函数内使用了await ,则这个函数必须是一个async

// async function c(b) {
//     let p = await b();
//     console.log("aaa");
//     console.log(p)
// }

// async function d() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             console.log("bbb");
//             resolve("这个过程是一个io");
//         }, 3000);
//     });
// }
// c(d);