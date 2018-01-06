num = 0
Y = "Y"
N = "N"
while num<3:
	height = int(input("请输入你的身高："))
	money = int(input("请输入你的身价："))
	color = int(input("请输入你的颜值分："))
	print("*"*30,"\n根据你所输入的信息，系统的评价为：")
	if height>=180 and money>=1000000 and color>=90:
		print("\t\t你是一个高富帅","\n","*"*30)
	elif height<180 and money>=1000000 and color>=90:
		print("\t\t你是一个富帅","\n","*"*30)
	elif height<180 and money<1000000 and color>=90:
		print("\t\t你是一个帅","\n","*"*30)
	elif height<160 and money<1000000 and color<90:
		print("\t\t你是一个矮穷矬","\n","*"*30)
