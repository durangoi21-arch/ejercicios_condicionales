numero = input("Ingrese un número de tres cifras: ")

if numero == numero[::-1]:
    print("Es capicúa")
else:
    print("No es capicúa")