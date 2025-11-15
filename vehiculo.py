# Superclase que será heredada por Automóvil y Motocicleta.
class Vehiculo:
    def __init__(self, marca, modelo, anio, motor):
        # Guardar los datos del vehiculo
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor #composición: motor es objeto Motor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, v): self._marca = v

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, v): self._modelo = v

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, v): self._anio = v

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, v): self._motor = v

    # Comportamiento del motor
    def encender(self):
        return self._motor.encender_motor()

    def apagar(self):
        return self._motor.detener_motor()

    #Para representar en texto
    def __str__(self):
        return f"{self._marca} {self._modelo} ({self._anio}) - {self._motor}"