Symbol的主要作用是创建唯一的、不可变的值，通常用作对象属性名。由于Symbol类型的值是独一无二的，因此它们可以确保对象属性名的唯一性。

举个例子，假设我们有一个应用程序，需要在各个模块之间传递一些数据。为了避免命名冲突，我们可能会使用一个全局的对象来保存这些数据，例如：

```
javascript复制代码const myAppData = {};

// 模块1存储数据
myAppData.data1 = 'some data';

// 模块2也想存储数据，但是不知道data1已经被占用了，于是就起名为data2
myAppData.data2 = 'more data';
```

在这个例子中，如果多个模块都试图往`myAppData`对象中添加属性，那么就有可能出现属性名冲突，导致数据被覆盖或者丢失。

为了避免这种情况，我们可以使用Symbol作为属性名，确保每个属性名的唯一性，例如：

```
javascript复制代码const myAppData = {};

// 模块1存储数据
const dataKey1 = Symbol('data1');
myAppData[dataKey1] = 'some data';

// 模块2也想存储数据，使用另一个Symbol作为属性名
const dataKey2 = Symbol('data2');
myAppData[dataKey2] = 'more data';
```

在这个例子中，我们使用了两个不同的Symbol作为属性名，确保了它们的唯一性。这样就可以避免属性名冲突的问题，保证数据的安全性和正确性。