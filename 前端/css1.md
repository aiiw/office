![image-20230330162858337](https://gitee.com/aiiw/images/raw/master/img/image-20230330162858337.png)

![](https://gitee.com/aiiw/images/raw/master/img/20230330164308.png)

![image-20230330164807071](https://gitee.com/aiiw/images/raw/master/img/image-20230330164807071.png)

![image-20230331091336550](https://gitee.com/aiiw/images/raw/master/img/image-20230331091336550.png)



![image-20230331110107876](https://gitee.com/aiiw/images/raw/master/img/image-20230331110107876.png)

![image-20230403094233795](https://gitee.com/aiiw/images/raw/master/img/image-20230403094233795.png)

![image-20230403094409609](https://gitee.com/aiiw/images/raw/master/img/image-20230403094409609.png)

![image-20230403095121387](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230403095121387.png)

![image-20230403095143582](https://gitee.com/aiiw/images/raw/master/img/image-20230403095143582.png)

![image-20230403095350224](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230403095350224.png)



![image-20230403100141541](https://gitee.com/aiiw/images/raw/master/img/image-20230403100141541.png)

可以使用CSS的`line-height`属性来实现文字的上下居中，将它的值设置为容器高度的值即可。例如：

```css
这个是行内元素的居中方式:
.container {
  height: 200px;
  line-height: 200px;
  text-align: center;
}
```

这样，容器中的文字就会在垂直方向上居中对齐。需要注意的是，如果文字的高度超过了容器的高度，那么这种居中方式可能会导致文字被截断。





如果要让一个absolute容器在其父容器中上下居中，可以使用CSS的`position`和`transform`属性来实现。

首先，将该容器的`position`属性设置为`absolute`，并将其`top`和`bottom`属性都设置为0，这样容器会占据父容器的整个高度。然后，可以使用`transform`属性将容器向上移动一半的高度，使其垂直居中对齐。例如：

```css
这个是块,经典的居中
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
  transform: translateY(-50%);
}
```

这样，`.child`元素就会在`.parent`容器中垂直居中对齐，无论它们的高度如何。需要注意的是，`.parent`容器必须拥有一个非静态定位（例如`relative`、`absolute`或`fixed`），否则`.child`元素的定位将无法相对于`.parent`容器进行计算。





transform属性在这里的作用

##### `transform`属性可以用来对元素进行变形操作，包括平移、旋转、缩放和倾斜等。在这个例子中，我们使用`transform: translateY(-50%)`将子元素 `.child` 向上平移了半个自身高度的距离，使其垂直居中对齐。

具体来说，`translateY(-50%)` 表示将元素在垂直方向上向上平移 50% 的自身高度，由于该元素的高度是已知的，因此这种方式可以使其垂直居中对齐。

另外，我们还可以使用`translateX(-50%)` 来实现水平居中对齐，该方式会将元素在水平方向上向左平移 50% 的自身宽度。需要注意的是，使用`translate`属性时，需要将元素的 `position` 属性设置为 `absolute` 或 `fixed`，以便相对于其父元素进行定位和计算平移距离。





既然有这个作用，为什么 还需要margin: auto;

`margin: auto` 的作用是将元素在水平方向上居中对齐。在这个例子中，我们将 `.child` 元素的 `top` 和 `bottom` 属性都设置为 0，这样它就会占据父容器的整个高度。接下来，使用 `margin: auto` 来将其在水平方向上居中对齐。

需要注意的是，当我们将一个块级元素的宽度设置为固定的值时，才可以使用 `margin: 0 auto` 来实现水平居中对齐。但是，如果元素的宽度是自适应的，那么 `margin: auto` 将无法使其水平居中对齐，此时需要使用其他的技巧来实现水平居中对齐，例如使用 Flexbox 或 Grid 等布局方式。





# 选择器

a,b,c这个是并

a b  这个是后代

a>b这个是亲



# 定位：

### 为什么要定位，就是浮动和标准流不能任意摆放盒子，浮动只在左右，标准流按顺序。

 定位：定位类型+ top,left,right,bottom

fix:粘在浏览器

父相子绝对：

如果一个容器没有父亲，浏览器是他的父亲。（绝对）

父容器如果有一个定位后，子容器就跑不出它的容器了。（并且如果父容器没有定位，会向上找，找到以它为基准，就近原则）

绝对定位是不占用位置的，只有相对定位是占用位置的，浮动也是不占用位置的。

![image-20230404094346562](https://gitee.com/aiiw/images/raw/master/img/image-20230404094346562.png)

![](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230404095021733.png)

![image-20230404095329952](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230404095329952.png)

![image-20230404095637741](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230404095637741.png)



```
对于绝对定位的元素，使用 margin: 0 auto; 是无法实现水平居中的。因为绝对定位会使元素脱离文档流，所以宽度不再由父级元素决定。如果要让绝对定位的元素水平居中，可以通过设置 left 和 right 属性来实现，例如：

position: absolute;
left: 50%;
transform: translateX(-50%);
这样就能够将元素水平居中了。其中，left: 50%; 将元素的左边缘距离视口左侧的距离设置为页面宽度的一半，而 transform: translateX(-50%); 将元素向左移动自身宽度的一半，从而实现水平居中的效果。
```



## 1:反向:行内元素是不能直接设置高度与宽度的，但是加了定位，就可以了

```
行内元素是不能直接设置高度与宽度的。因为行内元素的宽度和高度是由元素内容决定的。但是你可以使用CSS中的定位属性，如position: relative/absolute/fixed来改变元素在页面中的位置。然后再使用top、bottom、left、right等属性来控制元素的偏移量从而实现对元素大小的控制。需要注意的是，通过定位方式设置元素大小会影响到页面布局，所以一定要慎重使用。
```



## 2:反向:块元素默认宽度是100%，如果加了定位，默认大小是内容的大小。

```
如果一个块级元素没有设置定位属性（position: static），那么它的默认宽度是100%，高度则由其内容和内边距决定。也就是说，如果你不对块级元素设置宽度，那么它将占据父元素的所有可用空间。

如果一个块级元素设置了相对定位（position: relative），那么它的大小和位置与未设置定位属性时基本类似，但是它会相对于自身在正常文档流中的位置进行偏移。

如果一个块级元素设置了绝对定位（position: absolute），那么它的大小和位置就不再受到文档流的影响，而是相对于最近的已定位祖先元素（即其父元素中第一个设置了 position 属性并且值不是 static 的元素）进行定位。
```



### ![image-20230404095943959](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230404095943959.png) 

### 3：浮动是不会压住文字的，这个是它原来设计的初衷，做文字围绕效果

### 4：绝对定位，类似浮动，也是脱标，但是它是可以压住文字的。

## 5：只有相对定位是不脱标的。就是说移动后，位置仍保留。



![image-20230404143913625](C:/Users/11608/AppData/Roaming/Typora/typora-user-images/image-20230404143913625.png)



好的，以下是以列表形式提供CSS居中实现的方式：

1. 标准流

```css
Copy Code
.container {
  text-align: center;
}
```

1. 浮动

```css
Copy Code
.container {
  height: 300px;
  text-align: center;
}

.centered {
  display: inline-block;
  vertical-align: middle;
}

.centered img {
  max-height: 100%;
  max-width: 100%;
}
```

1. 定位

```css
Copy Code
.container {
  position: relative;
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

1. 弹性布局

```css
Copy Code.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

1. 渐变

```css
Copy Code
.container {
  background-image: linear-gradient(to bottom right, #FF0080, #FF8C00);
}
```

希望这些代码能够对您有所帮助！

```css
"transform" 和 "left" 都是 CSS 中用于控制元素位置的属性，但它们之间有一些根本性的区别。

首先，"left" 是相对定位（position: relative）下的属性。它指定元素左边缘与其包含块的左边缘之间的距离。因此，当元素的位置发生改变时，它所占据的空间不会受到影响，而且周围的元素也不会受到影响。

相比之下，"transform" 是一种变换操作，用于对元素进行平移、旋转、缩放等操作。它不会影响元素的位置，而只会影响元素的呈现方式。具体来说，当我们应用 "transform" 变换时，元素的位置仍然保持不变，但元素所占据的空间可能会发生变化，从而影响周围元素的布局。

另外，"left" 可以接受负值和百分比作为参数，而 "transform" 只能接受长度单位或角度单位作为参数。这意味着 "left" 可以将元素移动到包含块之外，而 "transform" 则无法实现这样的效果。

总之，"left" 和 "transform" 虽然都可以用于控制元素位置，但它们基于的机制和使用方式有很大的不同。开发者需要根据具体需求选择合适的属性，以实现自己想要的布局效果。
```

```css
transform: translate() 是 CSS3 中的一个变换属性，它用来移动元素。与 translate 搭配使用的是 transform 属性。

当我们需要对一个元素进行平移操作时，必须将 translate 函数作为 transform 属性值来进行设置。比如：

css
.box {
  transform: translate(50px, 100px);
}
这段代码会将 .box 元素向右移动 50 个像素，向下移动 100 个像素。

因此，transform: translate() 必须与 transform 属性一起使用，否则 translate 函数无法起效果。同时，transform 属性还可以实现其他的变换效果，包括旋转、缩放和扭曲等等。
```

| 定位方式   | 是否脱离文档流 | 定位基准点                 | 可设置的位置属性                 | 居中的例子                                                   |
| ---------- | -------------- | -------------------------- | -------------------------------- | ------------------------------------------------------------ |
| `static`   | 否             | 元素在标准流中的位置       | 无                               | 无                                                           |
| `relative` | 否             | 元素在标准流中的位置       | `top`、`bottom`、`left`、`right` | 通过设置 `margin: auto;` 来实现水平居中或者垂直居中。        |
| `absolute` | 是             | 最近的非 static 祖先元素   | `top`、`bottom`、`left`、`right` | 通过设置 `top: 50%; left: 50%; transform: translate(-50%,-50%);` 来实现水平居中和垂直居中。 |
| `fixed`    | 是             | 视口（浏览器窗口）         | `top`、`bottom`、`left`、`right` | 通过设置 `top: 50%; left: 50%; transform: translate(-50%,-50%);` 来实现水平居中和垂直居中。 |
| `sticky`   | 是             | 父容器和视口（浏览器窗口） | `top`、`bottom`、`left`、`right` | 无                                                           |
| `float`    | 是             | 元素在标准流中的位置       | `left`、`right`                  | 通过将元素包裹在一个容器中，设置容器 `text-align: center;` 和元素 `display: inline-block;` |

![image-20230404161630955](https://gitee.com/aiiw/images/raw/master/img/image-20230404161630955.png)

| 对齐方式                          | 描述                           | 使用条件                                                     |
| --------------------------------- | ------------------------------ | ------------------------------------------------------------ |
| `text-align: left;`               | 左对齐文本                     | 适用于行内块元素和文本级元素。                               |
| `text-align: center;`             | 居中文本                       | 适用于行内块元素和文本级元素。                               |
| `text-align: right;`              | 右对齐文本                     | 适用于行内块元素和文本级元素。                               |
| `text-align: justify;`            | 文本两端对齐                   | 适用于行内块元素和文本级元素。要求文本必须为多行文本，并且每一行的长度不相同时才能生效。 |
| `vertical-align: baseline;`       | 垂直方向以基线对齐             | 适用于行内块元素和表格单元格等内联元素。                     |
| `vertical-align: top;`            | 垂直方向以顶部对齐             | 适用于行内块元素和表格单元格等内联元素。                     |
| `vertical-align: middle;`         | 垂直方向居中对齐               | 适用于行内块元素和表格单元格等内联元素。                     |
| `vertical-align: bottom;`         | 垂直方向以底部对齐             | 适用于行内块元素和表格单元格等内联元素。                     |
| `vertical-align: text-top;`       | 垂直方向以文本顶部对齐         | 适用于图片、表格单元格等内联元素，但不适用于文本级元素。     |
| `vertical-align: text-bottom;`    | 垂直方向以文本底部对齐         | 适用于图片、表格单元格等内联元素，但不适用于文本级元素。     |
| `align-items: flex-start;`        | 元素在交叉轴开始位置对齐       | 适用于Flex容器内的所有项目。                                 |
| `align-items: flex-end;`          | 元素在交叉轴结束位置对齐       | 适用于Flex容器内的所有项目。                                 |
| `align-items: center;`            | 元素在交叉轴中间位置对齐       | 适用于Flex容器内的所有项目。                                 |
| `align-items: stretch;`           | 默认值。元素被拉伸以适应容器   | 适用于Flex容器内的所有项目。                                 |
| `align-items: baseline;`          | 元素在交叉轴基线位置对齐       | 适用于Flex容器内的所有项目，但只有当所有项目都有基线时才会生效。 |
| `justify-content: flex-start;`    | 元素在主轴开始位置对齐         | 适用于Flex容器内的所有项目。                                 |
| `justify-content: flex-end;`      | 元素在主轴结束位置对齐         | 适用于Flex容器内的所有项目。                                 |
| `justify-content: center;`        | 元素在主轴中间位置对齐         | 适用于Flex容器内的所有项目。                                 |
| `justify-content: space-between;` | 元素之间平均分布，首尾不留空白 | 适用于Flex容器内的所有项目。要求Flex容器的长度必须大于或等于所有项目的总长度。 |
| `justify-content: space-around;`  | 元素之间平均分布，首尾留有空白 | 适用于Flex容器内的所有项目。要求Flex容器的长度必须大于或等于所有项目的总长度。 |



![image-20230410111854319](https://gitee.com/aiiw/images/raw/master/img/image-20230410111854319.png)

```
Flexbox（弹性布局）是CSS3中的一种新的布局方式，它可以使元素的排列更加灵活和高效。以下是Flexbox常用的一些属性：

display: 定义元素的布局类型为flex。

flex-direction：定义主轴方向，有row、row-reverse、column、column-reverse四个值可选，分别表示水平从左到右、水平从右到左、垂直从上到下、垂直从下到上。

justify-content：定义主轴对齐方式，有flex-start、flex-end、center、space-between、space-around、space-evenly六个值可选。

align-items：定义交叉轴对齐方式，有flex-start、flex-end、center、baseline、stretch五个值可选。

flex-wrap：定义是否换行，有nowrap、wrap、wrap-reverse三个值可选。

align-content：定义多根轴线之间的对齐方式，有flex-start、flex-end、center、space-between、space-around、stretch六个值可选。

flex-grow：定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。

flex-shrink：定义项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。

flex-basis：定义项目在分配多余空间之前的初始大小，默认为auto。

flex：是flex-grow、flex-shrink和flex-basis的缩写，第二个和第三个参数可选。

order：定义项目的排列顺序，数值越小，排列越靠前，默认为0。
```

```
在 Flexbox 布局中，我们把容器称为“父元素”，把容器内的子元素称为“子元素”或“子项目”。以下是子项目常用的一些属性：

flex-grow: 定义子元素的放大比例，默认值为0，即如果存在剩余空间也不放大。

flex-shrink: 定义子元素的缩小比例，默认值为1，即如果空间不足，该子元素将缩小。

flex-basis: 定义子元素在分配多余空间之前的初始大小，默认值为auto。

flex: 是flex-grow、flex-shrink 和flex-basis的简写形式，可以同时设置这三个属性。

order: 定义子元素的排列顺序，数值越小，排列越靠前，默认为0。

align-self: 定义单个子元素在交叉轴上的对齐方式，覆盖父元素的align-items属性。它可以取flex-start、flex-end、center、baseline 或 stretch五个值。

使用这些属性可以更加灵活地控制子元素的布局和排列。
```

REM

```
是的，`rem`相对于根元素（即HTML标签）的字体大小来计算。因此，在CSS中设置了根元素的字体大小后，所有使用`rem`作为单位的尺寸都会基于该字体大小计算。例如，如果根元素的字体大小为16像素，那么1rem等于16像素。

值得注意的是，只有在CSS中设置了根元素的字体大小之后，`rem`才会按照该字体大小进行计算。如果没有设置，浏览器将使用默认的字体大小，通常为16像素，作为计算基准。

另外，应当区分`rem`与`em`的不同。`em`相对于当前元素的字体大小计算，而不是相对于根元素的字体大小。因此，`em`的大小随着父元素的字体大小而变化。


```

flex-wrap

```
flex-wrap是CSS中用于控制flex容器内的元素是否换行的属性。当flex-wrap的值为nowrap时，该容器内的元素不会换行，而会尽可能地占据一行；当值为wrap时，如果容器内的元素排列完一行之后还有剩余空间，那么剩余的元素将换到下一行；而当值为wrap-reverse时，则是从右向左进行排列，即在下一行首先排列靠右的元素。

例如，以下代码将创建一个flex容器，其内部元素默认不换行：

css
.flex-container {
  display: flex;
  flex-wrap: nowrap;
}
这里的.flex-container是自定义的CSS类名，表示一个flex容器，使用了display: flex来将其设置为flex布局，并使用flex-wrap: nowrap来设置其内部元素不换行。如果容器内的元素超出了一行的宽度，它们将被挤压在同一行内，而不是自动换行。
```

