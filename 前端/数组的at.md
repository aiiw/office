## 定义和用法

at() 方法用于接收一个整数值并返回该索引对应的元素，允许正数和负数。负整数从数组中的最后一个元素开始倒数。

匹配给定索引的数组中的元素。如果找不到指定的索引，则返回 undefined。

在传递非负数时，at() 方法等价于括号表示法。例如，array[0] 和 array.at(0) 均返回第一个元素。但是，当你需要从数组的末端开始倒数时，则不能使用 Python 和 R 语言中支持的 array[-1]，因为方括号内的所有值都会被视为字符串属性，因此你最终读取的是 array["-1"]，这只是一个普通的字符串属性而不是数组索引。

通常的做法是访问 length 并将其减去从末端开始的相对索引。例如，array[array.length - 1]。at() 方法允许使用相对索引，因此上面的示例可以简化为 array.at(-1)。更正式地，当 index < 0 时，该方法将访问索引 index + array.length。

at() 方法是通用的。其仅期望 this 具有 length 属性和以整数为键的属性。

```js
// 数组及数组元素
const cart = ['apple', 'banana', 'pear'];

// 一个函数，用于返回给定数组的最后一个元素
function returnLast(arr) {
  return arr.at(-1);
}

// 获取 'cart' 数组的最后一个元素
const item1 = returnLast(cart);
console.log(item1); // 输出：'pear'

// 在 'cart' 数组中添加一个元素
cart.push('orange');
const item2 = returnLast(cart);
console.log(item2); // 输出：'orange'
```

