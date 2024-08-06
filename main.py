from datetime import datetime
import json

def abrirArchivo():
    miJson=[]
    with open("info2.json", encoding="utf-8") as openfile:
        miJson= json.load(openfile)
        return miJson
archivo=abrirArchivo()
print(archivo)

def guardarArchivo(miData):
    with open("info2.json","w") as outfile:
        json.dump(miData,outfile)

print("Bienvenidoss!")
print("-------------Menú-------------")
print("""
    1. Registrar ventas
    2. Registrar compras
    3. Informe de ventas
    4. Informes de stock
      """)

opc=int(input("Elige una de las opciones de nuestro menú: "))
miInfo=[]
if opc==1:
    miInfo=abrirArchivo()
    for i in miInfo[0]["ventas"]:
        idR = int(input("Ingresa el id de la venta: "))
        fechaR = datetime.now()
        nombreCR = input("Ingresa el nombre del cliente: ")
        direccionR = input("Ingresa la dirección del cliente: ")
        registroR = {
            "id": idR,
            "fecha": fechaR,
            "nombre": nombreCR,
            "direccion": direccionR,
        }
        miInfo = abrirArchivo()
        miInfo[0]["ventas"].append(registroR)
        guardarArchivo(miInfo)
        print("La venta se guardó correctamente.")
        