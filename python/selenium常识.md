```
def click_elements(item):

    els = item.find_elements_by_css_selector(".loadTree.fa.fa-angle-right.collapsed-icon")
    if els:
       
        for el in els:
            try:
                
                outer_html = item.get_attribute('outerHTML')
                print(outer_html)
                print("======================================")
                el.click()  # el是批带有下级菜单图标图标图标图标图标图标图标图标图标图标图标图标图标
                time.sleep(1)
                outer_html = item.get_attribute('outerHTML')
          
                print(outer_html)
                print("一级菜单", item.text)
         
```

一 

1 item是一个动态的元素,受el.click影响,但是不会马上生效,要延迟1秒才会变化 

2 item.text会获取所有子节点的文本.



要获取第一个子节点的文本，你可以使用find_element_by_xpath或find_element_by_css_selector来找到第一个子节点元素，然后使用.text来获取其文本内容。下面是一个示例代码：

```
pythonCopy Code# 使用 XPath 找到第一个子节点元素
first_child = item.find_element_by_xpath("./*[1]")
# 获取第一个子节点元素的文本内容
first_child_text = first_child.text
print("第一个子节点的文本内容：", first_child_text)
```