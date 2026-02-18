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
