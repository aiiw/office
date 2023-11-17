 str = '2023-01-01'
 reg = /\d{4}-\d{2}-\d{2}/
 //dotall js 正则表达式中点 (.) 是一个特殊字符，它可以匹配除 换行符（\n）、回车符（\r）、行分隔符、段分隔符
 //反向断言
 //这里的 /\d(?=1)/ 是一个正则表达式，其中 (?=1) 是一个反向断言（lookahead assertion）。

 // 具体来说，正则表达式 / \d(?=1) / 匹配一个数字字符，但仅当该数字后面紧跟着一个字符 "1" 时才匹配成功。这种情况下，正则表达式只会匹配到数字 "1" 前面的一个数字。

 // 例如，对于字符串 "12345678910" 来说，正则表达式 / \d(?=1) / 只会匹配到数字 "9"，因为它后面是字符 "1"。

 // 反向断言是一种零宽度的断言，用于在匹配过程中指定一个条件，该条件必须满足但不会包含在最终的匹配结果中。在上述例子中，反向断言 (?=1) 用于确保数字后面的字符是 "1"，但并不将 "1" 包括在匹配结果中。
 reg = /\d(?=1)/
 obj1 = reg.exec(str) //匹配到的结果

 console.log(obj1)


 var str1 = 'abc3232323dfdfadsf23232323dsfadfdsakldjklfsad3232323' //这里要注意,如果没有这个var 后续引用这个str1 没有智能提示
 reg1 = /[a-zA-Z]+/g //这个g 表示全部匹配
 obj2 = str1.replace(reg1, '*')


 console.log(obj2)

 console.log(reg1.exec(str1));