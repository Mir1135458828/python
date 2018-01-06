print("*"*30)
name1 = "方便面"
price1 = 2
name2 = "冰红茶"
price2 = 2.5
name3 = "绿茶"
price3 = 3
name4 = "矿泉水"
price4 = 2
name5 = "香蕉"
price5 = 2
name6 = "苹果"
price6 = 4
name7 = "梨"
price7 = 3.5
print("便利店收银系统")
num = 0
while num<3:
	name = input("请输入商品名称：")
	if name==name1:
		print("商品名称：%s\n需要支付金额：%d元"%(name1,price1))
		print("*"*30)
	elif name==name2:
		print("商品名称：%s\n需要支付金额：%0.1f元"%(name2,price2))
		print("*"*30)
	elif name==name3:
		print("商品名称：%s\n需要支付金额：%d元"%(name3,price3))
		print("*"*30)
	elif name==name4:
		print("商品名称：%s\n需要支付金额：%d元"%(name4,price4))
		print("*"*30)
	elif name==name5:
		weight5 = input("请输入香蕉重量：")
		money5 = price5*float(weight5)
		print("商品名称：%s\n商品价格：%d斤/元\n商品重量：%0.2f斤\n支付金额：%0.2f元"%(name5,price5,float(weight5),money5))
		print("*"*30)
	elif name==name6:
		weight6 = input("请输入苹果的重量：")
		money6 = price6*float(weight6)
		print("商品名称：%s\n商品价格：%d斤/元\n商品重量：%0.2f斤\n支付金额：%0.2f元"%(name6,price6,float(weight6),money6))
		print("*"*30)
	elif name==name7:
		weight7 = input("请输入梨的重量：")
		money7 = price7*float(weight7)
		print("商品名称：%s\n商品价格：%d斤/元\n商品重量：%0.2f斤\n支付金额：%0.2f元"%(name7,price7,float(weight7),money7))
		print("*"*30)
	else :
		print("抱歉没有这种商品！")
	num+=1
