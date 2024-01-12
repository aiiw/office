import os,sys,re
# os.system("c:/windows/system32/netstat.exe " "-nao |findstr '8075'")
# os.system('')

print(os.system('netstat -nao|findstr "8" > 1.txt'))
