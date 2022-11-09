import pygame
import time
from FuncionesEGG import *
import numpy

nombreUsuario="FernandoRuido"

pygame.init()
ventana=pygame.display.set_mode([600,600])
Reloj=pygame.time.Clock()
S=LeerStream()


blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)

fuente1=pygame.font.Font("freesansbold.ttf", 40)

def MostrarInstruccion(ventana,Ins="Piense en cualquier cosa"):
    ventana.fill(blanco)
    mensaje=fuente1.render(Ins,
                           True,rojo,blanco)
    mensajeRect= mensaje.get_rect()
    mensajeRect.center=(600//2,600//2)
    ventana.blit(mensaje,mensajeRect)





Terminar=False
Inicio=time.time()
DatosTotales=[]
while (time.time()-Inicio)<90:
    if Terminar==True:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Terminar=True
    Datos = LeerDato(S)
    if time.time()-Inicio<5:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<10:
        MostrarInstruccion(ventana,"Arriba")
        Datos.append(1)
    elif time.time()-Inicio<15:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<20:
        MostrarInstruccion(ventana,"Abajo")
        Datos.append(2)
    elif time.time()-Inicio<25:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<30:
        MostrarInstruccion(ventana,"Derecha")
        Datos.append(3)
    elif time.time()-Inicio<35:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<40:
        MostrarInstruccion(ventana,"Izquierda")
        Datos.append(4)
    elif time.time()-Inicio<45:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<50:
        MostrarInstruccion(ventana,"A delante")
        Datos.append(5)
    elif time.time()-Inicio<55:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<60:
        MostrarInstruccion(ventana,"Atras")
        Datos.append(6)
    elif time.time()-Inicio<65:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<70:
        MostrarInstruccion(ventana,"Quieto")
        Datos.append(7)
    elif time.time()-Inicio<75:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<80:
        MostrarInstruccion(ventana,"Vuelta Izquierda")
        Datos.append(8)
    elif time.time()-Inicio<85:
        MostrarInstruccion(ventana)
        Datos.append(0)
    elif time.time()-Inicio<90:
        MostrarInstruccion(ventana,"Vuelta Derecha")
        Datos.append(9)
    pygame.display.update()
    DatosTotales.append(Datos)
    Reloj.tick(30)

nombrearchivo="Datos_"+nombreUsuario+"_"+str(time.time())+".npy"
with open (nombrearchivo,"wb") as f:
    numpy.save(f,numpy.array(DatosTotales))
pygame.quit()
