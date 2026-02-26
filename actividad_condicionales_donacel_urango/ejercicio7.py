dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if año <= 0:
    print("Fecha incorrecta")
else:
    if mes == 2:
        valido = 1 <= dia <= 28
    elif mes in [4, 6, 9, 11]:
        valido = 1 <= dia <= 30
    elif 1 <= mes <= 12:
        valido = 1 <= dia <= 31
    else:
        valido = False

    if valido:
        print("Fecha correcta")
    else:
        print("Fecha incorrecta")
