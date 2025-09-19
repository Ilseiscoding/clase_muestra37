def capturar_datos_alumnos():
    alumnos = []

    try:
        num_alumnos = int(input("¿Cuántos alumnos deseas capturar? "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    for i in range(num_alumnos):
        print(f"\n--- Alumno {i + 1} ---")
        nombre = input("Nombre del alumno: ")

        materias = []
        for j in range(3):
            materia = input(f"Nombre de la materia {j + 1}: ")
            
            while True:
                calificacion_str = input(f"Calificación para {materia}: ")
                try:
                    calificacion = float(calificacion_str)
                    break
                except ValueError:
                    print("❌ Error: Debes ingresar una calificación válida (número).")

            materias.append({
                "materia": materia,
                "calificacion": calificacion
            })

        alumnos.append({
            "nombre": nombre,
            "materias": materias
        })

    print("\n✅ Datos capturados correctamente:")
    for alumno in alumnos:
        print(f"\nAlumno: {alumno['nombre']}")
        for m in alumno["materias"]:
            print(f" - {m['materia']}: {m['calificacion']}")

# Ejecutar función principal
capturar_datos_alumnos()
