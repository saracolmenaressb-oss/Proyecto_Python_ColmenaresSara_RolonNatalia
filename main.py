import random
from datetime import datetime, timedelta

def registrar_nota_inicial(lista_campers):
    print("-- Registrar Nota de Admisión --")
    camper_id = input("Ingrese el ID del Camper a evaluar: ")
    encontrado = False
    for camper in lista_campers:
        if camper["ID"] == camper_id:
            encontrado = True
            if camper["Estado"] != "Inscrito":
                print(f"El camper {camper['Nombre']} tiene estado '{camper['Estado']}'. Solo se evalúan 'Inscritos'.")
                return
            try:
                teorica = float(input("Ingrese nota Teórica (0-100): "))
                practica = float(input("Ingrese nota Práctica (0-100):"))
                promedio = (teorica + practica) / 2
                print(f"Promedio obtenido: {promedio}")
                if promedio >= 60:
                    camper["Estado"] = "Aprobado"
                    print(f"¡Felicidades! {camper['Nombre']} ha sido APROBADO.")
                else:
                    print(f"Lo sentimos. {camper['Nombre']} no superó la prueba.")
            except ValueError:
                print("Error: Debes ingresar números válidos.")
                break
            if not encontrado:
                print("No se encontró ningún camper con ese ID.")

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
                aprobados = [c for c in lista_campers if camper["Estado"] == "Aprobado"]
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
                else:
                    print("ID incorrecto o el camper no está en estado 'Aprobado'.")

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
                        camper_editar["Dirección"] = nuevo_tel
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
            else:
                print("El ID ingresado no existe en el sistema")

def menu_reportes(lista_campers, lista_trainers):
            while True:
                print("-- MENÚ DE REPORTES Y CONSULTAS")
                print("1. Listar campers 'Inscritos'.")
                print("2. Listar campers 'Aprobados' (Prueba inicial).")
                print("3. Listar trainers trabajando.")
                print("4. Listar campers con riesgo 'Bajo' (Rendimiento).")
                print("5. Listar campers con Ruta de entrenamiento.")
                print("6. Volver al menú principal.")
                opcionUsuario = input("Seleccione reporte: ")
                if opcionUsuario == "1":
                    print("-- CAMPERS INSCRITOS --")
                    inscritos = [c for c in lista_campers if c["Estado"] == "Inscrito"]
                    for c in inscritos: print(f"{c['ID']} | {c['Nombre']} {c['Apellido']}")
                elif opcionUsuario == "2":
                    print("-- CAMPERS APROBADOS (Prueba inicial) --")
                    aprobados = [c for c in lista_campers if c["Estado"] == "Aprobado"]
                    for c in aprobados: print(f"{c['ID']} | {c['Nombre']} | {c['Apellido']}")
                elif opcionUsuario == "3":
                    print("-- LISTA DE TRAINERS --")
                    for t in lista_trainers:
                        print(f"Trainer: {t['nombre']} {t['apellido']} - Rutas: {t['rutas']}")
                elif opcionUsuario == "4":
                    print("-- CAMPERS EN RIESGO ALTO (Rendimiento bajo) --")
                    riesgo_alto = [c for c in lista_campers if c["Riesgo"] == "Alto"]
                    for c in riesgo_alto:
                        print(f"{c['ID']} | {c['Nombre']} - Grupo: {c['Grupo']} - Riesgo: Alto")
                elif opcionUsuario == "5":
                    ruta_buscar = input("Escriba la ruta a consultar: ")
                    print(f"-- CAMPERS EN RUTA {ruta_buscar}--")
                    por_ruta = [c for c in lista_campers if ruta_buscar.lower() in c.get("Ruta","").lower()]
                    for c in por_ruta:
                        print(f"{c['Nombre']} {c['Apellido']} - Trainer: {c['Trainer']}")
                elif opcionUsuario == "6":
                    break
                else:
                    print("Opción no válida")

