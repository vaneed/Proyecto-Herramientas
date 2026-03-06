import json
from datetime import datetime

ARCHIVO = 'logs.json'

def iniciar():
    """Crea el archivo si no existe"""
    try:
        with open(ARCHIVO, 'r') as f:
            pass
    except:
        with open(ARCHIVO, 'w') as f:
            json.dump({"intentos": []}, f)

def registrar(usuario, operacion, error):
    """Guarda un intento inválido"""
    with open(ARCHIVO, 'r') as f:
        datos = json.load(f)
    
    nuevo = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario,
        "operacion": operacion,
        "error": error
    }
    datos["intentos"].append(nuevo)
    
    with open(ARCHIVO, 'w') as f:
        json.dump(datos, f, indent=2)
    
    print(f"\n Intento inválido registrado: {error}")

def ver_ultimos():
    """Muestra los últimos intentos"""
    try:
        with open(ARCHIVO, 'r') as f:
            datos = json.load(f)
        
        print("\n=== ÚLTIMOS INTENTOS INVÁLIDOS ===")
        for intento in datos["intentos"][-5:]:
            print(f"{intento['fecha']} - {intento['usuario']} - {intento['operacion']} - {intento['error']}")
    except:
        print("No hay registros aún")