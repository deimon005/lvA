import math
import matplotlib.pyplot as plt
# primero definimos las librerias que ocuparemos
#---------------------------------------------------------------------------------------------------------------------------------------------
# Creamos una variable en la cual ingresemos la altura de nuestra problematica
#---------------------------------------------------------------------------------------------------------------------------------------------
altura_inicial = float(input('Ingrese la altura inicial desde la cual se esta efectuando el lanzamiento vertical hacia abajo (en metros): '))
#---------------------------------------------------------------------------------------------------------------------------------------------
# Creamos una variable en la cual ingresemos la velocidad de nuestra problematica
#---------------------------------------------------------------------------------------------------------------------------------------------
velocidad_inicial = float(input('Ingrese la velocidad inicial del lanzamiento vertical hacia abajo (en m/s^2): '))
#---------------------------------------------------------------------------------------------------------------------------------------------
# Creamos variable que es = a la gravedad 9,8 m/s^2
#---------------------------------------------------------------------------------------------------------------------------------------------
aceleracion_debido_a_gravedad = 9.8  # Aceleracion debida a la gravedad en m/s^2
#---------------------------------------------------------------------------------------------------------------------------------------------
# Tiempo de vuelo calculado utilizando la formula y la biblioteca math
#---------------------------------------------------------------------------------------------------------------------------------------------
tiempo_de_vuelo = math.sqrt((2 * (altura_inicial / aceleracion_debido_a_gravedad)))
#---------------------------------------------------------------------------------------------------------------------------------------------
# Velocidad final alcanzada por el objeto antes de tocar el piso
#---------------------------------------------------------------------------------------------------------------------------------------------
velocidad_final = velocidad_inicial + (aceleracion_debido_a_gravedad * tiempo_de_vuelo)

print("Tiempo de vuelo: {:.2f} segundos".format(tiempo_de_vuelo))
print('La velocidad final alcanzada por el objeto es: {:.2f} m/s^2'.format(velocidad_final))

# Generar los datos para el grafico
t = [i / 100 for i in range(int(tiempo_de_vuelo * 100) + 1)]  # Intervalo de tiempo en incrementos de 0.01 segundos
y = [altura_inicial - (0.5 * aceleracion_debido_a_gravedad * tiem ** 2) for tiem in t]  # Altura en funcion del tiempo
# Graficar los datos
plt.plot(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.title('Lanzamiento vertical hacia abajo')
plt.grid(True)
plt.show()
