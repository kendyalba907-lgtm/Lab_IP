edad=18
tiene_credencial=True
tiene_adeudo=False
if edad >=18 and tiene_credencial and not tiene_adeudo:
    es_mayor=True 
    autorizado=True
else:
    autorizado=False
print(autorizado)