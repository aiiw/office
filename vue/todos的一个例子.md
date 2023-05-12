```vue
<script setup>
import { ref } from 'vue'

// 给每个 todo 对象一个唯一的 id
let id = 0

const newTodo = ref('')
const todos = ref([
  { id: id++, text: 'Learn HTML' },
  { id: id++, text: 'Learn JavaScript' },
  { id: id++, text: 'Learn Vue' }
])

function addTodo() {
  const a=newTodo.value
todos.value.push({id:id++,text:a})
}

function removeTodo(todo) {
  // ...这个更加简洁  todos.value = todos.value.filter((t) => t !== todo)
  let index = todos.value.findIndex(item => item.id === todo.id);
  todos.value.splice(index, 1);
  console.log(todo.id)

}
</script>

<template>
  <form @submit.prevent="addTodo">
    <input v-model="newTodo">
    <button>Add Todo</button>    
  </form>
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      {{ todo.text }}
      <button @click="removeTodo(todo)">X</button>
    </li>
  </ul>
</template>
```

