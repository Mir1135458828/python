a = 1
b = True
while b:
	print("* "*a)
	if a==5:
		while a>=1:
			a-=1
			print("* "*a)
			if a==1:
				b = False
				break
	a+=1
