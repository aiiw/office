![image-20240618161631616](https://gitee.com/aiiw/images/raw/master/img/image-20240618161631616.png)

如上这个是通过元素的事件触发了函数,这个函数是要在事件中运行,所以是函数(),并且这个(参数)是一个实参,对应如上的event,这个是在这个区域的event默认对象

而右边的a是形参.

如下是另一种在在 script中定义元素变量,将函数绑定到事件,函数的默认第一个参数就是event默认对象,即浏览器已经默认运行了函数(event默认对象事件)

```
 function addClickHandler() {
            var lis = document.querySelectorAll('li');
            for (var i = 0; i < lis.length; i++) {
                lis[i].addEventListener('click', function () {
                    if (this.style.backgroundColor === 'blue') {
                        this.style.backgroundColor = '';
                    } else {
                        this.style.backgroundColor = 'blue';
                    }
                });
            }
        }

```

