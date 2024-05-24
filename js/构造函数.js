// 对于JS中的任何一个普通函数，当用new关键字来调用时，它就是构造函数。可见与函数定义无关，与调用方法有关。
//在社区中，通常默契地将函数名首字母大写来表示该函数以后希望被作为构造函数来使用
//但是，在JavaScript语言的对象体系，不是基于“类”的，而是基于构造函数（constructor）和原型链（prototype）
function Person(name, height) {
    this.name = name;
    this.height = height;
    this.bark = function (fs) {
        console.log("hello");

    }
}


var boy = new Person('Keith', '1800');

boy.__proto__
console.log(boy); //Person {name: 'Keith', height: 180, bark: ƒ}
console.log(boy.constructor); //f Person(){}  //整个构造函数原型
console.log(boy.bark('1')); //8
console.log(boy.name); //'Keith'
console.log(boy.height); //180
console.log("=========================================");

function Cat1(name) {
    this.name = name;
    console.log(this) //先打印 new的时候打印  Cat1 {name: 'kk'}  
}
var cat3 = new Cat1("kk");
console.log(cat3); //后打印  Cat1 {name: 'kk'} 指向原型链，再赋值

//如下是实例化一个构造函数的过程
function Person1(name, age) {
    this.name = name;
    this.age = age;
    this.eating = function () {
        console.log(this.name + ' is eating');
    }
}

const p1 = new Person1('zs', 12);

//----------------------------------------------------------------------------
/*实际JS引擎帮助我们实现的操作*/
// const newObj = {};
// newObj.__proto__ = Person.prototype;
// this = newObj;

// this.name = name;
// this.age = age;
// this.eating = function () {
//     console.log(this.name + ' is eating');
// }

// return newObj;