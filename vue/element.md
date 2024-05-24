### 常用类

- `el-menu`: `ElMenu` 组件最外层的容器元素。
- `el-menu-item`: `ElMenu` 的子组件之一，代表一个菜单项。
- `el-submenu`: `ElMenu` 的子组件之一，代表一个嵌套的子菜单。
- `el-menu--horizontal`: 水平展示的菜单容器类名，可以将菜单变为水平布局。
- `el-menu--dark`: 暗色主题的菜单容器类名，可以将菜单变为暗色主题。

### 常用属性

- `default-active`: 默认激活的菜单项的 index，即默认选中的菜单项的索引值。
- `unique-opened`: 是否只保持一个子菜单展开。
- `collapse-transition`: 子菜单展开/收缩时是否需要过渡动画。
- `router`: 是否使用 vue-router 进行路由跳转。

### 常用方法

- `toggleCollapse()`: 切换菜单的展开/收缩状态。
- `collapse()`: 收起菜单。
- `expand()`: 展开菜单。
- `handleClick(index, indexPath)`: 菜单项被点击时触发的回调函数，其中 `index` 为当前菜单项的索引值，`indexPath` 为当前菜单项所在的所有菜单项的索引值数组。

以下是Element Plus中常用的Tabs组件的类、属性和方法：

1. 类：

- `el-tabs`：Tabs组件的根元素。
- `el-tab-pane`：每个选项卡的内容容器。
- `is-active`：表示当前选中的选项卡。

1. 属性：

- `v-model`：绑定当前选中的选项卡的索引值。
- `tab-position`：设置选项卡的位置，可选值为 `top`、`bottom`、`left` 和 `right`。
- `type`：设置选项卡的样式类型，可选值为 `card` 和 `border-card`。
- `stretch`：设置选项卡是否自适应宽度，可选值为 `true` 和 `false`。
- `closable`：设置选项卡是否可以关闭，可选值为 `true` 和 `false`。
- `before-leave`：离开某个选项卡之前触发的函数。

1. 方法：

- `prevClick()`：点击向前滚动按钮时触发的事件。
- `nextClick()`：点击向后滚动按钮时触发的事件。
- `tabClick()`：点击某个选项卡时触发的事件。

除此之外，还有一些其他的方法和事件可以用于定制Element Plus Tabs组件的行为，比如`edit`事件、`tab-remove`事件、`tab-add`事件等等