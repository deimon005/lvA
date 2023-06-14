import math
#empezare definiendo las contantes y variables que necesitamos a la hora de calcular un lanzamiento vertical hacia abajo
#------------------------------------------------------------------------------------------
#altura inciial debe proporcionarse en metros
#siento que deberiamos hacer que altura inicial sea una variable input que el usuario puede ingresar e ir desarrollando su problema y que nuestro codigo le de respuesta
altura_inicial = float(input('ingrese la altura incial desde la cual se este efectuando el lanzamiento vertical hacia abajo(en metros)'))
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#velocidad incial es la velocidad con la que empieza a caer el objeto y se calcula en m/s^2
velocidad_inicial = float(input('ingrese la velocidad inicial del lanzamiento vertical hacia abajo(en m/s^2)'))
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#la aceleracion por gravedad en este caso es de 9,8 m/s^2
aceleracion_debido_a_gravedad = 9.8
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#el tiempo que tarda en llegar al suelo
#se calcula utilizando una formula que utiliza los datos ingresados anteriormente y la libreria math que nos permite realizar calculos matematicos un poco mas complejo
tiempo_de_vuelo = math.sqrt((2 * (altura_inicial / aceleracion_debido_a_gravedad)))
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#la veocidad final es la velocidad del objeto antes de tocar el piso
velocidad_final = velocidad_inicial + (aceleracion_debido_a_gravedad * tiempo_de_vuelo)
#------------------------------------------------------------------------------------------
#{:.2f} esto indicq que el valor se mostrara con 2 digitos despues de el punto
print("tiempo de vuelo : {:.2f} segundos".format(tiempo_de_vuelo))
print('la velocidad final alcanzada por el objeto es: {:.2f} m/s^2'.format(velocidad_final))

#wena cabros