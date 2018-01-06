a = 1
b = 0
while a<100:
	if a%2==0:
		b-=a
	else:
		b+=a
	a+=1
print(b)
