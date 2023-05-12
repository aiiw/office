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

