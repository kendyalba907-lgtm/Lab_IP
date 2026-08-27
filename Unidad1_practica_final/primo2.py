numero=int (input("ingresa un numero: "))
i=2
while i<=numero:
    if numero%i==0:
         primo=0
    i=i+1
if primo==1:
    print("Es primo")
if primo==0:
    print("No es primo")    