from ticket import Ticket


def cargar_vector(): #Punto 1
    primera = True
    v = []
    m = open('peajes-tp3.txt', 'rt')
    for linea in m:
        if primera:
            primera = False
        elif not primera:
            codigo = linea[0:10]
            patente = linea[10:17]
            pais_patente = None
            vehiculo = int(linea[17])
            pago = int(linea[18])
            pais = int(linea[19])
            distancia = int(linea[20:])
            t = Ticket(codigo, patente, pais_patente, vehiculo, pago, pais, distancia)
            v.append(t)
    m.close()
    return v
#OJO cada vez que se elija la opción "Crear arreglo desde registros" el arreglo debe ser creado de nuevo desde cero, perdiendo todos los registros que ya hubiese contenido.
#Falta implementar funcionalidad: Antes de eliminar el viejo arreglo, se muestre en pantalla un mensaje de advertencia al usuario de forma que tenga la opción de cancelar la operación.


def cargar_ticket_por_teclado(v): # Punto 2
    codigo = input("Ingrese el código del ticket (debe ser numérico):")
    while not codigo.isdigit():
        print("El código tiene que ser numérico.")
        codigo = input("Ingrese el código del ticket (debe ser numérico):")

    patente = input("Ingrese la patente del vehículo:")
    while not patente.isdigit() and patente.isalpha():
        print("La patente debe tener SOLO numeros y/o letras.")
        patente = input("Ingrese la patente del vehículo: ")

    pais_patente = 0

    tipo_vehiculo = (input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "))
    while tipo_vehiculo not in ['0', '1', '2']:
        print("Tipo de vehículo inválido, ingrese el valor correctamente.")
        tipo_vehiculo = input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    tipo_vehiculo = int(tipo_vehiculo)

    forma_pago = (input("Ingrese la forma de pago (1: manual, 2: telepeaje): "))
    while forma_pago not in ['1', '2']:
        print("La forma de pago debe ser 1 o 2.")
        forma_pago = input("Ingrese la forma de pago (1: manual, 2: telepeaje): ")
    forma_pago = int(forma_pago)

    pais = (input("Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "))
    while pais not in ['0', '1', '2', '3', '4']:
        print("País incorrecto, ingrese uno válido.")
        pais = input("Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")
    pais = int(pais)

    distancia = (input("Ingrese la distancia en kilómetros (000 si es la primera cabina): "))
    while not distancia.isdigit():
        print("Ingresar solo números.")
        distancia = input("Ingrese la distancia en kilómetros (000 si es la primera cabina): ")
    distancia = int(distancia)

    nuevo_ticket = Ticket(codigo, patente, pais_patente, tipo_vehiculo, forma_pago, pais, distancia)
    v.append(nuevo_ticket)
    print("Ticket agregado exitosamente.")


def ordenar_vector(v): # Punto 3
    determinar_pais(v)
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if int(v[i].codigo) > int(v[j].codigo):
                v[i], v[j] = v[j], v[i]


def mostrar_datos(v):
    ordenar_vector(v)
    for i in range(len(v)):
        print(v[i])


def determinar_pais(v):
    for i in range(len(v)):
        patente = v[i].patente
        if patente[0] == ' ':
            if 'A' <= patente[1] <= 'Z' and 'A' <= patente[2] <= 'Z' and 'A' <= patente[3] <= 'Z' and 'A' <= patente[4] \
                    <= 'Z':
                if '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                    pais_patente = 'Chile'
                else:
                    pais_patente = 'Otro'
            else:
                pais_patente = 'Otro'
        elif 'A' <= patente[0] <= 'Z' and 'A' <= patente[1] <= 'Z':
            if '0' <= patente[2] <= '9':
                if '0' <= patente[3] <= '9' and '0' <= patente[4] <= '9':
                    if '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                        pais_patente = 'Bolivia'
                    elif 'A' <= patente[5] <= 'Z' and 'A' <= patente[5] <= 'Z':
                        pais_patente = 'Argentina'
                    else:
                        pais_patente = 'Otro'
                else:
                    pais_patente = 'Otro'
            elif 'A' <= patente[3] <= 'Z':
                if '0' <= patente[4] <= '9' and '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                    pais_patente = 'Paraguay'
                else:
                    pais_patente = 'Otro'
            elif '0' <= patente[4] <= '9':
                if '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                    pais_patente = 'Uruguay'
                else:
                    pais_patente = 'Otro'
            elif '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                pais_patente = 'Brasil'
            else:
                pais_patente = 'Otro'
        else:
            pais_patente = 'Otro'
        v[i].pais_patente = pais_patente


def buscar_patente(v): # Punto 4
    determinar_pais(v)
    patente = input("Ingrese la patente a buscar:")
    while not patente.isdigit() and patente.isalpha():
        print("La patente debe tener SOLO numeros y/o letras.")
        patente = input("Ingrese la patente a buscar: ")
    x = int(input("Ingrese el pais por el que paso la patente (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))
    while x not in [0, 1, 2, 3, 4]:
        print("País incorrecto, ingrese uno válido.")
        x = int(input("Ingrese el pais por el que paso la patente (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))
    existe = False
    for i in range(len(v)):
        if patente == v[i].patente and x == v[i].pais:
            print(v[i])
            existe = True
            break
    if not existe:
        print("No hay resultados")


def buscar_codigo(v): # Punto 5
    c = input("Ingrese un codigo a buscar en el registro:")
    while not c.isdigit():
        print("El código debe ser numérico.")
        c = input("Ingrese un codigo a buscar en el registro:")
    existe = False
    for i in range(len(v)):
        if c == v[i].codigo:
            existe = True
            if v[i].pago == 1:
                v[i].pago = 2
                print("Se cambio el pago de", v[i].codigo, "de 1 a 2:\n", v[i])
                break
            else:
                v[i].pago = 1
                print("Se cambio el pago de", v[i].codigo, "de 2 a 1:\n", v[i])
                break
    if not existe:
        print("No hay resultados")


def conteo_autos_por_pais(v): # Punto 6
    contar_por_pais_auto = {}
    for ticket in v:
        pais = ticket.pais
        if pais not in contar_por_pais_auto:
            contar_por_pais_auto[pais] = 1
        else:
            contar_por_pais_auto[pais] += 1
    for pais, cantidad in contar_por_pais_auto.items():
        print(f"País: {pais} | Cantidad de autos: {cantidad}")

def calcular_importe_acumulado(v): #Punto 7
    acumulado_tipo_0 = 0
    acumulado_tipo_1 = 0
    acumulado_tipo_2 = 0
    
    for ticket in v:
        if ticket.vehiculo == 0:
            acumulado_tipo_0 += ticket.pago
        elif ticket.vehiculo == 1:
            acumulado_tipo_1 += ticket.pago        # cambie de tipo_vehiculo a vehiculo como esta en ticket en el 8 tambien
        elif ticket.vehiculo == 2:
            acumulado_tipo_2 += ticket.pago

    print("Importe acumulado por tipo de vehículo:")
    print("Motocicletas (Tipo 0):", acumulado_tipo_0)
    print("Automóviles (Tipo 1):", acumulado_tipo_1)
    print("Camiones (Tipo 2):", acumulado_tipo_2)

def tipo_vehiculo_con_mayor_monto(v): #Punto 8
    total_tipo_0 = 0
    total_tipo_1 = 0
    total_tipo_2 = 0
    
    for ticket in v:
        if ticket.vehiculo == 0:
            total_tipo_0 += ticket.pago
        elif ticket.vehiculo == 1:
            total_tipo_1 += ticket.pago
        elif ticket.vehiculo == 2:
            total_tipo_2 += ticket.pago
    
    tipo_con_mayor_monto = None
    monto_mayor = 0
    
    if total_tipo_0 > monto_mayor:
        monto_mayor = total_tipo_0
        tipo_con_mayor_monto = "Motocicletas (Tipo 0)"
    
    if total_tipo_1 > monto_mayor:
        monto_mayor = total_tipo_1
        tipo_con_mayor_monto = "Automóviles (Tipo 1)"
    
    if total_tipo_2 > monto_mayor:
        monto_mayor = total_tipo_2
        tipo_con_mayor_monto = "Camiones (Tipo 2)"
    
    if tipo_con_mayor_monto is not None:
        porcentaje = (monto_mayor / sum([total_tipo_0, total_tipo_1, total_tipo_2])) * 100
        print("El tipo de vehículo con mayor monto es:", tipo_con_mayor_monto)
        print("Monto acumulado:", monto_mayor)
        print("Porcentaje sobre el total:", round(porcentaje, 2), "%")
    else:
        print("No hay registros de vehículos.")


def promediar_distancia(v): #Punto 9
    suma = 0
    contador = 0
    for i in range(len(v)):
        suma += v[i].distancia
        contador += 1
    promedio = suma / contador if contador > 0 else 0
    # Llama a la función supera_promedio para contar vehículos que superaron el promedio
    vehiculos_superan = supera_promedio(v, promedio)
    print(f"Promedio de distancia: {promedio} km")
    print(f"Cantidad de vehículos que superaron el promedio: {vehiculos_superan}")


def supera_promedio(v, prom):
    acu_punto_9 = 0
    for i in range(len(v)):
        if v[i].distancia > prom:
            acu_punto_9 += 1
    return acu_punto_9


def principal(): # Menu de opciones
    v = []
    while True:
        print("\nMENU DE OPCIONES:")
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
            print('-' * 50, '\nPUNTO 1\n', '-' * 50)
            print('AVISO: Elegir esta opción borrará los datos cargados anteriormente.\nVolver: 0\nContinuar: 1')
            opcion = int(input('¿Desea continuar?: '))
            if opcion == 1:
                v = cargar_vector()
                print("Arreglo de registros creado desde el archivo.")
                print('-' * 50)
            else:
                pass
        # OJO cada vez que se elija la opción "Crear arreglo desde registros" el arreglo debe ser creado de nuevo desde cero, perdiendo todos los registros que ya hubiese contenido.
        # Falta implementar funcionalidad: Antes de eliminar el viejo arreglo, se muestre en pantalla un mensaje de advertencia al usuario de forma que tenga la opción de cancelar la operación.
        elif opcion == "2":
            print('-' * 50, '\nPUNTO 2\n', '-' * 50)
            cargar_ticket_por_teclado(v)
            print('Datos cargados con exito')
            print('-' * 50)
        elif opcion == "3": #Introducir mensaje de error cuando se seleccione la opcion 3 sin haber realizado un  arreglo (osea haber elegido la opcion 1)
            print('-' * 150, '\nPUNTO 3\n', '-' * 150)
            mostrar_datos(v)
            print('-' * 150)
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
            promediar_distancia(v)
        elif opcion == "10":
            print("Usted a salido del programa")
            break
        else:
            print("Opción inválida, porfavor seleccione una opción válida.")


if __name__ == '__main__':
    principal()
