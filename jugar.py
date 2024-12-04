import pygame
import random
import sys
import json
from funciones import dibujar_texto, fondo_preguntas, sonido_correcto, sonido_incorrecto, sonido_perdiste, sonido_ganaste
from pantalla_gameover import ingresar_nombre, mostrar_game_over


# Configuración básica
ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

pygame.init()


FUENTE = pygame.font.Font(None, 40)
FUENTE_PEQUEÑA = pygame.font.Font(None, 20)
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Juego de Preguntas')

def cargar_preguntas_desde_json(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        preguntas = json.load(file)
    return preguntas

preguntas = cargar_preguntas_desde_json('preguntas.json')

def obtener_puntos_por_dificultad(dificultad: str)-> int:
    """
    que hace?:asigna puntos a una pregunta en funcion de su dificultad
    que recibe?: recibe un str que es la dificultad
    que devuelve?: decuelve un valor int de los puntos 
    """
    if dificultad == "Fácil":
        return 1
    elif dificultad == "Intermedia":
        return 2
    elif dificultad == "Difícil":
        return 3
    return 0  

def mostrar_imagen_ganadora():
    imagen_ganadora = pygame.image.load("./assets/imagen_ganador.png") 
    ventana.blit(imagen_ganadora, (0, 0))
    pygame.display.update()
    pygame.time.wait(3000)  

def jugar():  
    from ranking import guardar_en_ranking
    """
    que hace?: Controla el flujo de preguntas y gestiona la puntuacion, vidas, y el tiempo
    que recibe?: utiliza variables y funciones importadas para el funcionamiento del juego.
    que devuelve?: None
    """  
    random.shuffle(preguntas) #Reorganiza aleatoriamente la lista de preguntas :)

    vidas = 3  
    puntaje = 0  
    pregunta_actual = 0  
    tiempo_inicio = pygame.time.get_ticks() 
    aciertos = 0  
    errores = 0  
    preguntas_resueltas = 0  


    while vidas > 0 and pregunta_actual < len(preguntas):  
        ventana.blit(fondo_preguntas, (0, 0))   
        pregunta = preguntas[pregunta_actual]    


        dibujar_texto(pregunta["pregunta"], FUENTE, BLANCO, ventana, ANCHO // 2, ALTO // 4)  


        for i, opcion in enumerate(pregunta["opciones"]):  
            dibujar_texto(f"{i + 1}. {opcion}", FUENTE, BLANCO, ventana, ANCHO // 2, ALTO // 2 + i * 50)  

        tiempo_limite = 8   
        reloj = pygame.time.Clock()  
        tiempo_final = pygame.time.get_ticks() + tiempo_limite * 1000   
        respuesta = None  

        while respuesta is None:  
            for evento in pygame.event.get():  
                if evento.type == pygame.QUIT:  
                    pygame.quit()  
                    sys.exit()  
                if evento.type == pygame.KEYDOWN:  
                    if evento.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:  
                        respuesta = int(evento.unicode) - 1  # Almacenar la respuesta          

            
            tiempo_restante = (tiempo_final - pygame.time.get_ticks()) // 1000  
            if tiempo_restante <= 0:   
                vidas -= 1  
                dibujar_texto("Tiempo agotado!", FUENTE, ROJO, ventana, ANCHO // 2, ALTO - 100)  
                pygame.display.update()  
                pygame.time.wait(1000)   
                break    


            ventana.blit(fondo_preguntas, (0, 0))    
            dibujar_texto(pregunta["Tema"], FUENTE, AMARILLO, ventana, ANCHO // 2, ALTO // 4.8)   
            dibujar_texto(pregunta["pregunta"], FUENTE, BLANCO, ventana, ANCHO // 2, ALTO // 4)   
            for i, opcion in enumerate(pregunta["opciones"]):  
                dibujar_texto(f"{i + 1}. {opcion}", FUENTE, BLANCO, ventana, ANCHO // 2, ALTO // 2 + i * 50)  
            

            dibujar_texto(f"Tiempo restante: {tiempo_restante}", FUENTE, ROJO, ventana, ANCHO // 2, ALTO // 10)  

            
            dibujar_texto(f"Aciertos: {aciertos}", FUENTE_PEQUEÑA, VERDE , ventana, ANCHO // 4, ALTO - 60)
            dibujar_texto(f"Errores: {errores}", FUENTE_PEQUEÑA, ROJO, ventana, ANCHO // 2, ALTO - 60)
            dibujar_texto(f"Respondidas: {preguntas_resueltas}", FUENTE_PEQUEÑA, AMARILLO, ventana, ANCHO // 1.3, ALTO - 60)

            pygame.display.update()  
            reloj.tick(30)  

        # verifica la respuesta  
        if respuesta is not None:  
            if pregunta["opciones"][respuesta] == pregunta["respuesta"]:  
                puntaje += obtener_puntos_por_dificultad(pregunta["dificultad"])  
                aciertos += 1  
                sonido_correcto.play()
            else:  
                vidas -= 1  
                errores += 1  
                sonido_incorrecto.play()

        preguntas_resueltas += 1  
        pregunta_actual += 1  

        

    tiempo_total = (pygame.time.get_ticks() - tiempo_inicio) // 1000  
    if vidas > 0 and pregunta_actual == len(preguntas):
            sonido_ganaste.play()
            mostrar_imagen_ganadora() 
            nombre_jugador = ingresar_nombre()  
            guardar_en_ranking(nombre_jugador, puntaje, tiempo_total)
    elif vidas == 0:
        sonido_perdiste.play()
        mostrar_game_over(puntaje)
        nombre_jugador = ingresar_nombre()  
        guardar_en_ranking(nombre_jugador, puntaje, tiempo_total)  



