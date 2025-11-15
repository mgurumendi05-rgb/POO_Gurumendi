from vehiculo import Vehiculo
# Clase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, puertas):
        super().__init__(marca, modelo, anio, motor)
        # Guardar el número de puertas
        self._puertas = puertas

    # Comportamiento del maletero
    def abrir_maletero(self):
        return "Maletero abierto"

    def tocar_claxon(self):
        return "Beep!"

    #Para representar en texto
    def __str__(self):
        return super().__str__() + f", {self._puertas} puertas"