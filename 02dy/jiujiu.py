num1 = 1
while num1<=9:
	num2 = 1
	while num2<=num1:
		print("%d*%d=%d"%(num2,num1,num2*num1),end=" ")
		num2+=1
	print("")
	num1+=1
