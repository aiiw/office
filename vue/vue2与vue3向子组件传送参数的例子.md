```vue
<!-- 父组件 -->
<template>
  <div>
    <h1>父组件</h1>
    <p>父组件数据：{{ msg }}</p>
    <button @click="changeMsg">改变数据</button>
    <!-- 通过:msg="msg"绑定数据到子组件 -->
    <child :msg="msg"></child>
  </div>
</template>

<script>
import Child from "./Child.vue";
export default {
  name: "Parent",
  components: {
    Child,
  },
  data() {
    return {
      msg: "Hello",
    };
  },
  methods: {
    changeMsg() {
      this.msg = "World";
    },
  },
};
</script>

<!-- 子组件 -->
<template>
  <div>
    <h2>子组件</h2>
    <p>子组件接收到的数据：{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: "Child",
  // 通过props接收父组件传递过来的数据
  props: ["msg"],
};
</script>
```

```vue
<!-- 父组件 -->
<template>
  <div>
    <h1>{{ title }}</h1>
    <Child :msg="message" />
  </div>
</template>

<script setup>
import Child from "./Child.vue";
const title = "父组件";
const message = "Hello from parent";
</script>
<!-- 子组件 -->
<template>
  <div>
    <h2>{{ title }}</h2>
    <p>{{ props.msg }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  msg: String,
});
const title = "子组件";
</script>
```