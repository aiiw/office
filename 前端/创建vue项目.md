# 创建VUE

1:使用 vue create myel2  这里只选择了vuex和router  如下是router 的 一个注意事项.

```
Vue CLI v5.0.8
? Please pick a preset: Manually select features
? Check the features needed for your project: Router, Vuex
? Choose a version of Vue.js that you want to start the project with 3.x
? Use history mode for router? (Requires proper server setup for index fallback in production) (Y/n)

这是在使用Vue.js框架中创建路由时的一个提示信息，询问是否要使用历史模式。历史模式会将URL改为类似于常规URL的形式，而不是使用哈希值(#)来表示路由。但这种模式需要服务器设置来支持在生产环境中的索引回退。它询问您是否想要使用历史模式，并要求您选择“是”或“否”，如果选择“是”，则需要进行额外的服务器设置。
```

2:完成有提示

```cmd
🎉  Successfully created project myelui2.
👉  Get started with the following commands:

 cd myelui2
 yarn serve
```