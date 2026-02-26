compra = float(input("Valor de la compra: "))

if compra > 300000:
    total = compra * 0.8
else:
    total = compra

print("Total a pagar:", total)