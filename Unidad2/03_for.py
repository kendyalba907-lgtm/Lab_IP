for numero in range (3,7,2):
    cuadrado=numero**2
    print (numero, cuadrado)

materias=["Python", "Linux", "Interfaces"]
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}. {materia}")


materias=["Python", "Linux", "Interfaces"]
for materia in materias:
    print(materia)


cadena="0123456789abcdef"
for letra in cadena:
    print(letra)

for i in range(len(cadena)):
    print(cadena[i])