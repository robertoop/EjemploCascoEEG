#pip install pyserial
def Identificar_Puertos():
    import serial.tools.list_ports

    puertos=serial.tools.list_ports.comports()
    print(puertos)
    for puerto in puertos:
        print(puerto)
#pip install pylsl

def LeerStream(nombre="AURA"):
    from pylsl import resolve_stream ,StreamInlet

    streams=resolve_stream("name",nombre)
    inlet=StreamInlet(streams[0])

    return inlet

def LeerDato(Stream):
    EEGDatos,TimeStamp=Stream.pull_sample()
    #SF=(4500000)/24/(28*3-1)#uV/conteo
    SF=1
    Datos=EEGDatos*SF
    Datos.append(TimeStamp)
    return Datos


def Fakedata():
    from pylsl import StreamInfo,StreamOutlet
    import time
    import random

    info= StreamInfo("FakeData","EEG",8,100,"float32","myid123")
    outlet= StreamOutlet(info)
    print("Mandando datos...")

    while True:
        datosfalsos=[random.random(),random.random(),
                     random.random(),random.random(),
                     random.random(),random.random(),
                     random.random(),random.random()]

        stamp=time.time_ns()/1000000000
        outlet.push_sample(datosfalsos,stamp)
        time.sleep(0.01)



