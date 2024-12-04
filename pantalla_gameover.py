import pygame
import sys
from funciones import game_over_image, dibujar_texto, fondo_ingresar_nombre, sonido_escribir


ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

pygame.init()

FUENTE = pygame.font.Font(None, 40)

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Juego de Preguntas')
def mostrar_game_over(puntaje):
    """
    que hace?: muestra la pantalla de "Game Over" al jugador.
    que recibe: recibe el puntaje, que es un entero.
    que devuelve:(None).

        
    """
    ventana.blit(game_over_image, (0, 0))
    dibujar_texto(f"Tu puntaje: {puntaje}", FUENTE, AMARILLO, ventana, ANCHO // 2, ALTO // 1.5)
    pygame.display.update()
    pygame.time.wait(3000) 

def ingresar_nombre():
    """
    que hace?: Permite que el jugador ingrese su nombre y lo muestra en la pantalla.
    que recibe?: ningun parametro.
    que devuelve?: devuelve el nombre ingresado como una cadena

    """
    nombre = ''
    max_caracteres = 10
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                sonido_escribir.play()
                if evento.key == pygame.K_RETURN:
                    return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if len(nombre) < max_caracteres:
                        nombre += evento.unicode

        ventana.blit(fondo_ingresar_nombre, (0, 0))
        dibujar_texto(nombre, FUENTE, NEGRO, ventana, ANCHO // 2, ALTO // 1.8)
        pygame.display.update()  


        pygame.display.update()

