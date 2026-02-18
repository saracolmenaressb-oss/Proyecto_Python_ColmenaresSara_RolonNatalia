def ver_notas(camper):
    if camper.get("nota")is None:
        print("Aun no se ha registrado notas")
    else:
        print(f'Tu nota es: {camper["Nota"]}')

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
