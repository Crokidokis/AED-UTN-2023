from ticket import Ticket

def cargar_vector(): #Punto 1
    primera = True
    v = []
    m = open('peajes-tp3.txt', 'rt')
    for linea in m:
        if primera:
            primera = False
        elif not primera:
            codigo = int(linea[0:10])
            patente = linea[10:17]
            vehiculo = int(linea[17])
            pago = int(linea[18])
            pais = int(linea[19])
            distancia = int(linea[20:])
            t = Ticket(codigo, patente, vehiculo, pago, pais, distancia)
            v.append(t)
    m.close()
    return v
#OJO cada vez que se elija la opción "Crear arreglo desde registros" el arreglo debe ser creado de nuevo desde cero, perdiendo todos los registros que ya hubiese contenido.
#Falta implementar funcionalidad: Antes de eliminar el viejo arreglo, se muestre en pantalla un mensaje de advertencia al usuario de forma que tenga la opción de cancelar la operación.

def cargar_ticket_por_teclado(v): #Punto 2
    codigo = int(input("Ingrese el código del ticket (debe tener 10 dígitos numéricos):"))
    while not codigo.isdigit() or len(codigo) != 10:
        print("El código del ticket debe tener 10 dígitos numéricos.")
        codigo = input("Ingrese el código del ticket (debe tener 10 dígitos numéricos):")

    patente = input("Ingrese la patente del vehículo (7 carácteres):")
    while len(patente) != 7:
        print("La patente debe tener 7 carácteres.")
        patente = input("Ingrese la patente del vehículo (7 carácteres): ")

    tipo_vehiculo = int(input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "))
    while tipo_vehiculo not in [0, 1, 2]:
        print("Tipo de vehículo inválido, ingrese el valor correctamente.")
        tipo_vehiculo = input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")

    forma_pago = int(input("Ingrese la forma de pago (1: manual, 2: telepeaje): "))
    while forma_pago not in [1, 2]:
        print("La forma de pago debe ser 1 o 2.")
        forma_pago = input("Ingrese la forma de pago (1: manual, 2: telepeaje): ")

    pais = int(input("Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "))
    while pais not in [0, 1, 2, 3, 4]:
        print("País incorrecto, ingrese uno válido.")
        pais = input("Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")

    distancia = int(input("Ingrese la distancia en kilómetros (debe tener 3 dígitos, 000 si es la primera cabina): "))
    while not distancia.isdigit() or len(distancia) != 3:
        print("La distancia debe ser un número entero de 3 dígitos.")
        distancia = input("Ingrese la distancia en kilómetros (debe tener 3 dígitos, 000 si es la primera cabina): ")

    nuevo_ticket = Ticket(codigo, patente, tipo_vehiculo, forma_pago, pais, distancia)
    v.append(nuevo_ticket)
    print("Ticket agregado exitosamente.")

def ordenar_vector(v): #Punto 3
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]
def mostrar_datos(v):
    ordenar_vector(v)
    for i in range(len(v)):
        print(v[i])

def buscar_patente(v): #Punto 4
    p = input("Ingrese la patente a buscar (7 carácteres):")
    while len(p) != 7:
        print("La patente debe tener 7 carácteres.")
        p = input("Ingrese la patente a buscar (7 carácteres):")
    x = int(input("Ingrese el pais por el que paso la patente (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))
    while x not in [0, 1, 2, 3, 4]:
        print("País incorrecto, ingrese uno válido.")
        x = int(input("Ingrese el pais por el que paso la patente (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))
    existe = False
    for i in range(len(v)):
        if p == v[i].patente and x == v[i].pais:
            print(v[i])
            existe = True
            break
    if not existe:
        print("No hay resultados")

def buscar_codigo(v): # Punto 5
    c = int(input("Ingrese un codigo a buscar en el registro (debe tener 10 dígitos numéricos:"))
    while not c.isdigit() or len(c) != 10:
        print("El código del ticket debe tener 10 dígitos numéricos.")
        c = int(input("Ingrese un codigo a buscar en el registro (debe tener 10 dígitos numéricos:"))
    izq, der = 0, len(v) - 1
    existe = False
    while izq <= der: #and not romper:
        x = (izq + der) // 2
        if c == v[x].codigo:
            existe = True
            if v[x].pago == 1:
                v[x].pago = 2
                print("Se cambio el pago de", v[x].codigo, "de 1 a 2:\n", v[x])
                break
            else:
                v[x].pago = 1
                print("Se cambio el pago de", v[x].codigo, "de 2 a 1:\n", v[x])
                break
        if c < v[x].codigo:
            der = x - 1
        else:
            izq = x + 1
    if not existe:
        print("No hay resultados")

def conteo_autos_por_pais(v): #Punto 6
    contar_por_pais_auto = []
    for ticket in v:
        pais = ticket.pais
        if pais not in contar_por_pais_auto:
            contar_por_pais_auto[pais] = 1
        else:
            contar_por_pais_auto[pais] += 1
    for pais, cantidad in contar_por_pais_auto.items():
        print(f"País: {pais} | Cantidad de autos: {cantidad}")

def calcular_importe_acumulado(v): #Punto 7
    pass

def tipo_vehiculo_con_mayor_monto(v): #Punto 8
    pass

def distancia_promedio(v): #Punto 9
    pass

def principal(): #Menu de opciones
    v = []
    while True:
        print("\nMenu de opciones:")
        print("1. Crear arreglo de registros desde el archivo")
        print("2. Cargar nuevo ticket")
        print("3. Mostrar todos registros ordenados por ticket")
        print("4. Buscar por patente y país")
        print("5. Cambiar forma de pago por código de ticket")
        print("6. Cantidad de vehículos por país")
        print("7. Calcular importe acumulado por tipo de vehículo")
        print("8. Vehículo con mayor monto y su porcentaje")
        print("9. Distancia promedio y vehículos que la superan")
        print("10. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            v = cargar_vector()
            print("Arreglo de registros creado desde el archivo.")
        # OJO cada vez que se elija la opción "Crear arreglo desde registros" el arreglo debe ser creado de nuevo desde cero, perdiendo todos los registros que ya hubiese contenido.
        # Falta implementar funcionalidad: Antes de eliminar el viejo arreglo, se muestre en pantalla un mensaje de advertencia al usuario de forma que tenga la opción de cancelar la operación.
        elif opcion == "2":
            cargar_ticket_por_teclado(v)
        elif opcion == "3":
            mostrar_datos(v)
        elif opcion == "4":
            buscar_patente(v)
        elif opcion == "5":
            buscar_codigo(v)
        elif opcion == "6":
            conteo_autos_por_pais(v)
        elif opcion == "7":
            calcular_importe_acumulado(v)
        elif opcion == "8":
            tipo_vehiculo_con_mayor_monto(v)
        elif opcion == "9":
            distancia_promedio(v)
        elif opcion == "10":
            print("Usted a salido del programa")
            break
        else:
            print("Opción inválida, porfavor seleccione una opción válida.")

if __name__ == '__main__':
    principal()