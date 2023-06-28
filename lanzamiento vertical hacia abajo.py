import tkinter as tk
import pygame
from pygame.locals import *

# Dimensiones de la ventana de Pygame
ANCHO = 800
ALTO = 600


def calcular():
    # Variables para el cálculo
    altura_inicial = float(altura_entry.get())
    velocidad_inicial = float(velocidad_entry.get())
    area_explosion = float(area_entry.get())
    velocidad_piloto = float(velocidad_piloto_entry.get())

    tiempo_vuelo = (velocidad_inicial + (velocidad_inicial ** 2 + 2 * 9.8 * altura_inicial) ** 0.5) / 9.8

    tiempo_impacto = tiempo_vuelo
    velocidad_impacto = velocidad_inicial + 9.8 * tiempo_impacto

    if tiempo_impacto * velocidad_piloto < area_explosion:
        resultado_label.config(
            text=f"La bomba te dañó.\nVelocidad final: {velocidad_impacto} m/s\nTiempo de vuelo: {tiempo_vuelo} s")
    else:
        resultado_label.config(
            text=f"La bomba no te dañó.\nVelocidad final: {velocidad_impacto} m/s\nTiempo de vuelo: {tiempo_vuelo} s")


def simular():
    # Variables para la simulación
    altura_inicial = float(altura_entry.get())
    velocidad_inicial = float(velocidad_entry.get())
    area_explosion = float(area_entry.get())
    velocidad_piloto = float(velocidad_piloto_entry.get())

    tiempo_vuelo = (velocidad_inicial + (velocidad_inicial ** 2 + 2 * 9.8 * altura_inicial) ** 0.5) / 9.8

    tiempo_impacto = tiempo_vuelo
    velocidad_impacto = velocidad_inicial + 9.8 * tiempo_impacto

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Simulación")

    avion_rect = pygame.Rect(ANCHO // 2, 50, 50, 20)
    bomba_rect = pygame.Rect(ANCHO // 2, 100, 20, 20)
    explosion_rect = None

    reloj = pygame.time.Clock()

    tiempo_transcurrido = 0

    while tiempo_transcurrido <= tiempo_vuelo:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        ventana.fill((255, 255, 255))

        # Mover el avión hacia la derecha según la velocidad del piloto
        avion_rect.x += int(velocidad_piloto)

        # Calcular la posición vertical de la bomba en función del tiempo
        tiempo_transcurrido += reloj.tick(
            60) / 1000  # Obtener el tiempo transcurrido desde el último fotograma en segundos
        bomba_rect.y = int((tiempo_transcurrido / tiempo_vuelo) * (ALTO - bomba_rect.height))

        # Verificar si la bomba ha alcanzado el suelo
        if tiempo_transcurrido >= tiempo_vuelo:
            if explosion_rect is None:
                explosion_rect = pygame.Rect(bomba_rect.x - area_explosion // 2, ALTO - area_explosion, area_explosion,
                                             area_explosion)
                if explosion_rect.colliderect(avion_rect):
                    resultado_label.config(text="La bomba te dañó.")
                else:
                    resultado_label.config(text="La bomba no te dañó.")
            else:
                if explosion_rect.width < area_explosion:
                    explosion_rect.inflate_ip(1, 1)

        # Dibujar los elementos en la ventana
        pygame.draw.rect(ventana, (0, 0, 255), avion_rect)
        pygame.draw.rect(ventana, (255, 0, 0), bomba_rect)
        if explosion_rect:
            pygame.draw.rect(ventana, (255, 255, 0), explosion_rect)

        pygame.display.flip()


# Crear la ventana principal de Tkinter
ventana_tk = tk.Tk()
ventana_tk.title("Simulación de vuelo")

# Etiquetas y campos de entrada
altura_label = tk.Label(ventana_tk, text="Altura inicial (metros):")
altura_label.pack()
altura_entry = tk.Entry(ventana_tk)
altura_entry.pack()

velocidad_label = tk.Label(ventana_tk, text="Velocidad inicial (m/s):")
velocidad_label.pack()
velocidad_entry = tk.Entry(ventana_tk)
velocidad_entry.pack()

area_label = tk.Label(ventana_tk, text="Área de explosión (metros):")
area_label.pack()
area_entry = tk.Entry(ventana_tk)
area_entry.pack()

velocidad_piloto_label = tk.Label(ventana_tk, text="Velocidad del piloto (m/s):")
velocidad_piloto_label.pack()
velocidad_piloto_entry = tk.Entry(ventana_tk)
velocidad_piloto_entry.pack()

calcular_button = tk.Button(ventana_tk, text="Calcular", command=calcular)
calcular_button.pack()

simular_button = tk.Button(ventana_tk, text="Simular", command=simular)
simular_button.pack()

resultado_label = tk.Label(ventana_tk, text="")
resultado_label.pack()

ventana_tk.mainloop()

