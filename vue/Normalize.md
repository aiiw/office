NormalizeNormalize要在Vue 3中使用Normalize.css，可以按照以下步骤进行操作：

1. 首先，安装Normalize.css并将其添加为依赖项：

```
bashCopy Code
npm install normalize.css --save-dev
```

1. 然后，在Vue应用程序的入口文件（通常是main.js）中导入Normalize.css：

```
javascriptCopy Code

import 'normalize.css/normalize.css'
```

1. 最后，在Vue组件中使用Normalize.css的样式即可。

请注意，由于Vue 3使用了单文件组件（SFC），因此您可以在组件级别引入Normalize.css。例如，在您的组件中，您可以添加以下代码：

```
htmlCopy Code

<template>
  <div class="my-component">
    ...
  </div>
</template>

<style lang="scss">
@import "~normalize.css/normalize.css";

.my-component {
  /* Add component-specific styles here */
}
</style>
```

这将仅在该组件中应用Normalize.css的样式，并且不会影响全局样式。

希望这可以帮助您在Vue 3中使用Normalize.css！