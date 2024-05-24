// 对的， 使用Object.freeze方法可以将一个对象设置为不可变的， 从而防止其属性被修改、 新增或删除。

// 一旦调用了Object.freeze方法， 就不能再修改对象和其属性的值了。 任何尝试修改属性值、 添加新属性或删除现有属性的操作都将被静默地忽略或引发类型错误（ 在严格模式下）。

// 例如， 在以下示例中， 我们创建了一个可变的对象， 并对其应用了Object.freeze方法：

// javascript
// const myObj = {
//     prop1: 'value1',
//     prop2: 'value2'
// };

// Object.freeze(myObj);

// // 修改属性的值，将被忽略
// myObj.prop1 = 'new value';

// // 添加新属性，将被忽略
// myObj.prop3 = 'value3';

// // 删除属性，将被忽略
// delete myObj.prop2;

// console.log(myObj); // 输出: { prop1: "value1", prop2: "value2" }

// 由于myObj被冻结了， 因此所有尝试修改、 添加或删除属性的操作都将被忽略。 输出结果显示， 对象的原始属性值没有发生变化。

// 需要注意的是， Object.freeze只能冻结第一层属性。 如果对象具有嵌套的属性， 则需要递归地对每个子对象调用Object.freeze方法， 以确保整个对象及其子对象都是不可变的。