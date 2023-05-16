<script setup>
import { ref,onMounted } from 'vue'

const p = ref(null)
</script>



<template>
  <p ref="p" @click="p.style.color='red'">hello1</p>
</template>





<script setup>
import { ref, onMounted } from 'vue'

const p = ref(null)

onMounted(() => {
  p.value.textContent = 'mounted2322!'
})
</script>

<template>
  <p ref="p">hello</p>
</template>