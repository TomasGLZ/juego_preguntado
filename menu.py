import pygame
import sys
from jugar import jugar
from ranking import mostrar_ranking
from funciones import dibujar_texto, fondo_menu, sonido_select

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

def menu_principal():
    """
    que hace?: muestra las opciones del menu principal y controla la navegacion segun la opcion seleccionada.
    que recibe?: ningun parametro.
    que devuelve?:(None).

    """
    while True:
        ventana.blit(fondo_menu, [0, 0])
        dibujar_texto("1. JUGAR", FUENTE, AMARILLO, ventana, ANCHO // 2, ALTO // 3)
        dibujar_texto("2. RANKING", FUENTE, AMARILLO, ventana, ANCHO // 2, ALTO // 2)
        dibujar_texto("3. SALIR", FUENTE, AMARILLO, ventana, ANCHO // 2, ALTO // 1.5) 

        # Eventos del menú
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    sonido_select.play()
                    jugar()
                if evento.key == pygame.K_2:
                    sonido_select.play()
                    mostrar_ranking()   
                if evento.key == pygame.K_3:
                    sonido_select.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
