s = '''${if(len({no2}) == 0, "", if('*' in {no2}, "AND t.xmda033 LIKE '%" + {no2}.replace('*', '%') + "%'", "AND t.xmda033='" + {no2} + "'"))}'''

# 使用 format 方法将变量值插入到字符串中
formatted_s = s.format(no2='no3')

print(formatted_s)