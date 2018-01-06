num = 3
account = "123456"
pwd = 123456
b = True
c= True
while num>=1:
	Account = input("请输入账号：")
	Pwd = int(input("请输入密码"))
	if Account==account and Pwd==pwd:
		print("登录成功！")
	else :
		print("账号或密码错误")
	num-=1
