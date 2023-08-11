# print(root.iter('year')) #全文搜索
# print(root.find('country')) #在root的子节点找，只找一个
# print(root.findall('country')) #在root的子节点找，找所有

import xml.etree.ElementTree as ET

tree = ET.parse("b.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print('========>', child.tag, child.attrib, child.attrib['name'])
    for i in child:
        print(i.tag, i.attrib, i.text)

# #只遍历year 节点
# for node in root.iter('year'):
#     print(node.tag, node.text)
# #---------------------------------------

# import xml.etree.ElementTree as ET

# tree = ET.parse("1.xml")
# root = tree.getroot()

# #修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set('updated', 'yes')
#     node.set('version', '1.0')
# tree.write('test.xml')

# #删除node
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)

# tree.write('output.xml')

# #在country内添加（append）节点year2
# import xml.etree.ElementTree as ET
# tree = ET.parse("1.xml")
# root = tree.getroot()
# for country in root.findall('country'):
#     for year in country.findall('year'):
#         if int(year.text) > 2009:
#             year2 = ET.Element('year2')
#             year2.text = '新年'
#             year2.attrib = {'update': 'yes'}
#             year.append(year2)  #往country节点下添加子节点

# tree.write('b.xml')