from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

# Motores
m1 = Motor("Gasolina", 120)
m2 = Motor("Diesel", 140)
m3 = Motor("Gasolina", 95)
m4 = Motor("Electrico", 180)

# Automóviles
a1 = Automovil("Kia", "Rio", 2020, m1, 4)
a2 = Automovil("Chevrolet", "Spark", 2024, m2, 2)

# Motocicletas
mo1 = Motocicleta("Suzuki", "Gixxer", 2016, m3, 155)
mo2 = Motocicleta("Honda", "CBR", 2020, m4, 200)

# Métodos
print(a1.abrir_maletero())
print(a2.tocar_claxon())
print(mo1.hacer_caballito())
print(mo2.usar_patada_arranque())

# Mostrar
print(a1)
print(a2)
print(mo1)
print(mo2)