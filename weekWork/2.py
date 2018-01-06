import random
number = random.randint(1,100)
for i in range(1,11):
	a = int(input("请猜一个数字："))
	if a>number:
		print("比%d小"%a)
	elif a==number:
		print("恭喜你，猜对了！")
		break
	else :
		print("比%d大"%a)
