import pygame
import sys
from menu import *
from funciones import dibujar_texto, fondo_ranking


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

def mostrar_ranking():
    """
    que hace?: muestra el ranking de jugadores y permite regresar al menu.
    que recibe?: ningun parametro.
    que devuelve?: (None).
    """
    ventana.blit(fondo_ranking, (0, 0))

    jugadores_ordenados = ordenar_ranking()  
    if jugadores_ordenados:
        for i, (nombre, puntaje, tiempo) in enumerate(jugadores_ordenados):
        
            if i == 0:
                color = AMARILLO
            else:
                color = BLANCO  

            texto = f"Top {i + 1} - {nombre}: {puntaje} (Tiempo: {tiempo} seg)"
            dibujar_texto(texto, FUENTE, color, ventana, ANCHO // 2, ALTO // 5 + (i + 1) * 40)
    else:
        dibujar_texto("No hay rankings disponibles.", FUENTE, NEGRO, ventana, ANCHO // 2, ALTO // 10 + 40)

    
    mensaje_escape = "Presiona ESC para volver al menú principal"
    dibujar_texto(mensaje_escape, FUENTE, NEGRO, ventana, ANCHO // 2, ALTO - 40)  

    pygame.display.update()

   
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:  
                if evento.key == pygame.K_ESCAPE:  
                    return  

        pygame.display.update()

def guardar_en_ranking(nombre, puntaje, tiempo):
    """
    que hace?: Guarda el nombre, puntaje y tiempo de un jugador en un ranking, ordenando adecuadamente y actualizando el archivo correspondiente.
    que recibe?: nombre (cadena), puntaje, y tiempo.
    que devuelve?:(None)
    """
    
    puntaje = int(puntaje)
    tiempo = int(tiempo)

    
    jugadores_ordenados = ordenar_ranking()

    
    if len(jugadores_ordenados) < 12 or puntaje > jugadores_ordenados[-1][1]:  
        
        jugadores_ordenados.append((nombre, puntaje, tiempo))

        
        jugadores_ordenados.sort(key=lambda x: (x[1], x[2]), reverse=True)

        
        jugadores_ordenados = jugadores_ordenados[:12]

        
        with open("ranking.txt", "w") as f:
            for nombre, puntaje, tiempo in jugadores_ordenados:
                f.write(f"{nombre}: {puntaje}: {tiempo}\n")

def ordenar_ranking():
    """
    que hace?: Lee el archivo de ranking, ordena los jugadores y guarda los mejores en el archivo.
    que recibe?: ningun parametro.
    que devuelve?: una lista de tuplas con los mejores jugadores

    """
    try:
        with open("ranking.txt", "r") as f:
            lineas = f.readlines()

        
        jugadores = []
        for linea in lineas:
            partes = linea.strip().split(":")
            if len(partes) == 3:  
                nombre = partes[0].strip()
                try:
                    puntaje = int(partes[1].strip())
                    tiempo = int(partes[2].strip())  
                    jugadores.append((nombre, puntaje, tiempo))
                except ValueError:
                    continue

        
        jugadores.sort(key=lambda x: (x[1], x[2]), reverse=True)

        
        jugadores_top_12 = jugadores[:12]

        
        with open("ranking.txt", "w") as f:
            for nombre, puntaje, tiempo in jugadores_top_12:
                f.write(f"{nombre}: {puntaje}: {tiempo}\n")

        return jugadores_top_12

    except FileNotFoundError:
        print("Archivo ranking.txt no encontrado.")
        return []
