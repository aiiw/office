在 Vue 3 中，你可以使用 `ref` 和 `reactive` 创建响应式数据，并通过 `setup()` 函数内部返回的对象中的属性来引用它们。然后，你可以使用 `Vue.createApp()` 方法创建Vue应用程序，并将其挂载到一个 DOM 元素上。

要选择 DOM 元素并操作它们，你可以使用 `ref` 来创建对 DOM 元素的引用。这个引用可以被传递给组件或者其他函数，以便于访问和操作相关的 DOM 元素。例如：

```vue
htmlCopy Code
<template>
  <div>
    <p ref="message" qq="">Hello, World!</p>
    <button @click="changeMessage">Change message</button>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    const message = ref(null)
    const changeMessage = () => {
      message.value.innerHTML = 'New message'
    }
    return { message, changeMessage }
  }
}
</script>
```

在这个例子中，我们使用 `ref` 创建了对 `<p>` 标签的引用，并将其赋值给名为 `message` 的响应式变量。在 `changeMessage` 函数中，我们可以通过 `message.value` 访问该 DOM 元素，并修改其内容。当 `changeMessage` 被触发时，按钮文本将会改变为 "New message"。

需要注意的是，在 Vue 3 中，你不能直接访问 DOM 元素。必须通过 `ref` 或 `reactive` 创建一个响应式变量，然后使用这个变量来操作 DOM 元素。

```vue
<template>
  <el-badge :content="message" class="item" ref="myBadge" abc='1'>
    <el-button @click="handleClick">comments</el-button>
  </el-badge>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const myBadge = ref(null)
const message = ref('a')

function handleClick() {
  const badgeElement = myBadge.value.$el
  if (badgeElement) {
    console.log(badgeElement)
  }
}
</script>
```

