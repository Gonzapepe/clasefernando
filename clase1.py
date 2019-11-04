import math
def area_rectangulo(b,h):
	area = b * h
	return print("El area del rectángulo es: ", int(area) )

def perimetro_rectangulo(l1,l2):
	perimetro = l1*2 + l2*2
	return print("El perimetro es: ", perimetro)

def area_circulo(R):
    area=math.pi*R**2
    return print('el area del circulo es %.3f ' % area)

def perimetro_circulo(R):
	perimetro = 2*math.pi*R
	return print('el perimetro es: ', perimetro)

def diametro_circulo(R):
	diametro = 2*R
	return print('el diametro es: ', diametro)

