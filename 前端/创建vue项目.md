# 创建VUE

### 1:使用 vue create myel2  这里只选择了vuex和router  如下是router 的 一个注意事项.

```
Vue CLI v5.0.8
? Please pick a preset: Manually select features
? Check the features needed for your project: Router, Vuex
? Choose a version of Vue.js that you want to start the project with 3.x
? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n)

这是在使用Vue.js框架中创建路由时的一个提示信息，询问是否要使用历史模式。历史模式会将URL改为类似于常规URL的形式，而不是使用哈希值(#)来表示路由。但这种模式需要服务器设置来支持在生产环境中的索引回退。它询问您是否想要使用历史模式，并要求您选择“是”或“否”，如果选择“是”，则需要进行额外的服务器设置。
```

### 2:完成有提示

```cmd
🎉  Successfully created project myelui2.
👉  Get started with the following commands:

 cd myelui2
 yarn serve
```

### 3:默认是没有vue.config.js

```
vue.config.js 是一个可选的配置文件，用于对 Vue CLI 的默认配置进行修改和扩展。使用该文件可以定制应用程序的构建过程、开发服务器配置等，并通过各种选项来控制如何生成和部署项目。

下面是一个示例 vue.config.js 文件的内容：

javascript
module.exports = {
  // 部署应用程序时的基本 URL
  publicPath: process.env.NODE_ENV === 'production' ? '/production-sub-path/' : '/',
  
  // 构建时的输出目录
  outputDir: 'dist',
  
  // 静态资源目录 (js, css, img, fonts)
  assetsDir: 'assets',
  
  // eslint-loader 是否在保存的时候检查
  lintOnSave: true,
  
  // webpack-dev-server 相关配置
  devServer: {
    proxy: {
      '/api': {
        target: '<url>',
        ws: true,
        changeOrigin: true
      },
      '/foo': {
        target: '<other_url>'
      }
    }
  },

  // 是否为生产环境构建生成 source map？
  productionSourceMap: true,

  // 是否启用 CSS source map？
  css: {
    sourceMap: true
  }
}
```

#### 3.1 一个初始化的project

```
import {
    createApp
} from 'vue'
import App from './App.vue'


createApp(App).mount('#app')
```



### 4:安装element

#### 4.1 npm install element-plus --save

#### 4.2在 Vue CLI 项目中，可以在 `vue.config.js` 文件中进行配置。如果你还没有创建这个文件，可以在项目根目录下创建一个。

要使用 Element Plus 的按需加载功能，需要安装以下两个包：

```
npm install -D unplugin-vue-components unplugin-auto-import
```

然后在 `vue.config.js` 中添加以下代码：

```
javascript复制代码const AutoImport = require('unplugin-auto-import/webpack')
const Components = require('unplugin-vue-components/webpack')
const { ElementPlusResolver } = require('unplugin-vue-components/resolvers')

module.exports = {
  // ...其他配置...
  configureWebpack: {
    plugins: [
      AutoImport({
        resolvers: [ElementPlusResolver()],
      }),
      Components({
        resolvers: [ElementPlusResolver()],
      }),
    ],
  },
}
```

然后重启下,不然不生效

