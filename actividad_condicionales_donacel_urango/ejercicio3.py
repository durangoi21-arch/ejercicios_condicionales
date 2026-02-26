a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a % b == 0 or b % a == 0:
    print("Uno es múltiplo del otro")
else:
    print("No son múltiplos")