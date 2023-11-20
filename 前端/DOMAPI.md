当然可以，以下是一些常用的 DOM API 属性和方法：

### 属性

- `textContent`：获取或设置元素中所有子节点的文本内容
- `innerHTML`：获取或设置元素内包含的 HTML 代码
- `value`：获取或设置表单元素的值（如 `<input>` 或 `<textarea>`）
- `checked`：获取或设置复选框或单选框的选中状态
- `disabled`：获取或设置禁用状态
- `selected`：获取或设置下拉列表中选项的选中状态
- `src`：获取或设置图像、音频或视频等媒体资源的 URL
- `href`：获取或设置链接的地址
- `classList`：获取或设置元素类名的列表

### 方法

- `querySelector(selector)`：选择符合指定 CSS 选择器的第一个元素
- `querySelectorAll(selector)`：选择符合指定 CSS 选择器的所有元素，并返回一个 NodeList 对象
- `addEventListener(type, listener)`：为指定元素添加事件监听器
- `removeEventListener(type, listener)`：从指定元素移除事件监听器
- `createElement(tagName)`：创建指定名称的 HTML 元素
- `appendChild(childElement)`：将指定元素添加为当前元素的子元素
- `insertBefore(newElement, referenceElement)`：在参考元素之前插入新元素
- `removeChild(childElement)`：从当前元素中删除指定子元素
- `setAttribute(name, value)`：为指定元素设置属性值
- `getAttribute(name)`：获取指定元素的属性值
- `hasAttribute(name)`：判断指定元素是否存在指定属性
- `removeAttribute(name)`：从指定元素中删除指定属性

这些属性和方法可以在操作 DOM 元素时非常有用，包括选择元素、添加/删除元素、修改元素的内容或属性等。同时，这仅仅是 DOM API 中一小部分常用功能的示例，开发者实际应用过程中可能会使用到更多的 API 属性和方法。



事件:

1. `click`：鼠标点击时触发。
2. `dblclick`：鼠标双击时触发。
3. `mouseover`：鼠标移入元素时触发。
4. `mouseout`：鼠标移出元素时触发。
5. `mousedown`：鼠标按下时触发。
6. `mouseup`：鼠标松开时触发。
7. `mousemove`：鼠标在元素上移动时触发。
8. `keydown`：按下键盘按键时触发。
9. `keyup`：松开键盘按键时触发。
10. `keypress`：按下键盘按键并释放时触发。
11. `focus`：元素获得焦点时触发。
12. `blur`：元素失去焦点时触发。
13. `change`：元素的值发生改变时触发（通常用于表单元素）。
14. `input`：元素的值发生改变时触发（通常用于输入框等）。
15. `submit`：表单提交时触发。
16. `load`：页面或图像加载完成时触发。
17. `unload`：页面即将被卸载时触发。
18. `resize`：窗口或框架大小改变时触发。
19. `scroll`：元素滚动时触发。
20. `contextmenu`：用户右击元素时触发上下文菜单事件。