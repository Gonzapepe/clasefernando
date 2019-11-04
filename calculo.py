import clase1

print('1.area del rectángulo.\n2.perimetro del rectangulo.\n3.area del circulo.\n4.perimetro del circulo\n5.diametro del circulo\n')
x=int(input('ingrese la formula: '))

if x == 1:
	b = int(input("ingrese la base: "))
	h = int(input("ingrese la altura: "))
	clase1.area_rectangulo(b,h)
if x == 2:
	l1 = int(input('ingrese el valor del lado 1: '))
	l2 = int(input("ingrese el valor del lado 2: "))
	clase1.perimetro_rectangulo(l1,l2)
if x == 3:
	r = int(input('ingrese el radio: '))
	clase1.area_circulo(r)
if x == 4:
	r = int(input('ingrese el radio: '))
	clase1.perimetro_circulo(r)
if x == 5: 
	r = int(input('ingrese el radio: '))
	clase1.diametro_circulo(r)