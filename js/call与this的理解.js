const obj = {}
obj.p = 1

function a() {
    console.log(this);
}

obj.f = a
obj.f() //谁调用函数,this就指向谁.

const obj1 = {
    name: "obj1"
}

obj.f.call(obj1)


//模仿一个 call

obj2 = {
    name: "newcall"
}
Function.prototype.newcall = function fn(obj) {
    obj.p = this, obj.p(), delete obj.p
}

obj.f.call(obj2)