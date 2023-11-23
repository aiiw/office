`defineProps({ msg: String })` 和 `defineProps([msg])` 的区别在于定义 props 的方式不同。

1. `defineProps({ msg: String })`：
   - 这是 Vue 3 中定义 props 的标准方式。
   - 使用对象的形式，键为 prop 名称，值为 prop 的配置选项，如类型、默认值等。
   - 通过这种方式定义的 props，可以提供更多的配置选项，并且代码结构更清晰。
2. `defineProps([msg])`：
   - 这种方式并不是 Vue 3 中官方推荐的定义 props 的方式。
   - 通过数组只能传递 props 的名称，无法指定其他配置选项，如类型。
   - 这种方式的代码可读性较差，而且不利于维护和扩展。

因此，推荐使用 `defineProps({ msg: String })` 的方式来定义 props，这样可以充分利用 Vue 3 提供的 props 配置选项，并且使代码更加清晰易懂。