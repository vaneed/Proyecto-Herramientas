from gestionjson import *
from validaciones import *
from datetime import datetime

ARCHIVO_DE_HERRAMIENTAS = "herramientas.json"

def agregar_herramienta():
    herramientas = cargar(ARCHIVO_DE_HERRAMIENTAS)

    herramienta = input('DIGITE EL NOMBRE DE LA HERRAMIENTA ')
    while not nombre_valido(herramienta):
        herramienta = input('ERROR DIGITE UN NOMBRE VALIDO ')

    Tipo_Herramienta=validarMenu("""
                               Ingrese la categoria de la herramienta:
                                1=Mecanica
                                2=Agricultura
                            """,1, 2)
    while(Tipo_Herramienta==None):
            Tipo_Herramienta=validarMenu("Porfavor ingrese una opcion dentro de los parametros: ",1, 2)
    if Tipo_Herramienta==1:
        Tipo_Herramienta="Mecanica"
    elif Tipo_Herramienta==2:
        Tipo_Herramienta="Agricultura"

    Estado=validarMenu("""
                               Ingrese el estado de la herramienta:
                                1. ACTIVA 
                                2. REPARACION
                                3. FUERA DE SERVICIO
                            """,1, 3)
    while(Estado==None):
                Estado=validarMenu("Porfavor ingrese una opcion dentro de los parametros: ",1 ,3)
    if Estado==1:
                Estado="ACTIVA"
    elif Estado==2:
                Estado="REPARACION"
    elif Estado==3:
                Estado="FUERA DE SERVICIO"
  
    Stock=validarEnteroMayor0("Ingrese la cantidad de herramientas disponibles: ",0)
    while (Stock==None):
        Stock=validarEntero("Error ingrese un numero entero postivo, cantidad no vailda: ")

    Precio=validarDecimalMayor0("Escriba el precio unitario de la herramienta: ",0)
    while (Precio==None):
         Precio=validarEntero("Error, Ingrese un numero postivo")
    
    agregar_herramienta = {
        "id": generar_id(herramientas),
        "NOMBRE": herramienta,
        "TIPO DE HERRAMIENTA": Tipo_Herramienta,
        "ESTADO": Estado,
        "CANTIDAD": Stock,
        "PRECIO": Precio
    }
    
    herramientas.append(agregar_herramienta)
    guardar(ARCHIVO_DE_HERRAMIENTAS, herramientas)
    print('HERRAMIENTA AGREGADA!')

def listar_herramientas():
    herramientas = cargar(ARCHIVO_DE_HERRAMIENTAS)
    
    if not herramientas:
        print("No hay herramientas")
        return
    
    print("\n--- LISTA DE HERRAMIENTAS ---")
    for elementos in herramientas:
        print(f"ID: {elementos['id']} | {elementos['NOMBRE']}")
        print(f"   Cant: {elementos['CANTIDAD']} | Estado: {elementos['ESTADO']} | ${elementos['PRECIO']}")

