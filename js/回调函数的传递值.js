function a(fun) {
    let a = fun(12)
    return a
}

let b = a((item) => item) //这个书写是正确,如果加上{},要写{retrun item}

console.log(b);