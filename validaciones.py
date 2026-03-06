def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None

def nombre_valido(nombre):
    if nombre.strip().lower()=="":
        print("Nombre vacio")
        return False
    return True

def validarDecimalMayor0(mesanje, minimo):
    try:
        dato=float(input(mesanje))
        if dato<=minimo:
            return None
        else:
            return dato
    except:
        return None
    
def validarEnteroMayor0(mesanje, minimo):
    try:
        dato=int(input(mesanje))
        if dato<=minimo:
            return None
        else:
            return dato
    except:
        return None