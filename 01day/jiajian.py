num1 = 0
num2 = 0
num3 = 0
while num1<100:
	num1+=1
	if num1%2!=0:
		num2+=num1
	else:
		num3+=num1
print("就是:",num2-num3)
