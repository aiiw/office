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
            const result = await longRunningCallback();
            resolve(result);
        }, 6000);
    });
}

(async () => {
    const synjg = await getsyndata();
    console.log("结果：", synjg);
})();