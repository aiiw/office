obj1 = {}
obj1.name = "11608"
console.log(obj1);
obj1.sex = "1"
obj1["abc"] = "3232"
for (const key in obj1) { //对象使用 for in 取得key
    if (Object.hasOwnProperty.call(obj1, key)) {
        const element = obj1[key];
        console.log(key, element);

    }
}
// const obj = {
//     id: "1",
//     name: "11608"
// }
// list = []
// for (let i = 0; i < 5; i++) {
//     console.log(i.toString());

//     list.push(obj)

// }

// console.log("======================================================");
// console.log(list)
// console.log("======================================================");
// obj.name = "10776"
// console.log(list)
// console.log("=================如上测试所有的对象都是相同的=====================================");
list = []
for (let i = 0; i < 5; i++) {
    console.log(i.toString());

    list.push({ //python  的 list.append
        id: i,
        name: "11608"
    })
}
console.log("list", list)

const a = {
    "name": "zhangxiao",
    "code": "562323",
    "age": "100"
}
const {
    name,
    code,
    age
} = a

console.log(typeof (code), code, "===============================");




let jsonData = {
    id: 42,
    status: "OK",
    data: [123, 456]
};
let { //这个是解构
    id,

    data: number //这里的:是别名的意思
} = jsonData;


console.log(id, number); //42 "OK" (2) [123, 456]