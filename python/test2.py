import random
proxys = [{'http': '39.137.69.10:8080'},
              {'http': '111.206.6.101:80'},
              {'http': '120.210.219.101:8080'},
              {'http': '111.206.6.101:80'},
              {'https': '120.237.156.43:8088'}]
proxy = random.choice(proxys)
print(proxy)