with open('C:/Users/11608/1.txt', 'r') as file:
    data = file.read()
list=[]
list=data.split(';')
for i in list:
    if i.find('maven') !=-1:
        print("aiiw:",i)