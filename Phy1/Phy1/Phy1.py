import math
print("Филатова Анатасия Евгеньевна ИУ5-55Б")
while True:
	try:
		A=float(input("Введите А: "))
		break
	except ValueError:
		print("А не число! Повторите ввод!")

while True:
	try:
		B=float(input("Введите B: "))
		break
	except ValueError:
		print("B не число! Повторите ввод!")

while True:
	try:
		C=float(input("Введите C: "))
		break
	except ValueError:
		print("C не число! Повторите ввод!")

print("x*x*a+x*b+c = 0")
D = B*B-4*A*C
print ("D= ", D)
if D>0:
	x1 = (-B+math.sqrt(D))/2*A
	x2 = (-B-math.sqrt(D))/2*A
	print("x1= ",x1, "; x2= ", x2)
elif D<0:
	print("Нет корней!")
elif D==0:
	x = (-B)/2*A
	print("x= ", x)
