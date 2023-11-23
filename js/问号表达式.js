//在 JavaScript 中，问号表达式通常指的是条件（三元）运算符 ? :。它是一种简洁的条件表达式，用于根据条件的真假来返回不同的值。

//其基本语法如下：


//condition ? expr1 : expr2
// 其中，condition 是一个用于计算为布尔值的表达式。如果 condition 为真，则整个表达式的值为 expr1；如果 condition 为假，则整个表达式的值为 expr
// 示例：

// javascript
var age = 20;
var canDrink = (age >= 21) ? "Yes" : "No";
console.log(canDrink); // 输出 "No"
// 在上面的例子中，如果年龄大于等于 21，则 canDrink 的值为 "Yes"；否则为 "No"。

// 条件运算符经常用于简单的条件赋值，或者在输出中根据条件选择不同的内容。它提供了一种在一行代码中表示条件逻辑的简洁方式。