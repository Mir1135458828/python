import random  #导入随机数
number =random.randint(1,100)  #生成1-100的随机数
for i in range(1,11,1):
	user = int(input("请猜一个数字："))
	if user>number:
		print("比%d小"%user)
	elif user==number:
		print("恭喜你，猜对了！")
		break
	elif user<number:
		print("比%d大"%user)
