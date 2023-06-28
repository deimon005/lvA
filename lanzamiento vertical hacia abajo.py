import tkinter as tk                        # Importar la biblioteca tkinter con el alias 'tk'
import pygame                               # Importar la biblioteca pygame
from pygame.locals import *                 # Importar todos los nombres definidos en el módulo locals de pygame

# Dimensiones de la ventana de Pygame
ANCHO = 1500                                # Variable que almacena el valor de ancho de nuestra gráfica en 1500 píxeles
ALTO = 1000                                 # Variable que almacena el valor de alto de nuestra gráfica en 1000 píxeles

PIXELES_POR_METRO = 1                       # Pixeles Equivalentes al Metro


def calcular():
    # Variables para el cálculo
    altura_inicial = float(altura_entry.get())                             # Obtener el valor de altura inicial del formulario y convertirlo a tipo float
    velocidad_inicial = float(velocidad_entry.get())                       # Obtener el valor de velocidad inicial del formulario y convertirlo a tipo float
    area_explosion = float(area_entry.get())                               # Obtener el valor del área de explosión del formulario y convertirlo a tipo float
    velocidad_piloto = float(velocidad_piloto_entry.get())                 # Obtener el valor de la velocidad del piloto del formulario y convertirlo a tipo float

    tiempo_vuelo = (velocidad_inicial + (velocidad_inicial ** 2 + 2 * 9.8 * altura_inicial) ** 0.5) / 9.8                            # Calcular el tiempo de vuelo utilizando la fórmula de la caída libre

    tiempo_impacto = int(tiempo_vuelo)                                                                                               # Convertir el tiempo de vuelo a un entero
    velocidad_impacto = int(velocidad_inicial + 9.8 * tiempo_impacto)                                                                # Calcular la velocidad de impacto utilizando la fórmula de la velocidad final en caída libre

    # Verificar si el producto del tiempo de vuelo y la velocidad del piloto es menor que el área de explosión,
    # y actualizar el texto de la etiqueta de resultado en consecuencia
    if tiempo_impacto * velocidad_piloto < area_explosion:
        resultado_label.config(
            text=f"La bomba te dañó.\nVelocidad final: {velocidad_impacto} m/s\nTiempo de vuelo: {tiempo_impacto} s")
    else:
        resultado_label.config(
            text=f"La bomba no te dañó.\nVelocidad final: {velocidad_impacto} m/s\nTiempo de vuelo: {tiempo_impacto} s")




