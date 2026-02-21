def validar_id():
    while True:
        id_usuario = input("ingrese su id: ").strip()

        if id_usuario.isdigit() and len(id_usuario) == 9:
            return id_usuario
        else:
            print("Error: la ID debe tener nueve numeros.")
def validar_nombre():
    while True:
        nombre = input("Ingrese u nombre: ").trip
    
    if nombre.repleace(" "," ").isalpha():
        return nombre
    else:
        print("Error: El nombre solo debe contener letras.")
def iniciar_sesion(trainers_data):
    nombre_ingresado = input("Ingrese su nombre: ")
    encontrado = False

    for profesor in lista_profesores:
        if profesor["nombre"].lower() == nombre_ingresado.lower():
            encontrado = True
            print(f"\nBienvenido/a {profesor['nombre']} ")
            menu_principal()
            break

    if not encontrado:
        print(" Profesor no registrado")
