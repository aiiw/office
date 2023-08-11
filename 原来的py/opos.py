import os
with open(r"123.txt","a") as ll:
	ll.writelines("--/n2323\n")
	ll.writelines("--/n2323")
	ll.writelines("--/n2323")
	ll.close()
with open(r"123.txt","r+") as ll:
	print(ll.readlines())


# os.system("dig @114.114.114.114 registry-1.docker.io")

