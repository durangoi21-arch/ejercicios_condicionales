dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if año > 0 and 1 <= mes <= 12 and 1 <= dia <= 30:

    dia += 1

    if dia > 30:
        dia = 1
        mes += 1

    if mes > 12:
        mes = 1
        año += 1

    print("Día siguiente:", dia, "/", mes, "/", año)

else:
    print("Fecha incorrecta")
