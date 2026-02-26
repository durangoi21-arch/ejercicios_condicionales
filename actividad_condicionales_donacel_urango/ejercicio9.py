nota = int(input("Ingrese nota (0-10): "))

notas = ["cero","uno","dos","tres","cuatro",
         "cinco","seis","siete","ocho","nueve","diez"]

if 0 <= nota <= 10:
    print(notas[nota])
else:
    print("Nota inválida")