def actualizar_herramientas():
    herramientas = cargar(ARCHIVO_DE_HERRAMIENTAS)
    listar_herramientas()
    id_h=validarEntero("Escoja el id a actualizar: ")
    while(id_h==None):
        id_h=validarEntero("Error, Escoja el id a actualizar: ")
    
    for elemento in herramientas:
            if id_h==elemento["id"]:
                while(True):
                    Herramienta_Actualizada = validarMenu("""
                               Ingrese el dato que desea actualizar:
                                1. Nombre
                                2. Tipo de herramienta
                                3. Estado
                                4. Cantidad
                                5. Precio
                                6. Volver
                            """,1, 6)
                    while Herramienta_Actualizada==None:
                        Herramienta_Actualizada=validarMenu("Error, Escoja una opcion dentro de los parametros",1,6)
                    match(Herramienta_Actualizada):
                        case 1:
                            NombreHerramienta_Actualizado=input('Ingrese el nuevo nombre de la herramienta: ')
                            while not nombre_valido(NombreHerramienta_Actualizado):
                                NombreHerramienta_Actualizado=input('Ingrese un nombre valido que no se repita de la herramienta: ')
                            elemento["NOMBRE"]=NombreHerramienta_Actualizado
                            guardar(ARCHIVO_DE_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 2:
                            TipoHerramienta_Actualizado = validarMenu("""
                               Ingrese la categoria de la herramienta:
                                1=MECANICA
                                2=AGRICULTURA
                            """,1,2)
                            while(TipoHerramienta_Actualizado)==None:
                            #LO PONEMOS DESPUES DEL VALIDADOR POR QUE SI NO SE VA A LEER LO QUE PONEMOS
                                TipoHerramienta_Actualizado=validarMenu('Error, Ingrese la nueva categoria de la herramienta dentro de los parametros establecidos: ',1,2)
                            if TipoHerramienta_Actualizado==1:
                                TipoHerramienta_Actualizado="MECANICA"
                            elif TipoHerramienta_Actualizado==2:
                                TipoHerramienta_Actualizado="AGRICULTURA"
                            elemento["TIPO DE HERRAMIENTA"]=TipoHerramienta_Actualizado
                            guardar(ARCHIVO_DE_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 3:
                            EstadoActualizado = validarMenu("""
                               Ingrese el nuevo estado de la herramienta:
                                1. ACTIVA
                                2. REPARACION
                                3. FUERA DE SERVICIO
                            """,1, 3)
                            while(EstadoActualizado)==None:
                                EstadoActualizado=validarMenu('Error, ingrese el nuevo estado de la herramienta: ',1,3)
                            if EstadoActualizado==1:
                                EstadoActualizado="ACTIVA"
                            elif EstadoActualizado==2:
                                EstadoActualizado="REPARACION"
                            elif EstadoActualizado==3:
                                EstadoActualizado="FUERA DE SERVICIO"
                            elemento["ESTADO"]=EstadoActualizado
                            guardar(ARCHIVO_DE_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 4:
                            StockActualizado=validarEnteroMayor0('Ingrese el nuevo stock a sumar de la herramienta: ',0)
                            while (StockActualizado)==None:
                                StockActualizado=validarEnteroMayor0('Error ingrese solo numeros enteros positivos, Ingrese el nuevo stock a sumar de la herramienta: ',0)
                            elemento["CANTIDAD"]+=StockActualizado
                            guardar(ARCHIVO_DE_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 5:
                            valorEstimado_Act=validarDecimalMayor0('Ingrese el nuevo precio unitario de la herramienta: ',0)
                            while (valorEstimado_Act)==None:
                                 valorEstimado_Act=validarDecimalMayor0('Error ingrese solo numeros postivos: ',0)
                            elemento["PRECIO"]=valorEstimado_Act
                            guardar(ARCHIVO_DE_HERRAMIENTAS,herramientas)
                            print('Herramienta actualizada!')
                            return
                        case 6:
                              return
    print("La herramienta no existe. \n")
        
            
           

def eliminar_herramienta():
    contador_aux=0
    herramientas = cargar(ARCHIVO_DE_HERRAMIENTAS)
    listar_herramientas()
    
    id_h = validarEntero("ID a eliminar: ")
    if id_h == None:
        return
    while(id_h==None):
        id_h=validarEntero("Error, Escoja el id a eliminar")

    for elemento in herramientas:
        if id_h==elemento["id"]:
            herramientas.pop(contador_aux)
            guardar(ARCHIVO_DE_HERRAMIENTAS,herramientas)
            print('Herramienta eliminada!')
            return
        contador_aux+=1
    print("La herramienta no existe. \n")


import logs

def crear_herramienta():
    print("\n----- CREAR HERRAMIENTA -----")
    usuario = input("Tu ID: ")
    
    if usuario != "admin":
        print("No tienes permisos")
        logs.ARCHIVO(usuario, "Crear herramienta", "Usuario sin permisos")
        return
    
    print("Herramienta creada")
