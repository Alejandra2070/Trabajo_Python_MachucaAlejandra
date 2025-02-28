import json

def abrirArchivo():
    miJson=[]
    with open("menu.json", encoding="utf-8") as openfile:
        miJson=json.load(openfile)
        return miJson
    
archivo=abrirArchivo()

def guardarArchivo(miData):
    with open("menu.json","w") as outfile:
        json.dump(miData,outfile)
###########################################################
def abrirArchivo2():
    miJson2=[]
    with open("pagos.json", encoding="utf-8") as openfile:
        miJson2=json.load(openfile)
        return miJson2
    
archivo2=abrirArchivo2()

def guardarArchivo2(miData):
    with open("pagos.json","w") as outfile:
        json.dump(miData,outfile)
###########################################################
def abrirArchivo3():
    miJson3=[]
    with open("pedidos.json", encoding="utf-8") as openfile:
        miJson3=json.load(openfile)
        return miJson3
    
archivo3=abrirArchivo3()

def guardarArchivo3(miData):
    with open("pedidos.json","w") as outfile:
        json.dump(miData,outfile)
############################################################

booleano = True
print("---------BIENVENIDOSSSS---------")
print("--------------------------------")
print("--------------MENÚ--------------")
print("""
    1. Crear pedidos
    2. Salir
      """)
opc=int(input("Elige una de las opciones de nuestro menú: "))
if opc==1:
    while booleano==True:
        print("""
            1. Añadir plato de entrada
            2. Añadir plato fuerte
            3. Añadir bebidas
            """)
        x=int(input("Qué deseas agregar al pedido? Elige una opción: "))
        if (x==1):
            miInfo=abrirArchivo()
            cont=0
            for i in miInfo[0]["Entrada"]:
                cont=cont+1
                print("-----------------------")
                print( cont,":","ID: ",i["id"])
                print("Nombre: ",i["nombre"])
                print("Precio: ",i["precio"])

                int(input("Cuál plato quieres ordenar?: "))
                if (cont==1):
                    nombre1=input("Ingresa tu nombre: ")
                    nombre2=input("Ingresa el nombre del plato que elegiste: ")
                    precio= int(input("Ingresa el precio del plato: "))
                    estado= input("Ingresa el estado del pedido (Creado/Preparación/Servido/Pagado): ")

                    añadir= {
                        "cliente": nombre1,
                        "items":{
                            "categoria": "entrada",
                            "nombre": "nombre2",
                            "precio": "precio",
                        },
                        "estado": "estado"
                    }
                    miInfo = abrirArchivo3()
                    miInfo[0]["pedidos"].append(añadir)
                    guardarArchivo3(miInfo)
                    otro=int(input("Deseas agregar algo más? (1. Si / 2. No): "))
                    if otro==1:
                        booleano=True
                    else:
                        booleano=False
                elif (cont==2):
                    nombreA=input("Ingresa tu nombre: ")
                    nombreB=input("Ingresa el nombre del plato que elegiste: ")
                    precio2= int(input("Ingresa el precio del plato: "))
                    estado2= input("Ingresa el estado del pedido (Creado/Preparación/Servido/Pagado): ")

                    añadir2= {
                        "cliente": nombreA,
                        "items":{
                            "categoria": "entrada",
                            "nombre": "nombreB",
                            "precio": "precio2",
                        },
                        "estado": "estado2"
                    }
                    miInfo = abrirArchivo3()
                    miInfo[0]["pedidos"].append(añadir)
                    guardarArchivo3(miInfo)
                    otro=int(input("Deseas agregar algo más? (1. Si / 2. No): "))
                    if otro==1:
                        booleano=True
                    else:
                        booleano=False


