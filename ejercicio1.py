# Inicialización de contadores
especialistas_senior = 0
residentes_junior = 0

# Validación de la cantidad de médicos a resgistrar
while True:
    try:
        cantidad_medicos = int(input("Ingresa la cantidad de médicos a resgistrar: "))
        if cantidad_medicos > 0:
            break
        else:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar")
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar")

# Bucle para el registro por médico
for i in range(cantidad_medicos):
    print(f"\n--- Registro del Médico {i+1} ---")

    while True:
        nombre = input("Ingresa Nombre Profesional (mín. 6 caracterees, sin espacios): ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("Nombre inválido. Debe tener al menos 6 caraceteres y no contener espacios")

    # Validación de la experiencia clínica
    while True:
        try:
            experiencia = int(input(f"Ingresa años de experiencia de {nombre}: "))
            if experiencia >= 0:
                break
            else:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia")
        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia")
    
    # Clasificación y actualización de contadores
    if experiencia > 5:
        especialistas_senior += 1
        print(f"{nombre} ha sido clasificado como Especialista Senior.")
    else:
        residentes_junior += 1
        print(f"{nombre} ha sido clasificado como Residente Junior")

# Salida Final   
print(f"\n!El hospital cuenta con {especialistas_senior} Especialistas Senior y {residentes_junior} Residentes Junior! ¡Sistema listo para operar!")