function abc() {
    return new Date("2022-12-12");
}
let vt = abc()
vt.__proto__ = {
    a: "2323"
}
vt.__proto__.b = "sdfdfd"
vt.__proto__.fn = function (a) {
    console.log(a);
}
abc().toString()
console.log(vt.a);
console.log(vt.b);
vt.fn("sss")