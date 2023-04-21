 str = '2023-01-01'
 reg = /\d{4}-\d{2}-\d{2}/
 //dotall js 正则表达式中点 (.) 是一个特殊字符，它可以匹配除 换行符（\n）、回车符（\r）、行分隔符、段分隔符
 //反向断言
 reg = /\d(?=3)/
 obj1 = reg.exec(str) //匹配到的结果

 console.log(obj1)


 var str1 = 'abc3232323dfdfadsf23232323dsfadfdsakldjklfsad3232323' //这里要注意,如果没有这个var 后续引用这个str1 没有智能提示
 reg1 = /[a-zA-Z]+/g //这个g 表示全部匹配
 obj2 = str1.replace(reg1, '*')


 console.log(obj2)

 console.log(reg1.exec(str1));