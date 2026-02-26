dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if mes == 2:
    valido = dia <= 28
elif mes in [4,6,9,11]:
    valido = dia <= 30
else:
    valido = dia <= 31

if 1 <= mes <= 12 and valido:
    print("Fecha correcta")
else:
    print("Fecha incorrecta")