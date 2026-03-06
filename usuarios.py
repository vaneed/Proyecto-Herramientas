from gestionjson import *
from gestionHerramientas import *
from validaciones import *


ARCHIVO_USUARIO = "Usuario.json"

def crear_usuario():
    usuarios = cargar(ARCHIVO_USUARIO)

    Nombres = input('Ingrese el nombre de el usuario: ')
    while not nombre_valido(Nombres) or existe_nombre(Nombres, usuarios):
        Nombres = input('Ingrese un nombre de usuario válido: ')
    
    Apellido = input('Ingrese el apellido de el usuario: ')
    while not nombre_valido(Apellido):
        Apellido = input('Ingrese un nombre de usuario válido: ')

    Celulares = validarEnteroMayor0('Ingrese el telefono de el usuario: ',0)
    while(Celulares==None):
        Celulares=validarEnteroMayor0("Error no ingrese numeros negativos ni simbolos, Ingrese el nuevo numero de tefono: ",0)
    

    Direccion = input('Ingrese la direccion de el usuario: ')
    

    nuevo_usuario = {
        "id": generar_id(usuarios),
        "Nombres": Nombres,
        "Apellido": Apellido,
        "Telefono": Celulares,
        "Direccion": Direccion,
    }

    
    usuarios.append(nuevo_usuario)
    guardar(ARCHIVO_USUARIO, usuarios)
    print('USUARIO AGREGADO!')

def existe_nombre(nombreU, usuarios):
    for elemento in usuarios:
        if elemento["Nombres"].lower() == nombreU.lower():
            return True
    return False

def listar_usuario():
    usuarios = cargar(ARCHIVO_USUARIO)

    if not usuarios:
        print ("No hay usuarios\n")
        return

    for elemento in usuarios:
        print(f'ID: {elemento["id"]}\n Nombre: {elemento["Nombres"]}\n Apellido: {elemento["Apellido"]}\n Telefono: {elemento["Telefono"]}\n Direccion: {elemento["Direccion"]}\n')
    print()

def listar_nombres():
    usuarios = cargar(ARCHIVO_USUARIO)

    if not usuarios:
        print ("No hay nombres\n")
        return

    for elemento in usuarios:
        print(f'ID: {elemento["id"]}\n Nombre: {elemento["Nombre usuario"]}\n Apellido: {elemento["Apellido"]}\n')
    print()


def actualizar_usuario():
    usuarios = cargar(ARCHIVO_USUARIO)
    listar_usuario()
    id_usuarios=validarEntero("Escoja el id a actualizar: ")
    while(id_usuarios==None):
        id_usuarios=validarEntero("Error, Escoja el id a actualizar: ")
        

    for elemento in usuarios:
            if id_usuarios==elemento["id"]:
                while(True):
                    ActualizarUsuario = validarMenu("""
                               Ingrese el parametro que requiere actualizar:
                                1. Nombre
                                2. Apellido
                                3. Telefono
                                4. Direccion
                            """,1, 4)
                    
                    match(ActualizarUsuario):
                        case 1:
                            NuevoNombre=input('Ingrese el nuevo nombre de el usuario: ')
                            while not nombre_valido(NuevoNombre) or existe_nombre(NuevoNombre, usuarios):
                                NuevoNombre = input('Ingrese un nombre de usuario válido, no repetido: ')
                            elemento["Nombres"]=NuevoNombre
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
                        case 2:
                            NuevoApellido=input('Ingrese el nuevo apellido de el usuario: ')
                            elemento["Apellido"]=NuevoApellido
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
                        case 3:
                            Nueov_Tel=validarEnteroMayor0('Ingrese el nuevo telefono de el usuario: ',0)
                            while (Nueov_Tel)==None:
                                Nueov_Tel=validarEnteroMayor0("Error no ingrese numeros negativos ni simbolos, Ingrese el nuevo numero de tefono: ",0)
                            elemento["Telefono"]=Nueov_Tel
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
                        case 4:
                            Nueva_Direccion=input('Ingrese la nueva direccion de el usuario: ')
                            elemento["Direccion"]=Nueva_Direccion
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
    print("El usuario no existe. \n")


def eliminar_usuario():
    contador_aux=0
    usuarios=cargar(ARCHIVO_USUARIO)
    listar_usuario()
    id_usuarios=validarEntero("Escoja el id a eliminar")
    while(id_usuarios==None):
        id_usuarios=validarEntero("Error, Escoja el id a eliminar")
    for elemento in usuarios:
        if id_usuarios==elemento["id"]:
            usuarios.pop(contador_aux)
            guardar(ARCHIVO_USUARIO,usuarios)
            print('Usuario eliminado!')
            return
        contador_aux+=1
    print("El usuario no existe. \n")


import logs

def crear_usuario():
    print("\n----- CREAR USUARIO -----")
    id_usuario = input("ID: ")
    
    if id_usuario == "admin":
        print("ID ya existe")
        logs.ARCHIVO("Desconocido", "Crear usuario", f"ID {id_usuario} ya existe")
        return
    
    print("Usuario creado")
