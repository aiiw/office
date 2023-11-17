const timeOut = require('./promise0') //这里使用node.js的导入模块功能

function id2() {
    let p = timeOut(3000) // 一般使用毫秒
    function abc(data) {
        console.log(data)
    }
    p.then(abc)
    p.then(() => {
        console.log("简单来讲，p.then会执行这里定义的函数，这里的函数的参数，来源resolve（这里的数据）");
    })
}
//id2()
// {/* <button onclick="id2()">id2第二个promise例子</button>
// <div>这个地方将p.then(对应resolve函数,可以另外地方写这个函数的定义,注意这里是函数形参,不用执行())</div>
function id3() {
    let p = timeOut(3000) // 一般使用毫秒

    p.then((data) => {
        console.log(data); //这个地方是timeOut  对象 的resolve 
        return new Promise((resolve, reject) => {
            resolve("这个是第一个then 传出去的")
        }).then((data) => {
            console.log(data + "这是第二个对象出去的")
        })
    })
}
id3()
// <button onclick="id3()">id3第三个promise例子</button>
// <div>输出:第一次,以及"这个是第一个then 传出去的",通过then 返回 一个 promise对象</div>
function id4() {
    async function bb() {
        return "1234"
    }
    console.log(bb())
}

id4()
// <button onclick="id4()">id4测试下异步1</button>
// <div>在一个函数的前面加 async 返回一个 promise 对象 其中 return "1234"
//     等同 new promise ((resolve)=>{resolve("1234")})
// </div>
async function bb1(name) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(
                name + ":3秒"
            );
        }, 3000)
    })

}

async function bb2(name) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(
                name + ":3秒"
            );
        }, 3000)
    })

}
async function id5() {

    let p1 = await bb1("bb1")
    let p2 = await bb2("bb2")
    console.log('id5', p1)
    console.log(p2)
}

id5()
// <button onclick="id5()">id5测试下异步2</button>
// <div>
//     <li>强调下await 只能在 async里面</li>
//     <li>await 可以直接取到resolve里的形参==then</li>
//     <li>多个await只会按顺序执行,而不是并行</li>
// </div>


async function doit() {
    var list = [];


    list.push(sayHello('a1'))
    list.push(sayHello('a2'));

    var result = await Promise.all(list);
    console.log(result);
    console.log('over')
}
doit()
// <button onclick="doit()">doit异步并发demo</button>
// <div>这个是网上的例子</div>


async function sayHello(name) {
    await new Promise(function (resolve) {
        setTimeout(function () {
            console.log(name + new Date());
            resolve(name);
        }, 3000)
    })
}



async function id6() {
    var list = [];
    list.push(bb1("id6,bb1"));
    list.push(bb2("id6,bb2"))
    var result = await Promise.all(list);

    // console.log(result);
    // var x;
    // for (x in result) {
    //     console.log(result[x])
    // }
    $.each(result, function (key, val) {
        console.info(key); //将输出one two three
        console.info(val); //将输出1，2，3 这个val等同于obj[key]
    });

}







// <button onclick="id6()">id6异步并发id5()</button>
// <div>参数网上的例子,改进[测试下异步2]</div> */} */}