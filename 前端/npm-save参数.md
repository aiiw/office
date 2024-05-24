# npm --save参数说明

![img](https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png)

[步步静心](https://blog.csdn.net/weixin_43862596)![img](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)于 2021-11-10 14:20:43 发布![img](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)10331![img](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png) 收藏 14



当你为你的模块安装一个依赖模块时，正常情况下你得先安装他们（在模块根目录下npm install [module](https://so.csdn.net/so/search?q=module&spm=1001.2101.3001.7020)-name），然后连同版本号手动将他们添加到模块配置文件package.json中的依赖里（dependencies）。

–save和–save-dev可以省掉你手动修改[package](https://so.csdn.net/so/search?q=package&spm=1001.2101.3001.7020).json文件的步骤。 npm install module-name --save自动把模块和版本号添加到dependencies部分 npm install module-name --save-dev自动把模块和版本号添加到devDependencies部分

```js
npm install axios
//执行完以上命令后，会在package.json文件中的dependencies节点下，看到axios以及其版本号
12
```

1. npm install moduleName --save
   简写 -s，将模块安装到项目 node_modules 目录下，也会将模块依赖写入 dependencies 节点，同时运行 npm install 初始化项目时会将模块下载到项目目录下。
2. npm install moduleName --save-dev
   简写 -d，将模块安装到项目 node_modules 目录下，也会将模块依赖写入 devDependencies 节点，同时运行 npm install 初始化项目时，会将模块下载到项目目录下。