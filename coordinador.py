def editar_camper(lista_campers):
    print("-- EDITAR INFORMACIÓN DE CAMPER --")
    camper_id = input("Ingrese el ID del camper a editar: ")

    camper_editar = None
    
    for c in lista_campers:
        if c["ID"] == camper_id:
            camper_editar = c
            break

    if camper_editar:
        print(f"Editando a: {camper_editar['Nombre']} {camper_editar['Apellido']}")
    else:
        print("No se encontró ningún camper con ese ID.")
    while True:
        print("¿Qué dato desea modificar?")
        print("1. Nombres")
        print("2. Apellidos")
        print("3. Dirección")
        print("4. Teléfono")
        print("5. Acudiente")
        print("6. Salir")

        opcionUsuario = input("Seleccione el número del dato a modificar: ")

        if opcionUsuario == "1":
            nuevo_nombre = input(f"Nombre actual ({camper_editar['Nombre']}): ")
            camper_editar["Nombre"] = nuevo_nombre
            print("Nombre actualizado")
        elif opcionUsuario == "2":
            nuevo_apellido = input(f"Apellido actual ({camper_editar['Apellido']}): ")
            camper_editar["Apellido"] = nuevo_apellido
            print("Apellido actualizado")
        elif opcionUsuario == "3":
            nueva_direc = input(f"Dirección actual ({camper_editar.get('Dirección', 'No registrada')}): ")
            camper_editar["Dirección"] = nueva_direc
            print("Dirección actualizada")
        elif opcionUsuario == "4":
            nuevo_tel = input(f"Teléfono actual ({camper_editar.get('Teléfono', 'No registrado')}): ")
            camper_editar["Telefono"] = nuevo_tel
            print("Teléfono actualizado")
        elif opcionUsuario == "5":
            nuevo_acu = input(f"Acudiente actual ({camper_editar.get('Acudiente', 'No registrado')}): ")
            camper_editar["Acudiente"] = nuevo_acu
            print("Acudiente actualizado")
        elif opcionUsuario == "6":
            print("Finalizando edición...")
            break
        else:
            print("Opción no válida")
def calcular_riesgo(puntos):
    if puntos >= 80: return "Bajo"
    if 40 <= puntos < 80: return "Medio"
    return "Alto"
for i in range(1, 101):
    if grupos:
        grupo_asignado = random.choice(grupos)
    else:
        print("No se puede seleccionar porque la lista de grupos está vacía.")
        break

    puntos_rendimiento = random.randint(0, 100)

    fecha_inicio = datetime(2026, 1, 15)
    fecha_fin = fecha_inicio + timedelta(days=30*10) #10 meses aprox

    print(f"{'ID':<10} | {'Camper':<20} | {'Trainer':<15} | {'Grupo':<5} | {'Riesgo':<8}")
    print("-" * 75)
for c in lista_campers[:10]:
    nombre_completo = f"{c['Nombre']} {c['Apellido']}"
    print(f"{c['ID']:<10} | {nombre_completo:<20} | {c['Trainer']:<15} | {c['Grupo']:<5} | {c['Riesgo']:<8}")   
    print(f"/nTotal de Campers creados: {len(lista_campers)}")

def registrar_nota_inicial(lista_campers):
    print("-- Registrar Nota de Admisión --")
    camper_id = input("Ingrese el ID del Camper a evaluar: ")

    camper_encontrado = None

    for c in lista_campers:
        if c["ID"] == camper_id:
            camper_encontrado = c
            break

    if camper_encontrado is None:
        print("No se encontró ningún camper con ese ID.")
        return

    if camper_encontrado["Estado"] != "Inscrito":
        print(f"El camper {camper_encontrado['Nombre']} tiene estado '{camper_encontrado['Estado']}'. Solo se evalúan 'Inscritos'.")
        return

    try:
        teorica = float(input("Ingrese nota Teórica (0-100): "))
        practica = float(input("Ingrese nota Práctica (0-100): "))
        promedio = (teorica + practica) / 2

        print(f"Promedio obtenido: {promedio}")

        if promedio >= 60:
            camper_encontrado["Estado"] = "Aprobado"
            print(f"¡Felicidades! {camper_encontrado['Nombre']} ha sido APROBADO.")
        else:
            print(f"Lo sentimos. {camper_encontrado['Nombre']} no superó la prueba.")

    except ValueError:
        print("Error: Debes ingresar números válidos.")
