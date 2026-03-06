from validaciones import *
from gestionHerramientas import *
from usuarios import *

def login():
    while(True):
        menu_principal=validarMenu("""
        BIENVENIDO AL SISTEMA
        1. Administrador
        2. Salir
    """,1,2)
        while menu_principal==None:
            menu_principal=validarMenu("ERROR VALOR INVALIDO INGRESELO DENUEVO",1,2)
        match(menu_principal):
            case 1:
                clave=123
                ingreso=int(input("INGRESE LA CLAVE DE ADMINISTRADOR: "))
                while ingreso!=clave:
                    ingreso=int(input("CLAVE INCORRECTA, INTENTE NUEVAMENTE: "))
                print("CLAVE CORRECTA, BIENVENIDO ADMINISTRADOR")
                menu_admin()
            case 2:
                print("GRACIAS POR USAR LA APP")
            case _:         
                print("NO SE ENCUENTRA LA OPCION")
        if menu_principal==2:
            break
   

def menu_admin():
    while True:
        print("\n===== MENÚ ADMIN =====")
        print("1. Herramientas")
        print("2. Usuarios")
        print("3. Salir")
        
        op = input("Opción: ")
        
        if op == "1":
            menu_herramientas()
        elif op == "2":
            menu_usuarios()
        elif op == "3":
            break


def menu_herramientas():
    while True:
        print("\n--- HERRAMIENTAS ---")
        print("1. Agregar")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        
        op = input("Opción: ")
        
        if op == "1":
            agregar_herramienta()
        elif op == "2":
            listar_herramientas()
        elif op == "3":
            actualizar_herramientas()
        elif op == "4":
            eliminar_herramienta()
        elif op == "5":
            return
    

def menu_usuarios():
    while True:
        print("\n--- USUARIOS ---")
        print("1. Agregar")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        
        op = input("Opción: ")
        
        if op == "1":
            crear_usuario()
        elif op == "2":
            listar_usuario()
        elif op == "3":
            actualizar_usuario()
        elif op == "4":
            eliminar_usuario()
        elif op == "5":
            return


import logs

logs.ARCHIVO()

while True:
    print("\n1. Usuarios")
    print("2. Herramientas")
    print("3. Ver historial")
    print("4. Salir")
    
    op = input("Opción: ")
    
    if op == "1":
        pass
    elif op == "2":
        pass
    elif op == "3":
        logs.ARCHIVO()
    elif op == "4":
        break

