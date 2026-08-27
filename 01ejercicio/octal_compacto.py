numero,octal=8,"" #se identifican las variables 
if numero==0:  print(0)#ve si el numero es igual a 0 y lo imprime si esto es verdadero
while numero>0:  octal,numero=str(numero%8)+octal,numero//8#mientras el numero sea mayor que 0 y calcula el residuo  y lo agrega a la variable octal y luego divide entre 8
print(octal) #imprime los resultados de la variable octal 