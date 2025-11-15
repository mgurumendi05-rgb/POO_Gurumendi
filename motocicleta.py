from vehiculo import Vehiculo
# Clase Motocicleta que hereda de Vehículo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        super().__init__(marca, modelo, anio, motor)
        # Guardar el cilindraje
        self._cilindraje = cilindraje

        #Comportamiento de la moto
    def hacer_caballito(self):
        return "La moto está haciendo un caballito"

    def usar_patada_arranque(self):
        return "La moto arrancó con patada"

    # Para representar en texto
    def __str__(self):
        return super().__str__() + f", {self._cilindraje} cc"