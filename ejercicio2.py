stock_disponible = 120
capacidad_maxima = 120
historial_prestamos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:
    print("=== Menú Principal ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo de libros")
    print("3. Devolver préstamo de libros")
    print("4. Historial de préstamos")
    print("5. Salir")
    
    try:
        opcion = int(input("Selecione una opción: "))

        if opcion == 1:
            print(f"Libros actualmente disponibles: {stock_disponible}")
        
        elif opcion == 2:
            try:
                cantidad = int(input("Ingresa cantidad de libros a prestar: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
                elif cantidad > stock_disponible:
                    print(f"La cantidad no puede superar el stock actual de libros. Solo quedan {stock_disponible} libros.")
                else:
                    stock_disponible -= cantidad
                    historial_prestamos += cantidad
                    print(f"Préstamo realizado con exito. Libros restantes: {stock_disponible}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == 3:
            try:
                cantidad = int(input("Ingresa cantidad de libros a devolver: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
                elif stock_disponible + cantidad > capacidad_maxima:
                    print(f"Error: La devolución supera la capacidad máxima de {capacidad_maxima} libros")
                else:
                    stock_disponible += cantidad
                    historial_prestamos -= cantidad
                    print(f"Devolución exitosa. Libros disponibles: {stock_disponible}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == 4:
            print(f"Cantidad total de préstamos activos en la sesión: {historial_prestamos}")
        
        elif opcion == 5:
            print("Gracias por utilizar nuestra sistema de gestión de libros de la Biblioteca Central. Hasta la próxima")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
    except ValueError:
        print("Error: Por favor, ingrese un número para seleccionar una opción del menú")
        

                
