在 Vue.js 3.x 中，`app.config` 是一个对象，用于存储 Vue.js 的全局配置。该对象具有以下一些属性：

- `isNativeTag`: 用来检查一个元素是否为原生的 HTML 标签的函数，默认为 `undefined`；
- `isCustomElement`: 用来检查一个元素是否为自定义元素的函数，默认为 `undefined`；
- `performance`: 是否开启性能追踪，默认为 `false`；
- `globalProperties`: 指定在应用程序期间将添加到每个组件实例上的属性和方法；
- `optionMergeStrategies`: 用于自定义选项合并策略的函数；
- `devtools`: 是否允许使用 Vue.js 开发工具，默认为 `true`；
- `warnHandler`: 警告处理程序的函数；
- `errorHandler`: 错误处理程序的函数；
- `compilerOptions`: 自定义编译器选项的对象。

### 这些属性中，`globalProperties` 可以用于将你自己的属性或方法添加到每个组件实例上。例如：

```vue
javascriptCopy Code

const app = createApp(App)

app.config.globalProperties.$myProperty = 'foo'

app.mount('#app')
```

在上面的代码中，我们将 `$myProperty` 添加到了 `globalProperties` 中，并设置其值为 `'foo'`。在任何组件中都可以直接使用 `this.$myProperty` 来访问它。

需要注意的是，在修改 `app.config` 属性时要特别小心，因为它们会影响到整个 Vue.js 应用程序。如果不理解这些属性的作用，请查看 Vue.js 官方文档中对每个属性的详细说明，以便正确地使用它们。



# `globalProperties` 和 `Vue.prototype` 都可以将属性和方法添加到每个 Vue 组件实例上，但它们的应用场景是不同的。

在 Vue.js 3.x 中，推荐使用 `globalProperties` 来添加全局属性和方法。使用 `globalProperties` 可以更加清晰地表明这些属性和方法是全局可用的，并且可以通过 `app.config.globalProperties.xxx` 来进行配置。

例如，在 Vue.js 3.x 中，我们可以使用以下方式将 `axios` 实例注册为全局属性：

```vue
javascriptCopy Code
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

const app = createApp(App)

app.config.globalProperties.$http = axios

app.mount('#app')
```

然后在任何组件中都可以使用 `this.$http` 来访问 `axios` 实例。

相比之下，`Vue.prototype` 更适合在 Vue 组件中添加实例属性和方法。例如：

```vue
javascriptCopy Code

export default {
  data() {
    return {
      message: 'Hello World!' //这个是向组件实例添加响应式属性
    }
  },
  mounted() {
    this.sayHello()
  },
  methods: {
    sayHello() {
      console.log(this.message)
    }
  }
}
```

在上面的代码中，我们在组件的 `methods` 中定义了一个 `sayHello` 方法，并将其添加到了当前组件实例的原型上。这样在模板中就可以直接使用 `this.sayHello()` 来调用它了。

总的来说，`globalProperties` 更适合添加全局属性和方法，而 `Vue.prototype` 更适合添加实例属性和方法。当然，这只是一种推荐的做法，具体应该根据业务需求来选择合适的方式。