def simular():
    # Variables para la simulación
    altura_inicial = float(altura_entry.get())                            # Obtener el valor de altura inicial del formulario y convertirlo a tipo float
    velocidad_inicial = float(velocidad_entry.get())                      # Obtener el valor de velocidad inicial del formulario y convertirlo a tipo float
    area_explosion = float(area_entry.get())                              # Obtener el valor del área de explosión del formulario y convertirlo a tipo float
    velocidad_piloto = float(velocidad_piloto_entry.get())                # Obtener el valor de la velocidad del piloto del formulario y convertirlo a tipo float

    tiempo_vuelo = (velocidad_inicial + (velocidad_inicial ** 2 + 2 * 9.8 * altura_inicial) ** 0.5) / 9.8           # Calcular el tiempo de vuelo utilizando la fórmula de la caída libre

    tiempo_impacto = int(tiempo_vuelo)                                                                               # Convertir el tiempo de vuelo a un entero
    velocidad_impacto = int(velocidad_inicial + 9.8 * tiempo_impacto)                                                # Calcular la velocidad de impacto utilizando la fórmula de la velocidad final en caída libre


    pygame.init()                                                        # Inicializar el módulo pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))                     # Crear una ventana con las dimensiones ANCHO y ALTO
    pygame.display.set_caption("Simulación")                             # Establecer el título de la ventana como "Simulación"
    
   # Crear un rectángulo para representar el avión en la simulación, con una posición y tamaño específicos
    avion_rect = pygame.Rect(ANCHO // 2, ALTO - int(altura_inicial * PIXELES_POR_METRO), 50 * PIXELES_POR_METRO, 20 * PIXELES_POR_METRO)
   # Crear un rectángulo para representar la bomba en la simulación, con una posición y tamaño específicos
    bomba_rect = pygame.Rect(avion_rect.centerx - 10 * PIXELES_POR_METRO, avion_rect.bottom, 20 * PIXELES_POR_METRO, 20 * PIXELES_POR_METRO)
   
    explosion_rect = None                                            # Inicializar el rectángulo de la explosión como None (sin explosión en este punto)

    reloj = pygame.time.Clock()                                      # Crear un objeto Clock para controlar la velocidad de la simulación

    tiempo_transcurrido = 0                                          # Inicializar el tiempo transcurrido en la simulación como 0

    while tiempo_transcurrido <= tiempo_vuelo:         # Bucle principal de la simulación que se ejecuta mientras el tiempo transcurrido sea menor o igual al tiempo de vuelo
        for event in pygame.event.get():               # Iterar sobre los eventos de pygame que han ocurrido
    # Si se detecta un evento de cierre de ventana (QUIT), se cierra pygame y se termina la simulación
            if event.type == QUIT:
                pygame.quit()
                return

        ventana.fill((255, 255, 255))                # Rellenar la ventana con el color RGB: 255, 255, 255

        # Mover el avión hacia la derecha según la velocidad del piloto
        avion_rect.x += int(velocidad_piloto * PIXELES_POR_METRO)

        # Calcular la posición vertical de la bomba en función del tiempo
        tiempo_transcurrido += reloj.tick(
            60) / 1000  # Obtener el tiempo transcurrido desde el último fotograma en segundos
        bomba_rect.y = avion_rect.bottom + int((tiempo_transcurrido / tiempo_vuelo) * altura_inicial * PIXELES_POR_METRO)   # Calcular la posición vertical de la bomba en función del tiempo transcurrido y la altura inicial

        # Verificar si la bomba ha alcanzado el suelo
        if tiempo_transcurrido >= tiempo_vuelo:            # Verificar si ha pasado el tiempo de vuelo completo
            if explosion_rect is None:                      # Verificar si el rectángulo de la explosión es None (no ha sido creado todavía)
        # Crear un rectángulo para representar la explosión, con una posición y tamaño basados en el área de explosión
                explosion_rect = pygame.Rect(bomba_rect.x - int(area_explosion * PIXELES_POR_METRO) // 2, bomba_rect.y - int(area_explosion * PIXELES_POR_METRO), int(area_explosion * PIXELES_POR_METRO),
                                             int(area_explosion * PIXELES_POR_METRO))
        # Si el rectángulo de la explosión colisiona con el rectángulo del avión, mostrar el mensaje de daño        
                if explosion_rect.colliderect(avion_rect):
                    resultado_label.config(text="La bomba te dañó.")
         # Si no hay colisión, mostrar el mensaje de que no hay daño            
                else:
                    resultado_label.config(text="La bomba no te dañó.")
            
            else:
                if explosion_rect.width < int(area_explosion * PIXELES_POR_METRO):       # Si el ancho del rectángulo de la explosión es menor que el área de explosión objetivo,
                    explosion_rect.inflate_ip(1, 1)                                      # inflar el rectángulo en incrementos de 1 píxel para simular una explosión en crecimiento

        # Dibujar los elementos en la ventana
        pygame.draw.rect(ventana, (0, 0, 255), avion_rect)                        # Dibujar un rectángulo en la ventana para representar el avión, con el color RGB: 0, 0, 255
        pygame.draw.rect(ventana, (255, 0, 0), bomba_rect)                        # Dibujar un rectángulo en la ventana para representar la bomba, con el color RGB: 255, 0, 0
        
        # Si el rectángulo de la explosión existe, dibujar un rectángulo en la ventana para representar la explosión,
         # con el color RGB: 255, 255, 0
        if explosion_rect:
            pygame.draw.rect(ventana, (255, 255, 0), explosion_rect)

        pygame.display.flip()                                                     # Actualizar la pantalla mostrando todos los elementos dibujados


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


