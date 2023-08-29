在 JavaScript 中，在变量名后面加上问号`?`是可选链操作符（Optional Chaining Operator）的用法。它是在 ES2020 中引入的语法。

可选链操作符主要用于访问对象的属性或调用对象的方法时，可以避免出现错误，特别是在处理可能为 null 或 undefined 的对象时。

当你使用可选链操作符时，如果对象的属性或方法存在，则返回对应的值或执行方法。如果属性或方法不存在，将返回 undefined，而不会产生错误。

以下是使用可选链操作符的示例：

```js
const person = {
  name: 'Alice',
  age: 25,
  address: {
    city: 'Beijing',
    street: '123 Main St'
  },
  hobbies: ['reading', 'painting']
};

// 访问存在的属性
console.log(person.name); // 输出: Alice

// 使用可选链操作符访问不存在的属性
console.log(person.job?.title); // 输出: undefined

// 可以在链式操作中使用多个可选链操作符
console.log(person.address?.city); // 输出: Beijing
console.log(person.address?.zipCode?.toString()); // 输出: undefined

// 可以在数组索引访问中使用可选链操作符
console.log(person.hobbies?.[0]); // 输出: reading
console.log(person.hobbies?.[10]); // 输出: undefined
```

通过使用可选链操作符，我们可以更加安全地访问对象的属性和方法，而不必担心空引用错误（Null Reference Errors）。如果某个属性不存在，代码将不会中断，而是返回 undefined。