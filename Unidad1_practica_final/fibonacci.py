numero=int(input("ingresa un numero: "))
es_primo=True
if numero <= 1:
    es_primo=False
else:
    i=2 
    while i<numero:
        if numero%i==0:
            es_primo=False
        i=i+1
if es_primo == True:
    print("Es primo")
    a=0
    b=1
    while a<numero:
        siguiente=a+b
        a=b
        b=siguiente
    if a==numero:
        print("El numero pertenece a Fibonacci")
    else: 
       print("El numero no pertenece a Fibonacci") 
else:
    print("No es primo")    