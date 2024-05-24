表达式语言（EL）在JSP中非常强大，可以用于各种场景，包括变量的访问、属性的获取、集合的迭代、条件判断等。以下是一些EL在JSP中的常用用法和操作：

### 1. 访问变量和属性

- **访问属性**：`${variable.property}` 或 `${variable['property']}`。可以用于访问JavaBean的属性或Map中的值。
- **访问会话属性**：`${sessionScope.variable}`，也可以通过`${session.variable}`访问。
- **访问请求属性**：`${requestScope.variable}` 或 `${request.variable}`。
- **访问页面属性**：`${pageScope.variable}`。

### 2. 操作集合

- **访问数组或List中的元素**：`${array[1]}` 或 `${list[0]}`。
- **访问Map中的值**：`${map['key']}`。
- **迭代集合**：配合JSP标签库（如JSTL）使用，循环遍历集合。

### 3. 条件判断

- **三元运算符**：`${condition ? 'value_if_true' : 'value_if_false'}`。
- **布尔运算**：`${variable > 10}`，可以用于简单的比较和逻辑操作。

### 4. 字符串操作

- **字符串连接**：`${"Hello, " + "world!"}`。
- **字符串长度**：`${variable.length()}`。

### 5. 日期和时间

- **格式化日期**：可以通过JSTL标签库配合EL来格式化日期。

### 6. JSTL（JavaServer Pages Standard Tag Library）配合EL

- **`c:forEach`**：用于循环迭代集合。
- **`c:if`**：用于条件判断。
- **`c:choose`**：类似于`switch-case`的逻辑。
- **`c:set`**：设置变量。

### 示例

```
jspCopy Code<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!-- 访问变量 -->
${user.name} <!-- 访问user对象的name属性 -->

<!-- 条件判断 -->
${user.age > 18 ? 'Adult' : 'Minor'} <!-- 三元运算符 -->

<!-- 循环迭代集合 -->
<c:forEach var="item" items="${items}">
    ${item}
</c:forEach>
```