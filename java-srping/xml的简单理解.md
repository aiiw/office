xmlns：是默认命名空间。如果不加前缀(namespace-prefix)，即为默认命名空间，指定使用该命名空间的元素及子元素只要不加其他前缀，就都是默认命名空间的元素。



##### targetNamespace：命名本文档的命名空间,以方便给其他的xml引用.

##### 正确， `targetNamespace` 是指定用于命名当前 XML 文档中元素和属性的命名空间。它也用于将当前文档作为其他文档的引用。通过为目标命名空间分配唯一的 URI（Uniform Resource Identifier），可以确保在不同的 XML 文档和应用程序中使用相同的元素和属性名称时不会发生冲突。

