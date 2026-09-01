numero, hexadecimal=30, ""
if numero==0:
    print("0")
while numero>0:
    residuo=numero%16
    hexadecimal="0123456789ABCDEF"[residuo]+hexadecimal
    numero=numero//16
print(hexadecimal)