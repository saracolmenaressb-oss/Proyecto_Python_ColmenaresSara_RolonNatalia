def registrar_nota(trainer, camper_id, nota):
    estudiantes =trainer.get('estudiantes_asignados',[])
    for camper in estudiantes:
        if camper['ID']==camper_id:
            camper['nota']= nota
            print("Nota registrada correctamente")
            return
    print("Error: este estudiante no le ha sido asignado")

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