def ver_horario_trainer(nombre_trainer, lista_trainers, lista_grupos):
    print(f"-- CONSULTA DE HORARIO: {nombre_trainer} --")
    horario_encontrado = "No registrado"
    for t in lista_trainers:
        if nombre_trainer.lower() in (t["nombre"] + " " + t["apellido"]).lower():
            horario_encontrado = t["horario"]
            break
        if horario_encontrado == "No registrado":
            print("Error: El nombre del trainer no coincide con nuestra base de datos.")
            return
        print(f"Jornada laboral: {horario_encontrado}")
        print("-" * 30)
        print("Grupos asignados:")

        tiene_grupos = False
        for g in lista_grupos:
            if nombre_trainer.lower() in g["trainer"].lower():
                print(f"Grupo: {g['id_grupo']} | Ruta: {g['ruta']}")
                tiene_grupos = True
        if not tiene_grupos:
            print("Aún no tienes grupos asignados para esta jornada.")

def listar_Aprobados():
    nota_examen_inicial= (notaPractica + notaTeorica) / 2
    if(nota_examen_inicial >=60):
        camper['estado']='aprobado'
    else:
        camper['estado']='no aprobado'
def asignar_notas_trainer():
    ID_buscar= input('ID del camper')
    for camper in campers:
        if camper['ID']==ID_buscar:
            examen_teorico=float(input('examen'))
            examen_Practico=float(input('examen'))
            quiz=float(input('nota quiz'))
            trabajo=float(input('nota trabajo'))
def campers_cursando(campers):
    print('--lista de campers cursando--')
    campers =[
            {"nombre": nombre},
            {"usuario": usuario},
            {"ID": ID},
            {"Estado": "cursando"}
        ]
def score_camper():
    score= (examen_teorico * )

Campers = []

lista_campers = []

nombres = ["Juan","Maria","Luis","Ana","Carlos","Elena","Diego","Paula","Andrés","Lucía"]
apellidos = ["Arias","Castro","Vargas","Ríos","Duarte","Peña","López","García","Marín"]
estados = ["En proceso de ingreso","Inscrito","Aprobado","Cursando","Graduado","Expulsado","Retirado"]
salones = ["Sputnik","Apolo","Artemis"]

trainers_data = [
        {"nombre":"Pedro","apellido":"Gómez","horario":"6:00-18:00","rutas":["Java","NodeJS"]},
        {"nombre":"Cristian","apellido":"Díaz","horario":"10:00-18:00","rutas":["Java","NodeJS"]},
        {"nombre":"Kevin","apellido":"Pinzón","horario":"6:00-14:00","rutas":["Java"]},
        {"nombre":"Edwin","apellido":"Mendoza","horario":"6:00-14:00","rutas":["Java","Netcore"]},
        {"nombre":"Jholver","apellido":"Pinto","horario":"6:00-14:00","rutas":["Java","Netcore"]},
        {"nombre":"Carlos","apellido":"Rodríguez","horario":"18:00-22:00","rutas":["Netcore"]}
    ]

Coordinadores = []

grupos = []

Rutas = []

ID = []

def calcular_riesgo(puntos):
    if puntos >= 80: return "Bajo"
    if 40 <= puntos < 80: return "Medio"
    return "Alto"

for t in trainers_data:
        #Determinamoscuántos turnos de 4 horas caben en su horario
        # Para simplificar, asignaremos 2 grupos a los de jornada larga y 1 a los de jornada corta/nocturna
        num_grupos = 2 if "18:00" in t["horario"] and "6:00" in t["horario"] else 1
        for i in range(1, num_grupos + 1):
            grupos.append({
                    "id_grupo": f"{t['nombre'][0]}{i}",
                    "trainer": f"{t['nombre']} {t['apellido']}",
                    "ruta": random.choice(t["rutas"])
                })

for i in range(1, 101):
    grupo_asignado = random.choice(grupos)
    puntos_rendimiento = random.randint(0, 100)

fecha_inicio = datetime(2026, 1, 15)
fecha_fin = fecha_inicio + timedelta(days=30*10) #10 meses aprox

