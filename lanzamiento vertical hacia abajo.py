import tkinter as tk
import math


def calcular_lanzamiento():
    try:
        altura_inicial = float(altura_entry.get())
        velocidad_inicial = float(velocidad_entry.get())
        area_explosion = float(area_entry.get())
        velocidad_piloto = float(velocidad_piloto_entry.get())

        tiempo_impacto = math.sqrt((2 * altura_inicial) / 9.8)
        velocidad_impacto = velocidad_inicial + 9.8 * tiempo_impacto

        if velocidad_impacto < 0:
            resultado_label.config(text="La bomba no llega al suelo.")
        elif tiempo_impacto * velocidad_piloto < area_explosion:
            resultado_label.config(text="La bomba te alcanzó.")
        else:
            resultado_label.config(text="La bomba no te alcanzó.")

        velocidad_final_label.config(text=f"Velocidad final: {velocidad_impacto:.2f} m/s")
        tiempo_caida_label.config(text=f"Tiempo de caída: {tiempo_impacto:.2f} s")

    except ValueError:
        resultado_label.config(text="Ingrese valores numéricos válidos.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lanzamiento Vertical")

# Etiquetas y campos de entrada
altura_label = tk.Label(ventana, text="Altura inicial (metros):")
altura_label.pack()
altura_entry = tk.Entry(ventana)
altura_entry.pack()

velocidad_label = tk.Label(ventana, text="Velocidad inicial (m/s):")
velocidad_label.pack()
velocidad_entry = tk.Entry(ventana)
velocidad_entry.pack()

area_label = tk.Label(ventana, text="Área de explosión (metros):")
area_label.pack()
area_entry = tk.Entry(ventana)
area_entry.pack()

velocidad_piloto_label = tk.Label(ventana, text="Velocidad del piloto (m/s):")
velocidad_piloto_label.pack()
velocidad_piloto_entry = tk.Entry(ventana)
velocidad_piloto_entry.pack()

calcular_button = tk.Button(ventana, text="Calcular", command=calcular_lanzamiento)
calcular_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

velocidad_final_label = tk.Label(ventana, text="")
velocidad_final_label.pack()

tiempo_caida_label = tk.Label(ventana, text="")
tiempo_caida_label.pack()

ventana.mainloop()
