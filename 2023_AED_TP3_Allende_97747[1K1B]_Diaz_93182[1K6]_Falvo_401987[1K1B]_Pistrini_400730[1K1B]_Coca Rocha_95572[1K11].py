class Ticket:
    def __init__(self, cod, pat, vehiculo, pago, pais, dist):
        self.codigo = cod
        self.patente = pat
        self.vehiculo = vehiculo
        self.pago = pago
        self.pais = pais
        self.distancia = dist

    def _str_(self):
        cad = 'Código:  {}  | Patente N°  {}  | Tipo de vehículo:  {}  | Forma de pago:  {}  | País de la cabina:  {}  | Distancia recorrida:  {}'
        return cad.format(self.codigo, self.patente, self.vehiculo, self.pago, self.pais, self.distancia)

def cargar_vector():
    primera = True
    v = []
    m = open('peajes-tp3.txt','rt')
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

def validacion(): 
    pass
    
def cargar_ticket_por_teclado(v):
    codigo = input("Ingrese el código del ticket: ")
    while not codigo.isdigit() or len(codigo) != 10:
        print("El código del ticket debe tener 10 dígitos numéricos.")
        codigo = input("Ingrese el código del ticket: ")

    patente = input("Ingrese la patente del vehículo: ")
    while len(patente) != 7:
        print("La patente debe tener 7 carácteres.")
        patente = input("Ingrese la patente del vehículo (7 carácteres): ")

    tipo_vehiculo = input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    while tipo_vehiculo not in ['0', '1', '2']:
        print("Tipo de vehículo inválido, ingrese el valor correctamente.")
        tipo_vehiculo = input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")

    forma_pago = input("Ingrese la forma de pago (1: manual, 2: telepeaje): ")
    while forma_pago not in ['1', '2']:
        print("La forma de pago debe ser 1 o 2.")
        forma_pago = input("Ingrese la forma de pago (1: manual, 2: telepeaje): ")

    pais = input("Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")
    while pais not in ['0', '1', '2', '3', '4']:
        print("País incorrecto, ingrese uno válido.")
        pais = input("Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")

    distancia = input("Ingrese la distancia en kilómetros (debe tener 3 dígitos, 000 si es la primera cabina): ")
    while not distancia.isdigit() or len(distancia) == 3:
        print("La distancia debe ser un número entero de 3 dígitos.")
        distancia = input("Ingrese la distancia en kilómetros (debe tener 3 dígitos, 000 si es la primera cabina): ")

    codigo = int(codigo)
    tipo_vehiculo = int(tipo_vehiculo)
    forma_pago = int(forma_pago)
    pais = int(pais)
    distancia = int(distancia)

    nuevo_ticket = Ticket(codigo, patente, tipo_vehiculo, forma_pago, pais, distancia)
    v.append(nuevo_ticket)

    print("Ticket agregado con exitosamente.")

def ordenar_vector(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

def buscar_patente(v): # 4
    p = input("Ingrese la patente a buscar: ")
    x = int(input("Ingrese el pais por el que paso la patente: "))
    existe = False
    for i in range(len(v)):
        if p == v[i].patente and x == v[i].pais:
            print(v[i])
            existe = True
            break
    if not existe:
        print("No hay resultados")

def buscar_codigo(v): # 5
    c = int(input("Ingrese un codigo a buscar en el registro: "))
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

def mostrar_datos(v):
    ordenar_vector(v)
    for i in range(len(v)):
        print(v[i])
        

def conteo_autos_por_pais(v):
    contar_por_pais_auto = {}

    for ticket in v:
        pais = ticket.pais

        if pais not in contar_por_pais_auto:
            contar_por_pais_auto[pais] = 1
        else:

            contar_por_pais_auto[pais] += 1


    for pais, cantidad in contar_por_pais_auto.items():
        print(f"País: {pais} | Cantidad de autos: {cantidad}")



def principal():

    v = []  # Inicia el arreglo de registros vacío

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

        elif opcion == "2":
            cargar_ticket_por_teclado(v)

        elif opcion == "3":
            mostrar_datos(v)

        elif opcion == "4":
            buscar_patente(v)

        elif opcion == "5":
            # Implementa la opción para cambiar la forma de pago por código de ticket
            cambiar_forma_pago(v)

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
            print("Opción no inválida.seleccione una opción válida.")


if __name__ == '__main__':
    principal()
