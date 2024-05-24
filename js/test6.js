const aiiw1 = Symbol("aiiw");
const aiiw2 = Symbol("aiiw");

const obj = {
    aiiw1: function () {
        console.log("aaaa");
    },
    aiiw2: function () {
        console.log("bbbb");
    }
};

obj[aiiw1](); // 输出 "aaaa"
obj[aiiw2](); // 输出 "bbbb"