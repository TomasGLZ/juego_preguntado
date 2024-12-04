import pygame

ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

pygame.init()
FUENTE = pygame.font.Font(None, 40)

# se inicializa la ventana 
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Juego de Preguntas')

# aca se cargan las imagenes 
fondo_menu = pygame.image.load("assets/pantalla_inicio.png").convert()
fondo_preguntas = pygame.image.load("assets/fondopreguntas.png").convert()
game_over_image = pygame.image.load('assets/gamerovernew.png').convert()
fondo_ranking = pygame.image.load('assets/fondoranking.png').convert()
fondo_ingresar_nombre = pygame.image.load('assets/ingrese_nombre.png').convert() 
#Sonidos
sonido_correcto = pygame.mixer.Sound("./assets/sounds/smrpg_correct.wav")
sonido_incorrecto = pygame.mixer.Sound("./assets/sounds/incorrect.wav")
sonido_select = pygame.mixer.Sound("assets/sounds/590039__mrfossy__sfx_massivelyincorrekt_06.wav")
sonido_ganaste = pygame.mixer.Sound("assets/sounds/ganaste.wav")
sonido_perdiste = pygame.mixer.Sound("assets/sounds/perdiste.wav")
sonido_escribir = pygame.mixer.Sound("assets/sounds/escribiendo.wav")
sonido_correcto.set_volume(0.5)  
sonido_incorrecto.set_volume(0.5) 
sonido_select.set_volume(0.5)
sonido_ganaste.set_volume(0.7)
sonido_perdiste.set_volume(0.7)
sonido_escribir.set_volume(0.5)



def dibujar_texto(texto, fuente, color, superficie, x, y):

    """
    que hace?: Dibuja texto en una superficie.
    que recibe: Texto, fuente, color, superficie, y las coordenadas (x, y).
    que devuelve?: None.

    """

    texto_obj = fuente.render(texto, True, color)
    texto_rect = texto_obj.get_rect(center=(x, y))
    superficie.blit(texto_obj, texto_rect)

