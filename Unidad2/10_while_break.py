while True:
    opcion=input("Elige A, B o C:").strip().upper()
    if opcion in ["A","B","C"]:
        break 
    print("Opción inválida, intenta de nuevo")
print(f"Elegiste la opción {opcion}")