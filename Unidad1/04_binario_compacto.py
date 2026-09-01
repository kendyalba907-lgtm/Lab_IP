numero,binario=8,"" #se identifican las variables 
if numero==0:  print(0)#ve si el numero es igual a 0 y lo imprime si esto es verdadero
while numero>0:  binario,numero=str(numero%2)+binario,numero//2#mientras el numero sea mayor que 0 y calcula el residuo  y lo agrega a la variable binario y luego divide entre 2
print(binario) #imprime los resultados de la variable binario 