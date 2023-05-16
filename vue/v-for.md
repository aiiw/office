<script setup>
import { ref,watch  } from 'vue'

const todoId = ref(1)
const todoData = ref(null)

async function fetchData() {
  todoData.value = null
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/todos/${todoId.value}`
  )
  todoData.value = await res.json()
}



  watch(todoId, (newCount,old) => {
  // 没错，console.log() 是一个副作用
    fetchData(newCount)
    console.log(`old |current:${old}`)
  console.log(`new count is: ${newCount}`)
})

</script>

<template>
  <p>Todo id: {{ todoId }}</p>
  <button @click="todoId++">Fetch next todo</button>
  <p v-if="!todoData">Loading...</p>
  <div v-else>
  <li v-for="(key,value) in todoData">  //第一个是值,第二个是key,如果是数组则为index
  {{ value }}
</li>
  </div>
</template>