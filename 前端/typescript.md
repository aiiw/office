### 问题缘由

在typescript项目中我们都需要配置tsconfig.json，在此之前的配置方法都是从网上模仿别人的然后修该或添加自己的配置项。随着项目的增多每次都要去复制感觉很麻烦，就想找一个更好的解决办法快速生成tsconfig.json文件。

### 提出问腿

如何快速生成tsconfig.json文件

### 解决办法

1. 首先全局安装typescript

```
npm install typescript -g
```

1. 在项目目录下执行

```
tsc --init
```