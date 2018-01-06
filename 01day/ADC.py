num = 0
number = 0
xing = "*"*30
while num<3:
	name = input("请输入你要玩的位置：\n")
	if name == "ADC":
		print("请选择你要操作的英雄: 1.后裔 2.虞姬 3.黄忠 4.马克 5.李元芳")
		number = int(input())
		if number==1:
			print("看，天空一只鸟飞过！\n%s"%xing)
		elif number==2:
			print("我的项羽在哪里！\n%s"%xing)
		elif number==3:
			print("一把年纪了，还在拆迁队干着！\n%s"%xing)
		elif number==4:
			print("摩擦摩擦，是魔鬼的步伐!\n%s"%xing)
		elif number==5:
			print("在看我，一直在看着我！\n%s"%xing)
		else :
			print("没有这个英雄！\n%s"%xing)
	else :
		print("你想要的位置已经被抢了！\n%s"%xing)
		
	num+=1
