a = int(input("请输入一个整数："))
num = 0
count2 = 0
count3 = 0
while num<a:
	num+=1
	if num%2==0:
		count2+=num
	else :
		count3+=num
print("偶数数之和：%d\t奇数数之和：%d\n总和：%d"%(count2,count3,count2+count3))
