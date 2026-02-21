from coordinador import gestionar_riesgo
from coordinador import asignar_trainer
from coordinador import matricular_camper()

from camper import calcular_riesgo()
from camper import editar_camper()
from camper import registrar_nota_inicial()
from camper import ver_trainer()
from camper import ver_notas()
from camper import ver_horario()
from reportes import menu_reportes()
from trainer import registrar_nota()
from trainer import ver_horario_trainer()
import data

import random
from datetime import datetime, timedelta
import Json
    camper = {
        "nombre": nombre,
        "id": id_estudiante,
        "direccion": direccion,
        "acudiente": acudiente,
        "estado": None 
        "Trainer": None
    }
    with open("campers.Json", "w") as f:
        Json.dump(numeros, f)
        estudiantes.append(nuevo_estudiante)

def menu_principal():
    print("=====================")
    print("BIENVENIDO A PLATAFORMA CAMPUSLANDS")
    print("=====================")
    print("--Menu principal--")
    print("1. Registrarme")
    print("2. Iniciar secion")
    print("3. salir")
    print(':')
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
    iniciar_sesion(trainers_data)
    print('1. Ver horario')
    print('2. Registrar notas')
    print('3. Volver al menu principal')
    opcion_trainer=int(input('Elije'))
    if opcion_trainer== '1':
        ver_horario_trainer(trainers_data)
    elif opcion_trainer=='2':
        registrar_nota(trainer, camper_id, nota)
    elif opcion_trainer=='3':
        menu_principal()
def menu_camper():
    print('Seleccione una opcion: ')
    print('1. Ver notas')
    print('2. Ver Trainer')
    print('3. Volver al menu prinipal')
    opcion_camper=int(input(':'))
    if opcion_camper = '1':
        ver_notas(camper)
    elif:
        ver_trainer(camper)
    elif:
        menu_principal()


    menu_principal()
    opcionUsuario=int(input(':'))
    if opcionUsuario=='1':
        print("Rellene la siguiente informacion")
        validar_nombre()
        Apellido=input("Digite su apellido: ")
        validar_id()
        Direccion= input("Digite su direccion: ")
        Acudiente= input("Digite su acudiente: ")
        validar_telefono()
    
    elif opcionEstado == '2':
        print("Seleccione su rol")
        print("1. camper")
        print("2. Coordinadora")
        print("3. Trainer")
        opcion_rol=int(input(':'))
        if(opcion_rol==1):
            validar_nombre()
            validar_id()       
            usuario=input("Digite su usuario: ")
            menu_camper()
        elif opcion_rol=='2':
            menu_trainer()
        elif opcion_rol=='3':
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
