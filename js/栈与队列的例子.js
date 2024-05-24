// for (var i = 0; i < 5; i++) {
//     setTimeout(() => console.log(i++), 4000)
// }
// console.log(i);


console.log("==========================================")

for (var i = 0; i < 5; i++) {
    console.log(i++)
}
console.log(i, "2323");
//这里输出0246 

console.log("==========================================")

for (var i = 0; i < 5; i++) {
    setTimeout(() => console.log(i++), 4000)
}
console.log(i, "2323"); //这个地方很有意思,输出是56789,而不是0246,为什么呢,因为