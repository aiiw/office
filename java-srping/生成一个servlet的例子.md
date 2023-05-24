1. 编写Java代码：将上面的代码保存为一个Java源文件，例如HelloWorld.java。

2. 编译Java代码：使用Javac编译器将源代码编译成.class文件。在命令行中，进入HelloWorld.java所在的目录并执行以下命令：

   ```
   Copy Codejavac -classpath /path/to/servlet-api.jar HelloWorld.java
   ```

   其中`/path/to/servlet-api.jar`是指向servlet-api.jar文件的路径。servlet-api.jar文件包含了Servlet API类库，你可以从Web容器的安装目录中找到它。

3. 配置Web应用程序：将生成的HelloWorld.class文件复制到Web应用程序的WEB-INF/classes目录下。在WEB-INF目录下，创建一个web.xml文件来配置Servlet，具体内容如下：

   ```
   xmlCopy Code<?xml version="1.0" encoding="UTF-8"?>
   <web-app xmlns="http://java.sun.com/xml/ns/javaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
                                http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
            version="3.0">
     <servlet>
       <servlet-name>HelloWorld</servlet-name>
       <servlet-class>HelloWorld</servlet-class>
     </servlet>
     <servlet-mapping>
       <servlet-name>HelloWorld</servlet-name>
       <url-pattern>/hello</url-pattern>
     </servlet-mapping>
   </web-app>
   ```

   在这个web.xml文件中，我们定义了一个名为HelloWorld的Servlet，并将它映射到URL模式/hello上。

4. 部署Web应用程序：将Web应用程序打包成WAR文件并部署到Web容器中。具体步骤可能因Web容器而异，通常需要在Web容器管理界面上传WAR文件并启动Web应用程序。

5. 访问Servlet：在浏览器中输入http://localhost:8080/yourapp/hello（其中localhost是你的Web服务器地址，8080是Web服务器端口，yourapp是你的Web应用程序名称），即可访问HelloWorld Servlet并查看它输出的内容。





code

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class HelloWorld extends HttpServlet {
  public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println("<html>");
    out.println("<head><title>Hello World</title></head>");
    out.println("<body>");
    out.println("<h1>Hello World!</h1>");
    out.println("</body></html>");
  }
}
```

