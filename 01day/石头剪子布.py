import random
num = 0
while num<5:
	user =int(input("请输入:1.石头 2.剪子 3.布\n"))
	numberber = random.randint(1,3)
	if user>0 and user<4:
		if user==1:
			if number==2:
				print("恭喜你，胜利了!",end="")
			elif number==3:
				print("不好意思，你竟然输给了人机!",end="")
			else:
				print("你竟然和一个人机打成了平手!",end="")
		if user==2:
			if number==3:
				print("恭喜你，胜利了!",end="")
			elif number==1:
				print("不好意思，你竟然输给了人机!",end="")
			else:
				print("你竟然和一个人机打成了平手!",end="")
		if user==3:
			if number==1:
				print("恭喜你，胜利了!",end="")
			elif number==2:
				print("不好意思，你竟然输给了人机!",end="")
			else:
				print("你竟然和一个人机打成了平手!",end="")
		choose = input("继续游戏(y):")
		if choose=="y":
			print("游戏继续！")
		else :
			print("游戏结束！")
			break
	else :
			print("请输入正确格式！")
	num+=1