def gestionar_riesgo(lista_campers):
    print("-- GESTIÓN DE RIESGO Y LLAMADOS DE ATENCIÓN --")
    camper_id = input("Ingrese el ID del camper: ")
    encontrado = False
    for camper in lista_campers:
        if camper['ID'] == camper_id:
            encontrado = True
            print(f"Camper: {camper['Nombre']} {camper['Apellido']}")
            print(f"Estado actual: {camper['Estado']}")
            print(f"Riesgo actual: {camper['Riesgo']}")

            print("Opciones:")
            print("1. Modificar nivel de riesgo manualmente")
            print("2. Volver")

            opcionUsuario = input("Seleccione: ")
            if opcionUsuario == "1":
                print("Seleccione el nuevo nivel de riesgo:")
                print("1. Bajo (>= 80 puntos)")
                print("2. Medio (40 - 79 puntos)")
                print("3. Alto (< 40 puntos) -> Genera llamado de atención")

                nuevo_riesgo = input("Opción: ")
                if nuevo_riesgo == "1":
                    camper["Riesgo"] = "Bajo"
                    print("Riesgo actualizado a Bajo")
                elif nuevo_riesgo == "2":
                    camper["Riesgo"] = "Medio"
                    print("Riesgo actualizado a Medio")
                elif nuevo_riesgo == "3":
                    camper["Riesgo"] = "Alto"
                    print("Riesgo actualizado a Alto. Se ha generado un llamado de atención")
                else:
                    print("Opción inválida")
                    break
                if not encontrado:
                    print("Error: Camper no encontrado")
def matricular_camper(lista_campers, lista_grupos):
    print("-- Módulo de Matrículas --")
    aprobados = [c for c in lista_campers if c["Estado"] == "Aprobado"]
    if not aprobados:
        print("No hay campers con estado 'Aprobado' pendientes de matrícula.")
        return
        print("Campers disponibles para matrícula:")
    for c in aprobados:
        print(f"ID: {c['ID']} - Nombre: {c['Nombre']} {c['Apellido']}")
        id_matricular = input("Ingrese el ID del camper a matricular: ")
        camper_seleccionado = None
    for c in lista_campers:
        if c["ID"] == id_matricular and c["Estado"] == "Aprobado":
            camper_seleccionado = c
            break
    if camper_seleccionado:
        print("Seleccione un grupo disponible:")
                #Poner grupos disponibles
    for i, g in enumerate(lista_grupos):
        print(f"{i+1}. Grupo {g['id_grupo']} ({g['ruta']}) - Trainer: {g['trainer']}")
    try:
        opcion = int(input("Ingrese el número del grupo: ")) - 1
        if 0 <= opcion < len(lista_grupos):
            grupo_asignado = lista_grupos[opcion]
            camper_seleccionado["Grupo"] = grupo_asignado["id_grupo"]
            camper_seleccionado["Trainer"] = grupo_asignado["trainer"]
            camper_seleccionado["Ruta"] = grupo_asignado["ruta"]
            camper_seleccionado["Estado"] = "Cursando"
            camper_seleccionado["Fecha_Inicio"] = "15/01/2026"
            camper_seleccionado["Fecha_Fin"] = "15/11/2026"
            print(f"¡Éxito! {camper_seleccionado['Nombre']} matriculado en {grupo_asignado['id_grupo']}.")
        else:
            print("Opción de grupo inválida.")
    except ValueError:
        print("Error: Ingrese un número válido.")