print(f"{'ID':<10} | {'Camper':<20} | {'Trainer':<15} | {'grupo':<5} | {'Riesgo':<8}")
print("-" * 75)
for c in lista_campers[:10]:
    nombre_completo = f"{c["Nombre"]} {c["Apellido"]}"
    print(f"{c["ID"]:<10} | {nombre_completo:<20} | {c["Trainer"]:<15} | {c["grupo"]:<5} | {c["Riesgo"]:<8}")
    
    print(f"/nTotal de Campers creados: {len(lista_campers)}")

camper = {
        "ID": f"1005{i:03d}",
        "Nombre": random.choice(nombres),
        "Apellido": random.choice(apellidos),
        "User": f"user_{i}",
        "Teléfono": f"315{random.randint(1000000, 9999999)}",
        "Dirección": f"Calle {random.randint(1, 100)} # {random.randint(1,50)}",
        "Acudiente": f"Familiar de {random.choice(nombres)}",
        "Trainer": grupo_asignado["trainer"],
        "Grupo": grupo_asignado["id_grupo"],
        "Ruta": grupo_asignado["ruta"],
        "Salon": random.choice(salones),
        "Fecha_Inicio": fecha_inicio.strftime("%d/%m/%Y"),
        "Fecha_Fin": fecha_fin.strftime("%d/%m/%Y"),
        "Estado": random.choice(estados),
        "Riesgo": calcular_riesgo(puntos_rendimiento)
    }
lista_campers.append(camper)

def menu_principal():
    print("=====================")
    print("BIENVENIDO A PLATAFORMA CAMPUSLANDS")
    print("=====================")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")

while True:
    menu_principal()
    opcionUsuario = input("Selecciona tu rol (1-3):")
    if opcionUsuario == "1":
        print("-- MENU CAMPER ---")
        #parte Sara
    elif opcionUsuario == "2":
            print("-- MENU TRAINER ---")
            trainer_nombre = input("Por favor ingresa tu nombre completo:")
            while True:
                print(f"Bienvenido(a) {trainer_nombre}")
                print("1. Ver mi horario y grupos asignados")
                print("2. Gestionar notas")##Parte Sara
                print("3. Volver al menú principal")
                opcion_trainer = input("Seleccione un opción: ")
                if opcion_trainer == "1":
                    ver_horario_trainer(trainer_nombre, trainers_data, grupos)
                elif opcion_trainer == "2":
                    ##Parte Saraaa
                elif opcion_trainer == "3":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción inválida.")
    elif opcionUsuario == "3":
        def menu_coordinador(lista_campers, rutas_existentes):
            print("-- COORDINACIÓN ACADÉMICA ---")
            print("1. Registrar nota de prueba de admisión")
            print("2. Definir estado de riesgo")
            print("3. Crear nuevas rutas de entrenamiento")
            print("4. Módulo de matrículas")
            print("5. Editar todos los datos de un camper")
            print("6. Reportes")
            print("7. Volver al menú principal")
            opcion_coordinador = input("Selecciona una opción (1, 2 o 3): ")
            if opcion_coordinador == "1":
                registrar_nota_inicial(lista_campers)
            elif opcion_coordinador == "2":
                gestionar_riesgo(lista_campers)
            elif opcion_coordinador == "3":
                print("-- CREAR NUEVA RUTA DE ENTRENAMIENTO --")
                nombre_ruta = input("Nombre de la nueva ruta: ")
                bd_principal = input("Base de datos principal: ")
                bd_alternativo = input("Base de datos alternativa: ")
                nueva_ruta = {
                    "Nombre": nombre_ruta,
                    "Módulos": ["Fundamentos de programación", "Programación Web", "Programación formal", "Bases de datos", "Backend"],
                    "BD": [bd_principal, bd_alternativo]
                }
                rutas_existentes.append(nueva_ruta)
                print(f"Ruta '{nombre_ruta}' creada existosamente en el sistema.")
            elif opcion_coordinador == "4":
                matricular_camper(lista_campers)
            elif opcion_coordinador == "5":
                editar_camper(lista_campers)
            elif opcion_coordinador == "6":
                menu_reportes(lista_campers)
            elif opcion_coordinador == "7":
                print("Volviendo al menú principal...")
                menu_principal()
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

    
