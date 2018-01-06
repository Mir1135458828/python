num = 0
while num<3:
	age = int(input("请输入年龄：\n"))
	if age<18:
		print("不准谈恋爱")
	elif age>=18 and age<=20:
		print("抓紧时间找对象")
	elif age>20 and age<=30:
		print("赶紧结婚吧！")
	else:
		print("系统出错！！！")
	num+=1
