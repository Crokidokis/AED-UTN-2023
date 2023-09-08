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
    v = []
    m = open('peajes-tp3.txt', 'rt')
    for linea in m:
        if linea != 0:
            codigo = linea[0:10]
            patente = linea[10:17]
            vehiculo = int(linea[17])
            pago = int(linea[18])
            pais = int(linea[19])
            distancia = int(linea[20:23])
            ticket = Ticket(codigo, patente, vehiculo, pago, pais, distancia)
            v.append(ticket)
    m.close()
    return v


def principal():
    # opcion 1
    v = cargar_vector()
    print(v)


if _name_ == '__main__':
    principal()