from FuncionesEGG import *
from datetime import datetime
from time import sleep
import numpy
import keyboard

S=LeerStream("FakeData")

DatosTotales=[]
for i in range(1000):
    Datos=LeerDato(S)
    if keyboard.is_pressed("1"):
        Datos.append(1)
    elif keyboard.is_pressed("2"):
        Datos.append(2)
    else:
        Datos.append(0)
    #print(Datos)
    Fecha=datetime.fromtimestamp(Datos[8])
    print(Fecha)
    DatosTotales.append(Datos)

print(DatosTotales)
with open ("DatosExperimento1.npy","wb") as f:
    numpy.save(f,numpy.array(DatosTotales))
