account = "king"
pwd = "123456"
money = 10000
b = True 
while b:
	Account = input("请输入账号：")
	Pwd = input("请输入密码：")
	if Account==account and Pwd==pwd:
		print("登陆成功！")
		A = 1
		while A<=3:
			choose = int(input("请选择功能：1.取款 2.存款 3.修改密码 4.查看余额 5.退出"))
			if choose==1:
				getMoney = int(input("请输入取款金额："))
				if getMoney>money:
					print("余额不足，无法取款！")
				else :
					print("取款成功！")
					Money = money-getMoney
			elif choose==2:
				saveMoney = int(input("请输入存款金额："))
				print("存款成功！")
				Money = money+saveMoney
			elif choose==3:
				print("暂时没有此功能！！！！！")
			elif choose==4:
				print("余额为：%d"%Money)
			elif choose==5:
				print("谢谢使用！")
				break
			else :
				print("指令错误！")
			A+=1	
	else:
		print("账号或密码错误,还有",b-1,"次机会")
		if b==1:
			print("密码错误达到三次，卡已被吞，请联系银行管理员！")
	b-=1	
