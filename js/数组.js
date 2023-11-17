// 1. `push()`: 向数组末尾添加元素


const numbers1 = [1, 2, 3];
numbers1.push(4);
console.log(numbers1); // [1, 2, 3, 4]


//2. `pop()`: 移除并返回数组的最后一个元素


const numbers2 = [1, 2, 3];
const lastElement = numbers2.pop();
console.log(lastElement); // 3
console.log(numbers2); // [1, 2]


//3. `shift()`: 移除并返回数组的第一个元素


const numbers3 = [1, 2, 3];
const firstElement = numbers3.shift();
console.log(firstElement); // 1
console.log(numbers3); // [2, 3]


//4. `unshift()`: 向数组开头添加元素


const numbers4 = [2, 3];
numbers4.unshift(1);
console.log(numbers4); // [1, 2, 3]


//5. `concat()`: 连接两个或多个数组


const array1 = [1, 2];
const array2 = [3, 4];
const combinedArray = array1.concat(array2);
console.log(combinedArray); // [1, 2, 3, 4]


//6. `slice()`: 返回指定范围的新数组
// slice(start, end)  接受两个参数， 表示要提取的起始和结束位置（ 结束位置不包含在提取结果中）。 如果省略第二个参数， 则提取从起始位置到数组末尾的所有元素。

const numbers6 = [1, 2, 3, 4, 5];
const slicedArray = numbers6.slice(2, 4);
console.log(slicedArray); // [3, 4]


//7. `splice()`: 删除、替换或插入元素
// splice(start, deleteCount, item1, item2, ...) 接受三个或更多参数。
// start表示操作开始的索引位置，
// deleteCount表示要删除的元素数量。
// 后面的参数item1, item2, ...指定要插入到数组中的新元素。


const numbers7 = [1, 2, 3, 4];
numbers7.splice(1, 2, 5, 6);
console.log(numbers7); // [1, 5, 6, 4]


//8. `join()`: 将数组元素连接成字符串


const fruits1 = ["apple", "banana", "orange"];
const joinedString = fruits1.join(", ");
console.log(joinedString); // "apple, banana, orange"


//9. `indexOf()`: 返回指定元素的索引


const numbers9 = [1, 2, 3, 4, 5];
const index = numbers9.indexOf(3);
console.log(index); // 2



//10. `lastIndexOf()`: 返回指定元素最后一次出现的索引


const numbers10 = [1, 2, 3, 2, 1];
const lastIndex = numbers10.lastIndexOf(2);
console.log(lastIndex); // 3


//11. `filter()`: 筛选符合条件的元素


const numbers11 = [1, 2, 3, 4, 5];
const evenNumbers = numbers11.filter(number => number % 2 === 0);
console.log(evenNumbers); // [2, 4]


//12. `map()`: 对每个元素执行函数并返回新数组
// forEach() 方法没有返回值， 它只是遍历数组并对每个元素执行指定的回调函数。
// map() 方法返回一个新数组， 该数组由原始数组中的每个元素经过回调函数处理后的结果组成。



const numbers12 = [1, 2, 3];
const squaredNumbers = numbers12.map(number => number ** 2);
console.log(squaredNumbers); // [1, 4, 9]



//13. `reduce()`: 对数组元素执行累计函数


const numbers13 = [1, 2, 3, 4, 5];
const sum = numbers13.reduce((accumulator, currentValue) => accumulator + currentValue);
console.log(sum); // 15


//14. `forEach()`: 对每个元素执行指定函数


const numbers14 = [1, 2, 3];
numbers14.forEach(number => {
    console.log(number); // 依次输出 1, 2, 3
});


//15. `sort()`: 对数组元素进行排序


const fruits = ["banana", "apple", "orange"];
fruits.sort();
console.log(fruits); // ["apple", "banana", "orange"]


//16. `reverse()`: 反转数组元素的顺序


const numbers16 = [1, 2, 3];
numbers16.reverse();
console.log(numbers16); // [3, 2, 1]


//17. `includes()`: 判断数组是否包含指定元素


const numbers17 = [1, 2, 3];
const includesTwo = numbers17.includes(2);
console.log(includesTwo); // true


//18.AT 


// 数组及数组元素 indexOf 这个是根据值查索引  at是根据索引查值
const cart = ['apple', 'banana', 'pear'];

console.log(cart.at(1));


//10 

const num = [1, 8, 3, 4, 5, 6, 7]
console.log(num.findIndex((a) => a > 5));



// // 一个函数，用于返回给定数组的最后一个元素
// function returnLast(arr) {
//     return arr.at(-1);
// }

// // 获取 'cart' 数组的最后一个元素
// const item1 = returnLast(cart);
// console.log(item1); // 输出：'pear'

// // 在 'cart' 数组中添加一个元素
// cart.push('orange');
// const item2 = returnLast(cart);
// console.log(item2); // 输出：'orange'