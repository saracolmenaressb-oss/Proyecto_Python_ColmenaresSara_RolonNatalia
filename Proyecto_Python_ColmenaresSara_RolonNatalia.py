from coordinador import gestionar_riesgo
from coordinador import asignar_trainer
from coordinador import matricular_camper(lista_campers, lista_grupos)

from camper import calcular_riesgo(puntos)
from camper import editar_camper(lista_campers)
from camper import registrar_nota_inicial(lista_campers)
from camper import ver_trainer(camper)
from camper import ver_notas(camper)
from camper import ver_horario(camper)
from reportes import menu_reportes(lista_campers, lista_trainers)
from trainer import registrar_nota(trainer, camper_id, nota)
from trainer import ver_horario_trainer(nombre_trainer, lista_trainers, lista_grupos)
import data

import random
from datetime import datetime, timedelta

camper = []
lista_campers = []
lista_trainers = []
trainer = []
camper_id = []
nombre_trainer = []
lista_grupos = []
nota = []
puntos = []

def menu_principal():
    print("=====================")
    print("BIENVENIDO A PLATAFORMA CAMPUSLANDS")
    print("=====================")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")
def menu_coordinador(lista_campers, rutas_existentes):
    print("-- COORDINACIÓN ACADÉMICA ---")
    print("1. Registrar nota de prueba de admisión")
    print("2. Definir estado de riesgo")
    print("3. Crear nuevas rutas de entrenamiento")
    print("4. Módulo de matrículas")
    print("5. Editar todos los datos de un camper")
    print('6. Asignar trainer')
    print("7. Reportes")
    print("8. Volver al menú principal")
def menu_trainer():
        print('1. Ver estudiantes')
        print('2. Registrar notas')
        print('3. Volver al menu principal')

while True:
    menu_principal()
    opcionUsuario = input("Selecciona tu rol (1-3):")
    if opcionUsuario == "1":
        print("-- MENU CAMPER ---")
        print("Seleccione su estado")
        print("1. cursando")
        print("2. en proceso de ingreso")
        print("3. :")
        opcionEstado=int(input(":"))
        if opcionEstado==1:
            nombre= input("Digite su nombre")
            usuario=input("Digite su usuario")
            ID= input("Digite su ID")
            camper_cursando={
            "nombre" : nombre,
            "usuario": usuario,
            "ID": ID,
            "Estado": "cursando"
            }
            lista_campers.append(camper_cursando)
            print("1. Ver notas")
            print("2. Ver trainer asignado")
            print("3. Ver horario asignado")
            print("4. Volver al menu principal")
            opcion_camper=int(input("seleccione una opcion"))
            if(opcion_camper==1):
                ver_notas(camper_cursando)
            elif(opcion_camper==2):
                ver_trainer(camper_cursando)
            elif(opcion_camper==3):
                ver_horario_trainer(camper_cursando.get("Trainer"), trainers_data, grupos)
        elif opcionEstado==2:
            print("Ingrese sus datos personales: ")
            nombre= input("Digite su nombre: ")
            print({nombre})
            ID= input("Digite su ID: ")
            print({ID})
            Direccion= input("Ingrese su direccion: ")
            Acudiente= input("¿Cual es su acudiente?: ")
            print("Seleccione en que horario quiere aplicar: ")
            print("1. Jornada de la mañana(6:00AM-2:00PM)")
            print("2. Jornada de la tarde(2:00PM-7:00)")
            print("3. Jornada de la noche(6:00PM-10:00PM)")
            print(":")
            opcionJornada=int(input(":"))
            camper_proceso_ingreso = {
                "nombre": nombre,
                "ID": ID,
                "direccion": Direccion,
                "acudiente": Acudiente,
                "Jornada": opcionJornada
            }
            nuevo_Camper.append(camper_proceso_ingreso)
            print("Se le notificara cuando deba presentar la prueba")
            menu_principal()
    elif opcionUsuario == '2':
        menu_trainer()
        opcion_trainer=int(input('Elije'))
        if(opcion_trainer==1):
           print("Función de registrar nota aún no implementada.")
        elif(opcion_trainer==2):
            ver_horario_trainer(nombre_trainer, lista_trainers, lista_grupos)
        elif(opcion_trainer==3):
            menu_principal()
    elif opcionUsuario == "3":
        menu_coordinador(lista_campers, rutas_existentes)
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
            matricular_camper(lista_campers, grupos)
        elif opcion_coordinador == "5":
            editar_camper(lista_campers)
        elif opcion_coordinador == "6":
            menu_reportes(lista_campers)
        elif opcion_coordinador == "7":
            print("Volviendo al menú principal...")
            menu_principal()
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
