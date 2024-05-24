let list = []
for (var i = 0; i < 10; i++) {
    list.push(i) //类似python list.append(i)
}

for (var i = 0; i < list.length; i++) {
    console.log(list[i])
}


var objset = {
    name: "jian"
}


objset.sex = "男"
console.log("==================================");
for (obj in objset) {
    console.log(obj)
}
console.log("==================================");
for (obj of objset) {
    console.log(obj)
}