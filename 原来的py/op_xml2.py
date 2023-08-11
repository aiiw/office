import xml.etree.ElementTree as ET
tree = ET.parse('xml01.xml')
root = tree.getroot()
print(root.tag)#根节点标签
for child in root:
     print(child.tag,child.attrib,child.text)  #二级节点标签、属性、内容

def walkData(root_node, level, result_list):  
    global unique_id  
    temp_list =[unique_id, level, root_node.tag, root_node.attrib,root_node.text]  
    result_list.append(temp_list)  
    unique_id += 1  
      
    #遍历每个子节点  
    children_node = root_node.getchildren()  
    if len(children_node) == 0:  
        return  
    for child in children_node:  
        walkData(child, level + 1, result_list)  
      

unique_id=1
list1=[]
root_node=root
level=1
walkData(root_node, level, list1)
for i in list1:
    print(i)