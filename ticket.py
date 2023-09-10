class Ticket: # Definición de la Clase
    def __init__(self, cod, pat, ppat,  vehiculo, pago, pais, dist):
        self.codigo = cod
        self.patente = pat
        self.pais_patente = ppat
        self.vehiculo = vehiculo
        self.pago = pago
        self.pais = pais
        self.distancia = dist

    def __str__(self):
        cad = 'Código:  {}  | Patente N°  {:^7} - {:<9}  | Tipo de vehículo:  {}  | Forma de pago:  {}  |' \
              ' País de la cabina: {}  | Distancia recorrida:  {}'
        return cad.format(self.codigo, self.patente, self.pais_patente, self.vehiculo, self.pago, self.pais, self.distancia)
