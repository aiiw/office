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