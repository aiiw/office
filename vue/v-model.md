```
<script setup>
import { ref } from 'vue'

const text = ref('')
</script>

<template>
  <input type='checkbox' v-model="text" placeholder="Type here">
  <p>{{ text }}</p>
</template>
```

##  我理解的v-model,只是针对表单.而表单的控件是提供给用户输入数据的.

## 例如A控制,输入的数据有一个值表示,value.这个值是与ref('')绑定后,就形式双向.

## 但是Radio|checkbox这样控件的交互是选中.因此它的值 就是true和flase





为了避免潜在的问题，我们应该始终将 `v-model` 绑定到一个响应式变量上。



创建双向数据绑定，将表单输入与 Vue 实例中的数据进行同步。因此，当你使用 `v-model` 指令时，它会自动创建一个绑定到 Vue 实例数据的变量，并且这个变量必须是响应式的才能保证数据更新时视图也能够及时响应

