// setTimeout(function () {
//     console.log("First");
//     setTimeout(function () {
//         console.log("Second");
//         setTimeout(function () {
//             console.log("Third");
//         }, 3000);
//     }, 2000);
// }, 1000);
// await 调用函数(SetTime),它必须是一个返回 Promise 对象的异步函数。 但它不一定有async修改
//内部使用了await 外部必须async,标志下这个是一个异步函数
function SetTime(t, content) {
    return new Promise((a, b) => {
        setTimeout(() => {
            a(content)
        }, t)
    })
}

(async () => {
    a = await SetTime(1000, 'First');
    console.log("在a会等等");
    console.log(a);
    b = await SetTime(2000, 'Second');
    console.log("在b会等等");
    console.log(b);
    c = await SetTime(3000, 'Third');
    console.log("在会等等");
    console.log(c);

})()