while True:
    nombre=input("Nombre: ").strip()
    #J   print (nombre) 
    nombre="".join(nombre.split())
    if nombre and nombre.replace(" ", "").isalpha():
        break
    print("Usa letras y no dejes el nombre vacío.")
nombre_normalizado=nombre.title()
print(f"Hola, {nombre_normalizado}") 