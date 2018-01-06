print("等腰三角形--------------------------------------------------")
a = 1
d = 1
c = 10
for b in range(5,0,-1):
	print(" "*30,"      "," "*b,"☣ "*a)
	a+=1
A = 1
for b in range(11,0,-1):
	print(" "*30,""," "*b,"☣ "*A)
	A+=1
C = 1
for b in range(15,0,-1):
	print(" "*26,""," "*b,"☣ "*C)
	C+=1
for q in range(1,7,1):
	print(" "*42,"☣☣")
'''
print("九九乘法表--------------------------------------------------")
for b in range(1,10,1):
	for d in range(1,b+1,1):
		print("%d*%d=%d"%(d,b,b*d),end=" ")
	print("")
'''
