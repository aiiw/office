<script setup>
import { ref } from 'vue'
import ChildComp from './ChildComp.vue'
const greeting = ref('Hello from parent')
</script>

<template>
  <ChildComp :msg='greeting' />
</template>

如上图的greeting是一个表达式,动态的,如果随便输入则显示:'No props passed yet',只能输入greeting,因为这是一个变量.当这个变量存在,则显示

相应的内容:Hello from parent.并且这个内容是响应式的.

```


<script setup>
const props = defineProps({
  msg: String
})
</script>


<template>
  <h2>{{ msg || 'No props passed yet' }}</h2>
</template>


```

