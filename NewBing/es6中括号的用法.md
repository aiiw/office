在ES6中，对象里面的中括号有以下用法：

1. 访问属性：可以使用中括号语法来访问对象的属性，例如：`obj['prop']`。这种方式同样可以用于访问动态变量名对应的属性，例如：

```
Copy Code
let propName = 'name';
let obj = { [propName]: 'John' };
console.log(obj.name); // 输出: John
```

1. 定义计算属性名：在定义对象字面量时，可以使用中括号语法来定义计算属性名，例如：

```
Copy Code
let prop = 'age';
let obj = {
  name: 'John',
  [prop]: 25
};
console.log(obj.age); // 输出: 25
```

1. 解构赋值：解构赋值时，也可以使用中括号语法来获取对象的属性值，例如：

```
Copy Code
let obj = { name: 'John', age: 25 };
let {['name']: personName, age} = obj;
console.log(personName); // 输出: John
```

1. Symbols属性：当使用Symbol作为对象属性时，只能使用中括号语法来访问该属性，例如：

```
Copy Code

let mySymbol = Symbol('mySymbol');
let obj = {
  [mySymbol]: 'hello world'
};
console.log(obj[mySymbol]); // 输出: hello world
```

总之，在ES6中，对象里面的中括号语法给了我们更多的灵活性和可读性，同时也支持动态变量名和Symbol属性的访问。