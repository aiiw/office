def remonths(year,mon,fa="0"):
	if mon in ['01','03','05','07','08','10','12']:
		b=(year+"-"+mon+"-01",year+"-"+mon+"-31")
		return b
	elif mon in ['04','06','09','11']:
		b=(year+"-"+mon+"-01",year+"-"+mon+"-30")
		return b
	elif mon in ['02'] and fa=="0":
		b=(year+"-"+mon+"-01",year+"-"+mon+"-28")
		return b
	elif mon in ['02'] and fa=="1":
		b=(year+"-"+mon+"-01",year+"-"+mon+"-29")
		return b
if __name__ == '__main__':
	print(remonths("2021", "02"))