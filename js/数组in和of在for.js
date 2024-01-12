let array = [1, 2, 3, 4, 5, 6]

for (obj in array) {
    console.log(obj); //这个是索引
}


for (obj of array) {
    console.log(obj); //这个是值 
}

var objset = {
    name: "jian"
}


objset.sex = "男"
console.log("==================================");
for (obj in objset) {
    console.log(obj) //这个是索引或者是key
}
console.log("==================================");
for (obj of objset) {
    console.log(obj) //没有这个语法 
}