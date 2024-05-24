![image-20230509152945827](https://gitee.com/aiiw/images/raw/master/img/image-20230509152946601.png)

![image-20230509153036917](https://gitee.com/aiiw/images/raw/master/img/image-20230509153036917.png)



如下应该有问题:第一个客户端口应该为2222,请求也是2222.这样才能保持与服务器是同一个源.

另外一个解释:浏览器应该是访问同源的nginx，然后ngnix去请求真正的后端（这里跨域了，但是不是浏览器在请求，所以没问题），nginx请求成功后把请求的结果返回浏览器

![image-20230509153325365](https://gitee.com/aiiw/images/raw/master/img/image-20230509153325365.png)