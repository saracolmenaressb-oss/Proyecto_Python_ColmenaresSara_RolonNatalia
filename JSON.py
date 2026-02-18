def guardar(datos):
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def cargar():
    try:
        with open('datos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None
