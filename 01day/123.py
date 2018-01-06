"""
weight = int(input("请输入体重(Kg)："))
height = int(input("请输入身高(cm): "))
height1 = height/100
BMI = weight/(height1*height1)
if BMI<18.5:
	print("过轻")
elif BMI>=18.5 and BMI<25:
	print("正常")
elif BMI>=25 and BMI<28:
	print("过重")
elif BMI>=28 and BMI<=32:
	print("肥胖")
else :
	print("严重肥胖")
"""
account = "123456"
password = "abc"
Account = input("请输入账号：")
Password = input("请输入密码：")
if account==Account and password==Password:
	print("登录成功！")
elif account!=Account and password==Password:
	print("账号不对！")
elif password!=Password and account==Account:
	print("密码不对！")
else :
	print("都不对！！！")
