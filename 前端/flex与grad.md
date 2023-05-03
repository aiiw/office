```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 定义一个总的去掉默认的占位 */
        * {
            padding: 0;
            margin: 0;
            list-style: none;

        }

        /* 1 定义一个总的body */
        body {
            width: 100%;
            overflow: auto;


        }



        /* 2 定义上方的topmain 使用relative 因为
需要占位置.但是这样定义会有一个问题,就是不会冻结.
因此需要改为fixed,但是它没有占位置,会导致下而的元素向上
占位的,因此需要在下面的元素,也就是mybody设置magin-top:50px */
        .topmain {
            height: 50px;
            position: relative;
            top: 0;
            left: 0;
            right: 0;
            margin-bottom: 2px;
            background-color: rgb(96, 96, 240);
            position: fixed;
            z-index: 9999;
        }

        /* 这个地方写.父.子是为了清楚架构吧? */
        .topmain .title {
            line-height: 50px;
            margin-left: 50px;
            font-size: 22px;
            color: aliceblue;
            font-family: 'Courier New',

        }

        /* 这个地方直接使用绝对定位也可以的,针对body? */
        .topmain .title1 {
            position: absolute;
            right: 100px;
            top: 10px
        }


        /* 这个地方使用了span元素,将其转为inline-block,这样有大小,就可以定位了 */
        .topmain .title1 span {
            display: inline-block;
            margin-left: 11px;
            color: chartreuse;
        }

        .topmain .title2 {
            position: absolute;
            right: 50px;
            top: 10px
        }

        /* 3 这里是内容区域,整个页面分上topmain,下为mybody
        mybody 又分为左 mymenu 右 mycontent 
        由于上面的topmain为脱标,所以这里要使用margin-top 50px
        同时这里使用了flex容器,装载了两个子项目,分别为mymenu,mycontent*/
        .mybody {
            margin-top: 50px;
            display: flex;
            /* 使用 flexbox 布局 */
            height: 100vh;
            /* 设置高度为视口高度 */
        }

        /* 4 如下是分了左右两个DIV,分别为mymenu  和 mycontent  
        */

        .mymenu {
            background-color: #ccc;
            /* flex: 0 0 20%; */
            /* 初始宽度为 200px 子项目  余下的给mycontent flex:1
            flex A B C A为占剩余空间的份数 B是缩放 C是初始,预占空间base */
            flex: 0 1 200px;
            transition: all 0.8s ease-out;
            overflow: hidden;
            min-width: 100px;
            /* 设置最小宽度，确保菜单内容不被截断 */
        }

        /* 收缩状态的菜单样式 */
        /* 收缩状态下的菜单样式 
        const menu = document.querySelector('.mymenu');
        const toggleBtn = document.getElementById('toggle-menu');
        toggleBtn.addEventListener('click', () => {
            menu.classList.toggle('collapsed');
        这个使用切换
        */
        .collapsed {
            flex-basis: 20px;
            background-color: blueviolet;

        }




        ul {
            /* 这里注释了,因为加上 *{padding: 0 margin: 0;} */
            /* padding: 0;
            margin: 0; */
            /* list-style: none; */
            background-color: red;
        }

        p {
            /* padding: 0;
            margin: 0; */
            /* list-style: none; */
            text-align: center;
        }

        li {
            border: 1px solid black;
            text-align: center;
            border-radius: 53px;
        }

        /* 相应父元素的第3个子元素,不管什么类型 */
        li:nth-child(3) {
            color: rgb(157, 248, 11);
        }

        /* 当前为li的类型列表中的第3个 */
        li:nth-of-type(3) {
            color: rgb(11, 90, 236);
        }

        /* 可以使用逗号同时声明多个类型 伪元素为:  */
        p:hover,
        li:hover {
            background-color: rgb(102, 8, 252);
            border-radius: 53px;
            color: aliceblue;
            cursor: pointer;
        }


        /* 这个是按钮的样式 */
        #toggle-menu {
            display: block;
            margin: 11px auto;
        }

        .mycontent {
            flex: 1;
            /* 剩余空间全部分配给内容区域 */
            margin-left: 3px;
        }

        /* 5 它是一个grid容器  margin: 0 auto;设置它的这个容器本身要居中.
        grid-template-columns: 100px 100px 100px; 定义三列,第一列100px,第....
        grid-template-rows: 100px 100px 100px;定义三 行,第一行100px,第....*/
        .container {
            display: grid;
            /* 行间距 */
            grid-row-gap: 2px;
            /* 列间距  */
            grid-column-gap: 2px;
            width: 1100px;
            height: 700px;
            grid-template-columns: 1fr 2fr;
            margin: 0 auto;

            /* 第一种居中办法 */
            /* position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%); */
            /* 第二种居中办法 */
            /* position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%); */
        }

        /* 将本身内容居中对齐的办法可以将其设置为 flex模式,并且
 justify-content: center;  align-items: center;*/
        .item1 {
            background-color: brown;
            display: flex;
            /* 添加display属性 */
            justify-content: center;
            /* 将内容水平居中 */
            align-items: center;
            /* 将内容垂直居中 */
        }

        .item2 {
            background-color: chartreuse;
            display: flex;
            /* 添加display属性 */
            justify-content: center;
            /* 将内容水平居中 */
            align-items: center;
            /* 将内容垂直居中 */
        }

        .item3 {
            /* background-color: blue;太强大了grid还可以嵌套flex */
            background-color: blueviolet;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* 在item4中 练习了一个flex的容器 */
        .item4 {
            display: flex;
        }

        .f1 {
            flex: 1;
            background-color: blue;
            font-size: 28px;
        }

        .f2 {
            flex: 1;
            background-color: rgb(247, 113, 3);
        }

        .f3 {
            flex: 1;
            background-color: rgb(4, 229, 245);
        }



        .f1,
        .f2,
        .f3 {

            display: flex;
            /* 添加display属性 */
            justify-content: center;
            /* 将内容水平居中 */
            align-items: center;
            /* 将内容垂直居中 */
        }

        .item5 {
            background-color: cyan;
            grid-column: span 2;
            /* 指定元素占据两列 */
            display: flex;
            /* 添加display属性 */
            justify-content: center;
            /* 将内容水平居中 */
            align-items: center;
            /* 将内容垂直居中 */
        }

        .ct {
            width: 100px;
            height: 100px;
            background-color: blueviolet;
            display: flex;
            /* 使用 flexbox 布局 */
            justify-content: center;
            /* 水平居中 */
            align-items: center;
            /* 垂直居中 */
            transition: all 1s;

        }

        .ct:hover {
            transform: scale(3);
        }

        /* .container>* {
            transition: all 1s;
        }

        .container>*:hover {
            background-color: blanchedalmond;
            transform: scale(0.8);
        } */

        .container>*.scale-down {
            transition: all 1s;
        }

        .container>*.scale-down:hover {
            background-color: blanchedalmond;
            transform: scale(0.8);
        }

        .container2 {
            display: grid;
            /* width: 800px; */
            /* 新增此行 */
            grid-template-columns: repeat(auto-fill, 100px);
            grid-template-rows: repeat(auto-fill, 100px);
            /* 整个容器的居中 */

            width: 100%;
            margin: 0 auto;
            /* 将容器水平居中 */
            /* 项目横向居中 */
            justify-content: space-around;
            /* 项目纵向居中 */
            /* align-items: center; */

            background-color: lightgrey;

            /* 水平居中 */
        }

        .container2 {
            display: grid;
            grid-template-columns: repeat(auto-fill, 100px);
            grid-template-rows: repeat(auto-fill, 100px);
            width: 92%;

            /* 如果希望网格容器铺满整个视口高度 */
            margin: 0 auto;
            justify-content: center;
            align-items: center;
            /* 垂直居中 */
            background-color: lightgrey;

            /* 行间距 */
            grid-row-gap: 2px;
            /* 列间距  */
            grid-column-gap: 2px;
        }



        .cc2 {
            background-color: antiquewhite;
            width: 100%;
            height: 100%;
            grid-row-start: auto;
    </style>

</head>

<body>
    <div class="topmain">
        <div class="title">我的测试管理系统</div>
        <div class="title1">个人信息<span>|</span></div>

        <div class="title2">退出</div>
    </div>
    <div class="mybody">
        <div class="mymenu">
            <!-- 左侧菜单 -->
            <ul>
                <li>第一个列表项</li>
                <p>第N个</p>
                <li>第二个列表项</li>
                <li>第三个列表项</li>
                <li>第四个列表项</li>
                <li>第五个列表项</li>
                <li>第六个列表项</li>
                <li>第七个列表项</li>
            </ul>
            <button id="toggle-menu">收缩</button>
        </div>
        <div class="mycontent">
            <div class="container">
                <div class="item1 scale-down">1</div>
                <div class="item2 scale-down">23</div>
                <div class="item3 scale-down">
                    <p>3</p>
                </div>
                <div class="item4 scale-down">
                    <div class="f1">f1</div>
                    <div class="f2">f3</div>
                    <div class="f3">f3</div>
                </div>
                <div class="item5 scale-down">
                    <div class="ct">居中</div>
                </div>

            </div>
            <div class="container2 ">

                <div class="cc2">123</div>
                <div class="cc2">123</div>
                <div class="cc2">123</div>
                <div class="cc2">123</div>
                <div class="cc2">123</div>
                <div class="cc2">123</div>

            </div>
        </div>
    </div>
    <script>
        const menu = document.querySelector('.mymenu');
        const toggleBtn = document.getElementById('toggle-menu');

        toggleBtn.addEventListener('click', () => {
            menu.classList.toggle('collapsed');
            // menu.classList.toggle('collapsed')
            // classList 是 DOM API 中的一个属性，它提供了一组方法用于操作元素的类名。具体来说，classList 包含 add, remove, toggle, contains 和 replace 等方法，可以方便地添加、删除、切换、查询和替换元素的类名。
            //是 JavaScript 中的 DOM 操作，用于切换指定元素的类名。具体来说，它会在含有指定类名时将该类名从元素的 class 属性中移除，否则就添加该类名到 class 属性中。

            // 在本例中，当点击按钮时，事件监听器会调用 toggleCollapsed() 函数，在函数中通过 classList.toggle() 方法来为菜单元素 .menu 切换一个叫做 "collapsed" 的类名。

            // .collapsed 类名定义了菜单被收缩起来时的样式规则。由于在 CSS 中使用了过渡效果（transition），因此菜单的宽度变化会呈现出平滑的动画效果。

            // 这种方法可以轻松地实现控制菜单的扩展和收缩状态。
        });

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

        addClickHandler();
    </script>
</body>

</html>
```

