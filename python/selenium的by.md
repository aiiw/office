`By` 类提供了许多不同的定位器，您可以使用这些定位器根据元素的不同属性来定位元素。以下是一些常用的定位器：

- `By.ID`：根据元素的 id 属性定位元素。
- `By.NAME`：根据元素的 name 属性定位元素。
- `By.CLASS_NAME`：根据元素的 class 属性定位元素。
- `By.TAG_NAME`：根据元素的标签名定位元素。
- `By.LINK_TEXT`：根据元素的链接文本定位元素。
- `By.PARTIAL_LINK_TEXT`：根据元素的链接部分文本定位元素。
- `By.XPATH`：根据 XPath 表达式定位元素。
- `By.CSS_SELECTOR`：根据 CSS 选择器定位元素。

例如，在上面的代码示例中，我们使用了`By.XPATH`定位器来定位相对XPath `"./tr/td[3]"` 所表示的元素。如果您想要使用其他定位器，只需要将第一个参数替换为对应的定位器即可。

例如，如果您想使用`By.ID`定位器来查找具有特定 ID 的元素，可以使用以下代码：

```
pythonCopy Code# 导入selenium库
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开网页
driver.get("https://example.com")

# 使用ID定位器查找元素
my_element = driver.find_element(By.ID, "my-element-id")
```

在上面的代码中，我们将`By.XPATH`替换为了`By.ID`，并将相对XPath `"./tr/td[3]"` 替换为了具有特定ID的元素的ID。