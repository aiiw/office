//如下例如模仿了python的time.sleep 阻挡主进程
//由于js是单线程的
//所以需要通过 async 和 await

//在getsyndata使用 await 的函数longRunningCallback，它必须是一个返回 Promise 对象的异步函数。 但它不一定有async修改.
//在getsyndata函数内使用了await ,则这个函数必须是一个async

function longRunningCallback() {
    return new Promise((resolve) => {
        console.log("开始执行长时间运行的回调函数");
        // 模拟长时间运行的操作
        let a = 1;
        const endTime = Date.now() + 1 * 20 * 1000; // 20秒后的时间戳
        while (Date.now() < endTime) {
            // 空循环，模拟长时间运行的操作
            a = a + 1
        }
        console.log("长时间运行的回调函数执行结束");
        resolve(a);
    });
}

async function getsyndata() {
    return await new Promise((resolve) => {
        setTimeout(async () => {
            const result = await longRunningCallback(); //在使用 await 的函数longRunningCallback，必须是一个返回 Promise 对象的异步函数。但这个函数不一定有async修改.
            resolve(result);
        }, 6000);
    });
}

(async () => {
    const synjg = await getsyndata();
    console.log("结果：", synjg);
})();
console.log("这里还是会先打印出来吧");