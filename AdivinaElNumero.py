import random

print("¡Hola!¿Cómo te llamas?")

nombre=input()

print("Bienvenido/a: ",nombre,"\nEstoy pensando en un número del 1 al 100. ¿Puedes adivinarlo?")
print("(Recuerda que solo tienes 6 intentos)")

intentos=0

numero= random.randint(1,100)


while intentos<6:
	intentos=intentos+1
	print("Introduce un número")
	numingresado= int(input())
	if numero<numingresado:
		print("El número a adivinar es menor que el ingresado.")
		

	elif numero>numingresado:
		print("El número a adivinar es mayor que el ingresado.")
		

	else:
		print("Correcto! has adivinado el número. Felicitaciones!")

if intentos==6:
	print("Has acabado tus intentos")

