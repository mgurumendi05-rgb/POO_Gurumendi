# Clase que representa un motor
class Motor:
    def __init__ (self, tipo, potencia):
        # Guardar los datos del motor
        self._tipo = tipo
        self._potencia = potencia

    #Encapsulamiento con property
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, v): self._tipo = v

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, v): self._potencia = v

    #Métodos de su comportamiento
    def encender_motor(self):
        return "Motor encendido"

    def detener_motor(self):
        return "Motor apagado"

    #Para representar en texto
    def __str__(self):
        return f"Motor({self._tipo}, {self._potencia}hp)"