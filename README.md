# Proyecto INFO 1120 - FIS 1102
Participantes del Proyecto : Demian Quezada, Fernando Prieto, Benjamin Parra, Ricardo Rios. 
#
Carrera Perteneciente: Ing. Civil Informática.        
#
Materias Involucradas : Fisica , Programación I 

# Descripción 
Muy buenas profesor y profesora, esperando que se encuentre bien, queremos hacer presentación de nuestro proyecto final.
Teniendo esta oportunidad para que explayemos lo realizado frente a los desafíos y soluciones a las cual nos hemos enfrentado, implementando desarrollos en el código y nuestra problemática.
Discutiremos los beneficios y dificultades que hemos tenido hasta este momento a través de nuestra organización y tiempo implicado. 

# Evento Físico a Simular 
Lanzamiento vertical hacia abajo. 

# Breve Historia
El lanzamiento vertical hacia abajo es un concepto utilizado en física y describe el movimiento de objetos que se inician desde una altura específica.

Cuando el objeto se arroja verticalmente hacia abajo, se expone solo a la gravedad de activación. En este tipo de lanzamiento, una vez realizado el único poder que actúa sobre el objeto es la gravedad. Esto se debe a que se considera que no tiene resistencia al aire u otra fuerza externa importante.

Al comienzo del arranque, el objeto 'tiene' velocidad inicial en la dirección vertical. Si el objeto cae debido a la gravedad, la velocidad aumentará constantemente. La aceleración experimentada por el objeto es la aceleración debido a la gravedad, y es de aproximadamente 9.8 metros partido por segundos al cuadrado (9.8 m/s^2) en la tierra. Esta aceleración permanece constante a través del lanzamiento.


# Aplicaciones
La simulación de este evento físico puede tener aplicaciones en el ámbito militar, de defensa, destruccion, espacial ,etc. permitiendo evaluar la efectividad de diferentes estrategias y planificar operaciones de mejor rendimiento en x proyecto.


# Siendo Nuestra Problemática la Siguiente

Digamos que un equipo táctico estadounidense quiere acabar con la base de operaciones militares norcoreanas en mitad de una disputa, utilizando una bomba que será lanzada desde un avión de combate de forma vertical hacia abajo a una velocidad de 5m/s esto con un sistema de muelles y resortes desde una altura estimada de aproximadamente una 200m con dirección a la base de operaciones, la bomba tiene unas características propias, estás siendo que la bomba tiene un radio de explosion de 20 metros y una onda expansiva de 50 metros desde el origen de la explosion.
Las formulas que ocuparemos son 2: 
+ Tiempo de vuelo (t): t = (√(2h/g))
+ Velocidad final (vf): vf = v₀ + gt.

Ellos quieren saber con claridad el tiempo en que llegará esta bomba al objetivo, a través de la velocidad en la cual caerá este objeto, para de esta formas saber cuanto debe de ser la velocidad mínima con la cual deben de alejarse del origen de la explosion y asi no ser afectados por esta misma

# Ejemplo matemático

Supongamos que dejamos caer una bomba desde lo alto de un edificio de 50 metros de altura. Queremos calcular el tiempo que tardará en llegar al suelo y la velocidad con la que llegará.

Establecer los datos:

Altura inicial (h0): 50 metros
Aceleración debido a la gravedad (g): 9.8 m/s² (tomamos el valor estándar)
Velocidad inicial (v0): 2 m/s (la bomba se lanzara con una velocidad de 2m/s)
Calcular el tiempo de caída:
Utilizaremos la siguiente fórmula de la cinemática:
h = h0 - v0 * t - 0.5 * g * t²

Dado que la altura final (h) es 0 (la bomba llega al suelo), podemos reescribir la fórmula como:
0 = 50 - 2 * t - 0.5 * 9.8 * t²

Simplificando la ecuación, obtenemos:
4.9 * t² = 50

Resolviendo para t, dividimos ambos lados de la ecuación por 4.9:
t² = 10

Tomando la raíz cuadrada de ambos lados, obtenemos:
t ≈ √10 ≈ 3.16 segundos

Por lo tanto, el tiempo que tarda la bomba en caer es de aproximadamente 3.16 segundos.

Calcular la velocidad final:
Utilizaremos la siguiente fórmula de la cinemática:
v = v0 + g * t

Dado que v0 es 2 (la bomba se lanza con una velocidad de 2m/s), podemos reescribir la fórmula como:
v = 2 + 9.8 * 3.16

Calculando el resultado, obtenemos:
v ≈ 32.96 m/s

Por lo tanto, la velocidad con la que la bomba llega al suelo es aproximadamente 32.96 m/s.

En resumen, la bomba tarda aproximadamente 3.16 segundos en caer y llega al suelo con una velocidad de aproximadamente 32.96 m/s en un lanzamiento vertical hacia abajo desde un edificio de 50 metros de altura.

# Para Desarrollar la Simulación de la Operación, se Utilizaran las Siguientes Herramientas de Programación
Usamos el lenguaje de programacion Python 3.11.4, el intérprete del lenguaje fue Pycharm - Visual studio code y también utilizamos GitHub Desktop para el trabajo en grupo.

Las Librerias que Utilizamos son: 

+ PyGames : biblioteca de Python que se utiliza para desarrollar videojuegos y aplicaciones multimedia interactivas. Proporciona herramientas y funciones que permiten a los desarrolladores crear gráficos, animaciones, efectos de sonido y manejar la entrada del usuario.

+ Math : biblioteca incorporada en muchos lenguajes de programación que proporciona funciones y operaciones matemáticas avanzadas. Esta biblioteca permite realizar cálculos matemáticos más complejos que los operadores básicos que están disponibles de forma predeterminada. 

+ Tkinter : biblioteca de Python utilizada para crear interfaces gráficas de usuario (GUI, por sus siglas en inglés). Proporciona un conjunto de herramientas y widgets que permiten a los desarrolladores crear ventanas, botones, cajas de texto y otros elementos interactivos en sus aplicaciones.

Los programas y librerias que ocuparemos estaran dentro del siguiente link --> [programas](https://drive.google.com/drive/folders/1mwAAq_y6OmhLmySDE-CxzDlTXKNUx4OL?usp=sharing)

# Guía de Instalación de los Programas
Adjuntamos video en el siguiente link --> [Video Tutorial](https://youtu.be/GjodcyVgZAs)
# Video Explicación Fenómeno Físico
Adjuntamos video en el siguiente link --> [Video Explicación](https://youtu.be/IEs_uttm9g8)
