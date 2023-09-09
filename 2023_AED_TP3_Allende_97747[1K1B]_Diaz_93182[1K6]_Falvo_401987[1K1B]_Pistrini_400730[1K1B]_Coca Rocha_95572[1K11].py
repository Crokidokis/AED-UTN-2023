class Ticket:
    def _init_(self, cod, pat, vehiculo, pago, pais, dist):
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
    
def ordenar_vector(v)
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

def mostrar_datos(v)
ordenar_vector(v)
for i in range(len(v)):
    print(v[i])

def principal():
    # opcion 1
    v = cargar_vector()
    # opcion 3
    mostrar_datos(v)


if _name_ == '__main__':
    principal()
