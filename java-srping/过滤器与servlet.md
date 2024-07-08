在 Java Web 应用程序中，Filter 和 Servlet 是两种不同的组件，用于处理 HTTP 请求和响应。它们之间的主要区别在于它们的功能和用途：

1. **Filter（过滤器）**：
   - 过滤器用于在请求进入 Servlet 前执行预处理操作，或在响应返回客户端前执行后处理操作。
   - 过滤器可以对请求或响应进行修改、重定向、包装等操作，以实现一些通用的功能，如身份验证、日志记录、字符编码转换等。
   - 过滤器通过实现 `javax.servlet.Filter` 接口来定义，并通过在 `web.xml` 或使用注解配置来指定过滤器的 URL 匹配模式。
2. **Servlet（Servlet）**：
   - Servlet 是一种用于处理客户端请求的 Java 类，通常用于生成动态的 Web 内容。
   - Servlet 处理特定 URL 的请求，并生成相应的响应。它可以读取表单数据、调用业务逻辑、生成 HTML、XML 或其他类型的响应。
   - Servlet 通过扩展 `javax.servlet.http.HttpServlet` 类或实现 `javax.servlet.Servlet` 接口来定义，并通过在 `web.xml` 或使用注解配置来指定 Servlet 的 URL 映射。

常用的语法示例：

1. **Filter 的配置**（在 `web.xml` 中配置）：

   ```
   xmlCopy Code<filter>
       <filter-name>MyFilter</filter-name>
       <filter-class>com.example.MyFilter</filter-class>
   </filter>
   <filter-mapping>
       <filter-name>MyFilter</filter-name>
       <url-pattern>/my/*</url-pattern>
   </filter-mapping>
   ```

2. **Filter 的注解配置**（在 Servlet 类上使用注解）：

   ```
   javaCopy Code
   @WebFilter(filterName = "MyFilter", urlPatterns = "/my/*")
   public class MyFilter implements Filter {
       // Filter 方法实现
   }
   ```

3. **Servlet 的配置**（在 `web.xml` 中配置）：

   ```
   xmlCopy Code
   <servlet>
       <servlet-name>MyServlet</servlet-name>
       <servlet-class>com.example.MyServlet</servlet-class>
   </servlet>
   <servlet-mapping>
       <servlet-name>MyServlet</servlet-name>
       <url-pattern>/myservlet</url-pattern>
   </servlet-mapping>
   ```

4. **Servlet 的注解配置**（在 Servlet 类上使用注解）：

   ```
   javaCopy Code
   @WebServlet(name = "MyServlet", urlPatterns = "/myservlet")
   public class MyServlet extends HttpServlet {
       // Servlet 方法实现
   }
   ```

无论是使用 XML 配置还是注解配置，都可以达到相同的效果，选择哪种方式取决于个人或项目的偏好和要求。