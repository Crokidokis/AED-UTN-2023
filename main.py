from ticket import Ticket


def cargar_vector():  # Punto 1
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

def cargar_ticket_por_teclado(v):  # Punto 2
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


def ordenar_vector(v):  # Punto 3
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

paises = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Chile", "Otro")

def determinar_pais(v):
    for i in range(len(v)):
        patente = v[i].patente
        if patente[0] == ' ':
            if 'A' <= patente[1] <= 'Z' and 'A' <= patente[2] <= 'Z' and 'A' <= patente[3] <= 'Z' and 'A' <= patente[4] \
                    <= 'Z':
                if '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                    pais_patente = paises[5]
                else:
                    pais_patente = paises[6]
            else:
                pais_patente = paises[6]
        elif 'A' <= patente[0] <= 'Z' and 'A' <= patente[1] <= 'Z':
            if '0' <= patente[2] <= '9':
                if '0' <= patente[3] <= '9' and '0' <= patente[4] <= '9':
                    if '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                        pais_patente = paises[1]
                    elif 'A' <= patente[5] <= 'Z' and 'A' <= patente[5] <= 'Z':
                        pais_patente = paises[0]
                    else:
                        pais_patente = paises[6]
                else:
                    pais_patente = paises[6]
            elif 'A' <= patente[3] <= 'Z':
                if '0' <= patente[4] <= '9' and '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                    pais_patente = paises[3]
                else:
                    pais_patente = paises[6]
            elif '0' <= patente[4] <= '9':
                if '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                    pais_patente = paises[4]
                else:
                    pais_patente = paises[6]
            elif '0' <= patente[5] <= '9' and '0' <= patente[5] <= '9':
                pais_patente = paises[2]
            else:
                pais_patente = paises[6]
        else:
            pais_patente = paises[6]
        v[i].pais_patente = pais_patente


def buscar_patente(v):  # Punto 4
    determinar_pais(v)
    patente = input("Ingrese la patente a buscar:")
    while not patente.isdigit() and patente.isalpha():
        print("La patente debe tener SOLO numeros y/o letras.")
        patente = input("Ingrese la patente a buscar: ")
    x = int(input(
        "Ingrese el pais por el que paso la patente (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))
    while x not in [0, 1, 2, 3, 4]:
        print("País incorrecto, ingrese uno válido.")
        x = int(input(
            "Ingrese el pais por el que paso la patente (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay):"))
    existe = False
    for i in range(len(v)):
        if patente == v[i].patente and x == v[i].pais:
            print(v[i])
            existe = True
            break
    if not existe:
        print("No hay resultados")


def buscar_codigo(v):  # Punto 5
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


def conteo_autos_por_pais(v):
    vec_conteo = [0] * 7










def calcular_monto(v):  # Punto 7
    acum = 3*[0]
    for i in range(len(v)):
        importe_basico = 300
        if v[i].pais == 1:
            importe_basico = 200
        elif v[i].pais == 2:
            importe_basico = 400

        if v[i].pago == 2:
            importe_basico = importe_basico - (importe_basico * 10 / 100)

        if v[i].vehiculo == 0:
            importe_final = importe_basico - (importe_basico * 50) / 100
            acum[0] += importe_final
        elif v[i].vehiculo == 1:
            importe_final = importe_basico
            acum[1] += importe_final
        elif v[i].vehiculo == 2:
            importe_final = importe_basico + (importe_basico * 60) / 100
            acum[2] += importe_final

    return acum


def mayor_monto(acum): # Punto 8
    total1 = acum[0]
    total2 = acum[1]
    total3 = acum[2]
    suma = mayor = 0
    vehiculos = ('Motocicleta', 'Automovil', 'Camión')
    if total1 > total2 and total1 > total3:
        print('Vehículo con mayor monto: ', vehiculos[0])
        mayor = total1
    elif total2 > total3:
        print('Vehículo con mayor monto: ', vehiculos[1])
        mayor = total2
    else:
        print('Vehículo con mayor monto: ', vehiculos[2])
        mayor = total3

    suma = total1 + total2 + total3
    print('Su importe representa el ', round(mayor * 100 / suma, 2), '% del total.')


def promediar_distancia(v):  # Punto 9
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


def principal():  # Menu de opciones
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
        elif opcion == "2":
            print('-' * 50, '\nPUNTO 2\n', '-' * 50)
            cargar_ticket_por_teclado(v)
            print('-' * 50)
        elif opcion == "3":  # Introducir mensaje de error cuando se seleccione la opcion 3 sin haber realizado un  arreglo (osea haber elegido la opcion 1)
            print('-' * 150, '\nPUNTO 3\n', '-' * 150)
            mostrar_datos(v)
            print('-' * 150)
        elif opcion == "4":
            print('-' * 50, '\nPUNTO 4\n', '-' * 50)
            buscar_patente(v)
            print('-' * 50)
        elif opcion == "5":
            print('-' * 50, '\nPUNTO 5\n', '-' * 50)
            buscar_codigo(v)
            print('-' * 50)
        elif opcion == "6":
            print('-' * 50, '\nPUNTO 6\n', '-' * 50)
            conteo_autos_por_pais(v)
            print('-' * 50)
        elif opcion == "7":
            print('-' * 50, '\nPUNTO 7\n', '-' * 50)
            acum = calcular_monto(v)
            print('Motocicleta: ', acum[0], '\nAutomóvil: ', acum[1], '\nCamión: ', acum[2])
            print('-' * 50)
        elif opcion == "8":
            print('-' * 50, '\nPUNTO 8\n', '-' * 50)
            acum = calcular_monto(v)
            mayor_monto(acum)
            print('-' * 50)
        elif opcion == "9":
            print('-' * 50, '\nPUNTO 9\n', '-' * 50)
            promediar_distancia(v)
            print('-' * 50)
        elif opcion == "10":
            print('-' * 50)
            print("Usted a salido del programa")
            print('-' * 50)
            break
        else:
            print("Opción inválida, porfavor seleccione una opción válida.")


if __name__ == '__main__':
    principal()
