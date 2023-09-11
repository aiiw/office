XML XSD保存在单独的文档中，文档可以链接到XML文档以使用它。

**语法**
XSD的基本语法如下 - 

```xml
<?xml version = "1.0"?>

<xs:schema xmlns:xs = "http://www.w3.org/2001/XMLSchema">
   targetNamespace = "http://www.yiibai.com"
   xmlns = "http://www.yiibai.com" elementFormDefault = "qualified">

   <xs:element name = 'class'>
      <xs:complexType>
         <xs:sequence>
            <xs:element name = 'student' type = 'StudentType' minOccurs = '0' 
               maxOccurs = 'unbounded' />
         </xs:sequence>
      </xs:complexType>
   </xs:element>

   <xs:complexType name = "StudentType">
      <xs:sequence>
         <xs:element name = "firstname" type = "xs:string"/>
         <xs:element name = "lastname" type = "xs:string"/>
         <xs:element name = "nickname" type = "xs:string"/>
         <xs:element name = "marks" type = "xs:positiveInteger"/>
      </xs:sequence>
      <xs:attribute name = 'rollno' type = 'xs:positiveInteger'/>
   </xs:complexType>

</xs:schema>
XML
```

**`<Schema>`元素**

`Schema`是XSD的根元素，它始终是必需的。

```xml
<xs:schema xmlns:xs = "http://www.w3.org/2001/XMLSchema">
XML
```

上面的片段指定模式中使用的元素和数据类型是在 http://www.w3.org/2001/XMLSchema 命名空间中定义的，这些元素/数据类型以`xs`为前缀。 它始终是必需的。

```xml
targetNamespace = "http://www.yiibai.com"
XML
```

上面的片段指定此模式中使用的元素在 `http://www.yiibai.com` 命名空间中定义。 这是可选的。

```xml
xmlns = "http://www.yiibai.com"
XML
```

上面的片段指定默认命名空间是 `http://www.yiibai.com` 。

```
elementFormDefault = "qualified"
```

上面的片段表明，在任何XML Document中使用它们之前，在此模式中声明的任何元素都必须是名称空间限定的。它是可选的。

#### 引用架构

看看以下引用架构 - 

```xml
<?xml version = "1.0"?>

<class xmlns = "http://www.yiibai.com"
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation = "http://www.yiibai.com student.xsd">  

   <student rollno = "393">    
      <firstname>Dinkar</firstname>
      <lastname>Kad</lastname>
      <nickname>Dinkar</nickname>
      <marks>85</marks>
   </student>

   <student rollno = "493">     
      <firstname>Vaneet</firstname>
      <lastname>Gupta</lastname>
      <nickname>Vinni</nickname>
      <marks>95</marks>
   </student>

   <student rollno = "593">    
      <firstname>Jasvir</firstname>
      <lastname>Singh</lastname>
      <nickname>Jazz</nickname>
      <marks>90</marks>
   </student>
</class>
XML
```

上面的片段指定默认名称空间声明。 模式验证器检查此命名空间是否所有元素都是此命名空间的一部分。它是可选的。

```xml
xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation = "http://www.yiibai.com student.xsd">
XML
```

定义`XMLSchema-instance xsi`后，使用`schemaLocation`属性。 此属性有两个值，XML Schema的名称空间和位置，由空格分隔使用。它是可选的。

//更多请阅读：https://www.yiibai.com/xsd/xsd_syntax.html 