import pygame
import sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Carga imagen y posicion al azar")
#colores
colorFondo = (1, 150, 70)
colorRectangulo = (255, 60, 40)
#carga imagen
imagen = pygame.image.load("imagenes/pygame.png")
#posicion imagen
posX1, posY1 = (10, 40)
while True:
    ventana.fill(colorFondo)
    ventana.blit(imagen, (posX1, posY1))
    for i in range (15):
        posX2, posY2 = randint(1, 500), randint(1,300)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        colorRectangulo = (r, g, b)
        pygame.draw.rect(ventana, colorRectangulo,(posX2, posY2, 40, 40))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()