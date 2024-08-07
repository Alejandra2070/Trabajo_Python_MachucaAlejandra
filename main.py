from datetime import datetime
#importamos json para trabajar con el
import json

def abrirArchivo2():
    miJson3=[]
    with open("info.json", encoding="utf-8") as openfile:
        miJson3= json.load(openfile)
        return miJson3
def guardar2(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)
######################################
def abrirArchivo():
    miJson=[]
    with open("info2.json", encoding="utf-8") as openfile:
        miJson= json.load(openfile)
        return miJson
archivo=abrirArchivo()

def guardarArchivo(miData):
    with open("info2.json","w") as outfile:
        json.dump(miData,outfile)
#####################################
def abrir():
    miJson2=[]
    with open("info3.json", encoding="utf-8") as openfile:
        miJson2= json.load(openfile)
        return miJson2
archivo2=abrir()

def guardar(miData):
    with open("info3.json","w") as outfile:
        json.dump(miData,outfile)
######################################

#creamos un menú para facilitar la realización del programa
print("#################################")
print("-------BIENVENIDOSSSSS!-------")
print("#################################")
print("-------------Menú-------------")
print("""
    1. Registrar ventas
    2. Registrar compras
    3. Informe de ventas
    4. Informes de stock
    5. Salir del programa
      """)

#elegir cual de las opciones va a realizar
opc=int(input("Elige una de las opciones de nuestro menú: "))
miInfo=[]
if (opc==1):
    miInfo=abrirArchivo() #abrimos la libreria
    #ingresar la información de la venta
    idR = int(input("Ingresa el id de la venta: "))
    fechaR = int(input("Ingresa la fecha de la venta: "))
    nombreCR = input("Ingresa el nombre del cliente: ")
    direccionR = int(input("Ingresa la dirección del cliente: "))
    nombreER = input("Ingresa el nombre del empleado que realizó la venta: ")
    cargoER = input("Ingresa el cargo del empleado que realizó la venta: ")
    nombrePR = input("Ingresa el nombre del producto vendido: ")
    cantidadPR = int(input("Ingresa la cantidad vendida del producto: "))
    precioPR = int(input("Ingresa el precio del producto vendido: "))
    #guardar la información de la venta
    registroR = {
        "id": idR,
        "fechaVenta": fechaR,
        "nombreCliente": nombreCR,
        "direccion": direccionR,
        "nombreEmpleado": nombreER,
        "cargoEmpleado": cargoER,
        "nombreProducto": nombrePR,
        "cantidad": cantidadPR,
        "precio": precioPR
    }
    #abrir la libreria para guardar la información
    miInfo = abrirArchivo()
    miInfo[0]["ventas"].append(registroR)
    guardarArchivo(miInfo)
    #una vez guardada, se le informa al usuario
    print("La venta se guardó correctamente.")
elif(opc==2):
    miInfo=abrir() #abrir la libreria
    #pedir la información de la compra
    idPro = int(input("Ingresa el id de la compra: "))
    fechaPro = int(input("Ingresa la fecha de la compra: "))
    nombreProR = input("Ingresa el nombre del proveedor: ")
    contactoPro = int(input("Ingresa el contacto del proveedor: "))
    nombrePro = input("Ingresa el nombre del producto: ")
    cantidadPro = int(input("Ingresa la cantidad del producto vendido: "))
    precioPro = int(input("Ingresa el precio de la compra: "))
    #guardar la información de la compra realizada
    registro = {
        "id": idPro,
        "fecha": fechaPro,
        "nombre": nombreProR,
        "contacto": contactoPro,
        "nombreProveedor": nombrePro,
        "cantidad": cantidadPro,
        "precio": precioPro
    }
    #abrir la libreria y guardar la información en ella
    miInfo = abrir()
    miInfo[0]["Compras"].append(registro)
    guardar(miInfo)
    #se informa que la compra ya se guardó
    print("La compra se realizó correctamente.")
elif(opc==3):
    miInfo=abrirArchivo() #abrir la libreria
    #mostrar la información que hay en el json sobre las ventas
    for i in miInfo[0]["ventas"]:
        print("########################")
        print("ID:",i["id"])
        print("Fecha de la venta:",i["fechaVenta"])
        print("Nombre del cliente:",i["nombreCliente"])
        print("Dirección del cliente:",i["direccion"])
        print("Nombre del empleado:",i["nombreEmpleado"])
        print("Cargo del empleado:",i["cargoEmpleado"])
        print("Nombre del producto:",i["nombreProducto"])
        print("Cantidad vendida:",i["cantidad"])
        print("Precio del producto:",i["precio"])
        #hace la multiplicación para mostrar el valor total por la compra
        print("Precio total:",i["precio"]*i["cantidad"])

elif(opc==4):
    miInfo=abrirArchivo2() #se abre la libreria para mostrar la información que hay en el json sobre la panadería
    for i in miInfo[0]["Panaderia"]:
        print("########################")
        print("Nombre:",i["nombre"])
        print("Precio:",i["precio"])
        print("Cantidad:",i["cantidad"])
elif(opc==5):
    #se despide al usuarioy se le agradece por utilizar el programa
    print("Muchas gracias por usar nuestro programa. Vuelve pronto! :D")   

#Desarrollado por Alejandra Machuca grupo T2     