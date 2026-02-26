cantidad = int(input("Cantidad de llantas: "))

if cantidad < 5:
    precio = 30000
elif cantidad <= 10:
    precio = 25000
else:
    precio = 20000

total = cantidad * precio

print("Precio por llanta:", precio)
print("Total a pagar:", total)