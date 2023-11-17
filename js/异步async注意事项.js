// 在JavaScript中，如果一个函数被声明为异步函数（使用 async 关键字），
//并且在函数体内使用 return 返回一个值，
//那么这个值将会被隐式地包装在一个 Promise 对象中返回。

// 对于您提供的例子 async fn(){ return 123; }，当调用这个异步函数时，它会返回一个 Promise 对象，该对象已经被解决（resolved），
//并且其解决值为 123。也就是说，实际上返回的是一个解决状态的 Promise 对象，而不是单纯的数字 123。

// 您可以通过 then 方法或使用 await 来获取该异步函数返回的值：

//访问 promise 对象 的resolved.可以使用then.或者 await
async function example() {
    return 123;
}

example()
    .then(result => {
        console.log(result); // 输出 123
    })
    .catch(error => {
        console.error(error);
    });

// 或者使用 await
(async () => {
    const result = await example();
    console.log(result); // 输出 123
})();


// 注意，无论异步函数内部使用 return 返回的是什么值，它都会被自动包装成一个解决状态的 Promise 对象，以便进行异步处理。

// 希望这个解答对您有所帮助！如果您还有其他问题，请随时提问。