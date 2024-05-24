在Spring MVC中，您不需要显式地实例化`HttpServletRequest`对象来处理HTTP请求。Spring MVC会自动将`HttpServletRequest`对象作为方法的参数传递给您的控制器方法。您只需要在方法的参数列表中声明`HttpServletRequest`类型的参数，Spring MVC会在运行时自动将请求对象传递给该参数。

例如，您可以在控制器方法中这样使用`HttpServletRequest`：

```
javaCopy Code@GetMapping("/test2")
public String test2(HttpServletRequest request) {
    // 在方法中使用 request 对象
    String abc = request.getParameter("bbb");
    return "hello world12 " + abc;
}
```

在上面的示例中，我们通过`request.getParameter("bbb")`获取了名为`bbb`的请求参数的值。

总之，在Spring MVC中，您不需要手动实例化`HttpServletRequest`对象，只需在方法参数中声明它，Spring MVC会自动将请求对象传递给它。

1. `HttpServletRequest`：表示HTTP请求对象，用于获取HTTP请求的信息，如请求参数、请求头等。
2. `HttpServletResponse`：表示HTTP响应对象，用于控制和发送HTTP响应给客户端。
3. `HttpSession`：表示HTTP会话对象，用于在不同的请求之间存储和共享数据。
4. `Principal`：表示当前用户的身份信息，通常用于进行身份验证和授权。
5. `Locale`：表示客户端的语言环境，用于国际化和本地化。
6. `Model`：用于在控制器方法中存储数据，传递给视图渲染。
7. `ModelMap`：`Model`的子类，用于存储和管理模型数据。
8. `RedirectAttributes`：用于在重定向时传递数据给重定向的目标地址。
9. `WebRequest`：Spring提供的包装了`HttpServletRequest`和`HttpServletResponse`的接口，提供了更多的功能和方法。

1. `HttpServletRequest` - Represents the HTTP request object.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(HttpServletRequest request) {
       String value = request.getParameter("parameterName");
       // Do something with the value
       return "exampleView";
   }
   ```

2. `HttpServletResponse` - Represents the HTTP response object.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(HttpServletResponse response) {
       // Set response headers or write to the response
       return "exampleView";
   }
   ```

3. `HttpSession` - Represents the HTTP session object.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(HttpSession session) {
       session.setAttribute("key", "value");
       // Retrieve or manipulate session attributes
       return "exampleView";
   }
   ```

4. `Principal` - Represents the current user's identity.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(Principal principal) {
       String username = principal.getName();
       // Do something with the username
       return "exampleView";
   }
   ```

5. `Locale` - Represents the client's locale.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(Locale locale) {
       String language = locale.getLanguage();
       // Do something based on the client's language
       return "exampleView";
   }
   ```

6. `Model` - Used for storing model attributes.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(Model model) {
       model.addAttribute("attributeName", "attributeValue");
       // Add model attributes to be used in the view
       return "exampleView";
   }
   ```

7. `ModelMap` - A subclass of `Model` for storing and managing model attributes.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(ModelMap modelMap) {
       modelMap.addAttribute("attributeName", "attributeValue");
       // Add model attributes similar to Model
       return "exampleView";
   }
   ```

8. `RedirectAttributes` - Used for passing data during redirection.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(RedirectAttributes redirectAttributes) {
       redirectAttributes.addAttribute("param", "value");
       // Add attributes to be passed during redirection
       return "redirect:/redirectedUrl";
   }
   ```

9. `WebRequest` - Interface wrapping `HttpServletRequest` and `HttpServletResponse`.

   ```
   javaCopy Code@GetMapping("/example")
   public String example(WebRequest webRequest) {
       String value = webRequest.getParameter("parameterName");
       // Use methods from HttpServletRequest or HttpServletResponse
       return "exampleView";
   }
   ```

Servlet 中有几个内置的对象，它们是由 Servlet 容器创建和管理的。以下是一些常见的内置对象：

1. **HttpServletRequest（HTTP 请求对象）**：代表客户端的 HTTP 请求。通过这个对象，可以获取客户端提交的请求信息，如请求参数、请求头等。
2. **HttpServletResponse（HTTP 响应对象）**：代表服务器对客户端的 HTTP 响应。通过这个对象，可以控制向客户端发送的响应内容，如设置响应头、写入响应体等。
3. **HttpSession（HTTP 会话对象）**：代表客户端与服务器之间的一次会话。通过这个对象，可以在不同的请求之间共享数据，实现会话状态的管理。
4. **ServletContext（Servlet 上下文对象）**：代表当前 Web 应用的 Servlet 环境。通过这个对象，可以获取 Web 应用的配置信息、共享数据等。
5. **ServletConfig（Servlet 配置对象）**：代表当前 Servlet 的配置信息。通过这个对象，可以获取 Servlet 的初始化参数等配置信息。

这些内置对象可以通过相应的方法或属性来获取，并且可以在 Servlet 的生命周期内使用。在编写 Servlet 时，通常会使用这些内置对象来处理客户端的请求，并生成对应的响应。



这些内置的对象不需要手动创建，Servlet 容器会自动为每个请求创建它们的实例。下面是一个简单的示例，演示如何在 Servlet 中使用这些内置对象：

```
javaCopy Codeimport java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ExampleServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取请求参数
        String username = request.getParameter("username");

        // 设置响应内容类型
        response.setContentType("text/html");

        // 获取当前会话或创建新的会话
        HttpSession session = request.getSession();
        Integer visitCount = (Integer) session.getAttribute("visitCount");
        if (visitCount == null) {
            visitCount = 1;
        } else {
            visitCount++;
        }
        session.setAttribute("visitCount", visitCount);

        // 输出响应内容
        response.getWriter().println("<html><body>");
        response.getWriter().println("<h1>Hello, " + username + "!</h1>");
        response.getWriter().println("<p>Visit count: " + visitCount + "</p>");
        response.getWriter().println("</body></html>");
    }
}
```

在这个示例中，我们通过 `doGet()` 方法处理 GET 请求。在方法参数中，`HttpServletRequest` 和 `HttpServletResponse` 对象是由容器创建并传递给 Servlet 的，无需手动创建。我们可以直接使用它们来获取请求信息和发送响应。另外，`HttpSession` 对象也是由容器管理的，我们可以通过 `request.getSession()` 方法获取当前会话对象，无需手动创建。