//Promise { 'aaaa' } 相当于 retrun new promist 中的resolve("aaaa"),要使用then才能调用这个"aaaa",如果想简单点调用,可以使用await

async function a() {
    return "aaaa"
}


let b = a()

console.log(b);

a().then((val) => console.log(val))

async function c() {
    let d = await a()
    console.log(d);
}

c()