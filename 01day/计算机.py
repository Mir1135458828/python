num = 0
while num<3:
	jia = "+"
	jian = "-"
	cheng = "*"
	chu = "/"
	pingfang = "**"
	x = int(input("请输入x:"))
	y = int(input("请输入y:"))
	a = input("请输入（+ - * / **）：")
	if a == jia:
		print("x+y=",x+y)
	elif a == jian:
		print("x-y=",x-y)
	elif a == cheng:
		print("x*y=",x*y)
	elif a == chu:
		print("x/y=",float(x/y))
	elif a == pingfang:
		print("x**y=",x**y)
