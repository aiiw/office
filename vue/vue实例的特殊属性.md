在Vue中，以 `$` 开头的属性和方法通常是框架内部定义的一些特殊属性和方法，用于实现某些功能或提供一些便利。这些属性和方法都被添加到组件实例上，并可以在组件内部通过 `this` 访问。

以下是一些常见的以 `$` 开头的属性和方法：

- `$el`：组件对应的 DOM 元素。
- `$data`：组件数据对象。
- `$props`：组件属性对象。
- `$emit()`：用于触发自定义事件。
- `$on()`：用于监听自定义事件。
- `$watch()`：用于监听数据变化。
- `$set()`：用于给嵌套数据对象添加响应式属性。
- `$nextTick()`：用于在 DOM 更新后执行回调函数。
- `$refs`：组件内所有拥有 ref 属性的子组件或 DOM 元素的引用。
- `$router`：Vue 路由实例。
- `$store`：Vuex 的 store 实例。

需要注意的是，由于这些属性和方法是框架内部定义的，它们可能会在未来的版本中被修改或删除，因此在使用时需要查看文档并注意版本兼容性。



```vue
<template>
  <div>
    <p>Hello world!</p>
  </div>
</template>

<script>
export default {
  name: 'my-component',
  mounted() {
    console.log(this.$el) // 输出 <div><p>Hello world!</p></div>（组件对应的 DOM 元素）
  }
}
</script>
```



以props为例子说明下原理：

`props` 函数的原理是在组件定义时将属性的配置项保存到组件实例中，当组件被渲染时，Vue 会对这些属性进行检查和校验，并将它们挂载到组件实例的 `$props` 属性上，以便在组件内部使用。

### 具体来说，在组件实例化时，Vue 会遍历 `props` 对象的每个属性，并为每个属性设置一个响应式的数据对象。这个数据对象包含了以下属性：

- `value`：当前属性的值
- `sync`：是否支持双向绑定
- `isRequired`：是否必填
- `validator`：自定义校验函数
- `type`：属性类型

然后，当组件被渲染时，Vue 会对传递给组件的属性进行类型校验和格式化，并将它们赋值给相应的数据对象的 `value` 属性。如果有自定义校验函数，则会执行该函数来验证属性值是否符合要求。如果存在错误，则会发出警告或抛出异常。

最后，`$props` 属性会被注入到组件的上下文中，以便在模板中使用。你可以通过 `$props` 来访问组件的所有属性，如下所示：

```vue
<template>
  <div>
    <p>{{ $props.message }}</p>
    <p>{{ $props.count }}</p>
  </div>
</template>

<script>
export default {
  name: 'my-component',
  props: {
    message: {
      type: String,
      required: true
    },
    count: {
      type: Number,
      default: 0
    }
  }
}
</script>
```

