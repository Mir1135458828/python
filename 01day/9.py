name = "张三"
A = "king"
pwd = "666666"
account = input("请输入账户：")
password = input("请输入密码：")
if account==A and password==pwd:
	print("账户密码正确")
else :
	print("密码错误！")
money = 20000#现有存款
getMoney = int(input("请输入要取款的金额："))
if money>=getMoney:
	Money = money-getMoney
	print("*"*30)
	print("账户：%s\n密码******\n用户姓名：%s\n原有金额：%0.2f元\n取款金额：%0.2f元\n剩余金额：%0.2f元"%(account,name,money,getMoney,Money))
	print("*"*30)
else :
	print("余额不足，无法操作！")
