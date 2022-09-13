import random #Importamos la libreria random
#Asignacion de puntaje aleatorio dentro de un rango.
points = random.randint(1,11)

#COLOR
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'

#ESTILO
NORMAL = '\x1b[0;m'
YELLOWFONDO = '\033[1;33;43m'
WHITENEGRITA = '\x1b[1;37m'
WHITECURSIVA = '\033[3;37m'
GREENTACHADO = '\x1b[7;32m'

REDNEGRITA = '\x1b[1;31m'
BLUECURSIVA = '\033[3;34m'
GREENCURSIVA = '\033[3;32m'
YELLOWSUBRAYADO = '\033[4;33m'



# Bienvenida a la Trivia De Jujutsu Kaisen - ANIME
print(YELLOWFONDO + "✦✦✦  BIENVENIDO A MI TRIVIA DEL ANIME JUJUTSU KAIZEN  ✦✦✦\n" + NORMAL)
print(WHITECURSIVA + "Aqui pondras a prueba tus conocimientos con 10 PREGUNTAS del anime, yeih!!\n" )

#Preguntaremos su nombre
print("Mi nombre es Steffi-chan y te acompañare en esta travesia! \n " )
name = input( "Cuentame, ¿Como quieres que te llame?\n")
print("\nHi, %s." % name )
print("ENCANTADA DE CONOCERTE!! UWU")

# Es importante dar instrucciones sobre cómo jugar:
print( WHITENEGRITA +
"\nTe cuento %s," %name,"antes de iniciar la travesia de sabiduria,  necesitas saber esto... \n")

print(
    "Responder las siguientes preguntas escribiendo la letra de la alternativa en minuscula y presionando 'Enter' para enviar tu respuesta: \n" + NORMAL)

#Preguntamos los animos 
ready = input("¿Estas listo? Pon SI para avanzar --> ")

while ready not in ("yes", "si", "SI","Si", "YES"):
  ready = input("No quieres jugar? Dime que SI --> ")

print("\n EMPECEM000S!! ヽ (o ^ – ^ o) ノ")
print()

print ("INICIAS CON ", points," PUNTOS, VEAMOS CUANTOS PUNTOS CONSIGUES!")
print()
print()




# INICIO DE PREGUNTAS

# Pregunta 1
print(MAGENTA +"1) ¿Dónde se encuentra la escuela secundaria de Yuji Itadori? "+ RESET)
print(CYAN)
print("  a) Estudio conmigo")
print("  b) Kioto")
print("  c) Sugisawa")
print("  d) Seul")
print(RESET)


# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_1 == "c" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO +"Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 2
print(MAGENTA +"2) ¿Cómo se llama la extensión de dominio de Sukuna? " + NORMAL)
print(CYAN)
print("  a) La Rosa de Guadalupe nivel dios")
print("  b) Santuario malevólo")
print("  c) Reino demoniaco")
print("  d) Autoencarnacion bebito fiu fiu")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_2 == "b" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL )
  print()
  
# Pregunta 3
print(MAGENTA + "3) ¿Cuál es el apodo de Satoru Gojo? " + RESET)
print(CYAN)
print("  a) El chaman mas fuerte")
print("  b) El tigre de la universidad")
print("  c) El invencible")
print("  d) El hijo de Medusa")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_3 == "a" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 4
print(MAGENTA + "4) ¿A que se dedica Yoshinobu Gokuganji? " +RESET)
print(CYAN)
print("  a) Instructor del colegio de Tokio")
print("  b) Director del colegio de Kioto")
print("  c) Suplente de enfermeria")
print("  d) Sensei de Class Assassination")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_4"
respuesta_4 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_4 not in ("a", "b", "c", "d"):
  respuesta_4 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_4 == "b" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 5
print(MAGENTA +"5) ¿Quien no esta en segundo año? "+ RESET)
print(CYAN)
print("  a) Maki Zenin")
print("  b) Mikaela Yu")
print("  c) Aoi Todo")
print("  d) Yo, no pase de año")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_5"
respuesta_5 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_5 not in ("a", "b", "c", "d"):
  respuesta_5 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_5 == "c" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 6
print(MAGENTA +"6) ¿Cuántos dedos de Sukuna tiene en su poder Suguru Geto? "+ RESET)
print(CYAN)
print("  a) No se sabe, se esta esperando la segunda temporada")
print("  b) 5")
print("  c) No lei el manga")
print("  d) 6")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_6"
respuesta_6 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_6 not in ("a", "b", "c", "d"):
  respuesta_6 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_6 == "a" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 7
print(MAGENTA +"7) ¿Cómo se llama el padre de Megumi Fushiguro? "+ RESET)
print(CYAN)
print("  a) Tenemos el mismo padre")
print("  b) Alan Garcia")
print("  c) Tsumiki Fushiguro")
print("  d) Toji Fushiguro")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_7"
respuesta_7 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_7 not in ("a", "b", "c", "d"):
  respuesta_7 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_7 == "d" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 8
print(MAGENTA +"8) ¿Dónde solía vivir Nobara Kugisaki? "+ RESET)
print(CYAN)
print("  a) Era mi vecina del cerro")
print("  b) En el campo")
print("  c) En un departamento de 8x8")
print("  d) En Tokio")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_8"
respuesta_8 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_8 not in ("a", "b", "c", "d"):
  respuesta_8 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_8 == "b" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# Pregunta 9
print(MAGENTA +"9) ¿ Como se llama el espíritu maldito que tiene Itadori y que se comió para tenerlo? "+ RESET)
print(CYAN)
print("  a) Inuyasha - un dedo")
print("  b) Sukune - un chaufa")
print("  c) Tomoe - una serpiente")
print("  d) Sukuna - un dedo")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_9"
respuesta_9 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_9 not in ("a", "b", "c", "d"):
  respuesta_9 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_9 == "d" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
  # Pregunta 10
print(MAGENTA +"10) ¿ Que animales son los shikigamis de Megumi Fushiguro? "+ RESET)
print(CYAN)
print("  a) Winnie Pooh y Tiger")
print("  b) Lobos y zorros")
print("  c) Tucanes y cocodrilos")
print("  d) Perros y sapos")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_10"
respuesta_10 = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_10 not in ("a", "b", "c", "d"):
  respuesta_10 = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()

# Verificacion de respuesta correcta o incorrecta.
if respuesta_10 == "d" :
  suerte = random.randint(1,10)
  points += suerte
  print("Correcto %s" %name, "HAZ GANADO ", points," PUNTOS! 🌟 \n")
else:
  suerte = random.randint(1,10)
  points -= suerte
  print("UY! Incorrecto %s" %name ,"PERDISTE ", points," PUNTOS!  \n")
  print("Vamos a la siguiente! \n")

  #Conociendo tu puntaje
  print(GREENTACHADO + "Tu puntaje es:", points, "PUNTOS" + NORMAL)
  print()
  
# COMODIN
print("PREGUNTA COMODIN!! AQUI PUEDES RECUPERARTE SI TUVISTE UNA MALA RACHA \n")

#Inicia la pregunta
print(MAGENTA +" ------ Escoge un numero  ----- "+ RESET)
print(CYAN)
print("  a) Uno ")
print("  b) Dos")
print("  c) Tres")
print("  d) Cuatro")
print(RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_puntosExtras"
respuesta_puntosExtras = input("\nTu respuesta: ")

# Validacion de respuesta en general.
while respuesta_puntosExtras not in ("a", "b", "c", "d"):
  respuesta_puntosExtras = input("Uy! Debes colocar a,b,c,d. Ingresa nuevamente tu respuesta! --> ")
print()


if respuesta_puntosExtras == "a" :
  # Añadimos combo, el usuario da un numero.
  x = int(input("Dime un numero..."))
  points = points * int(x)
  print("%s" %name, "HAZ GANADO MUCHOS PUNTOS! 🌟 \n")
elif respuesta_puntosExtras == "b":
  # Añadimos combo, el usuario da un numero.
  x = int(input("Dime un numero..."))
  points = points - int(x)
  print("%s" %name, "PERDISTE PUNTOS! 🌟 \n")
elif respuesta_puntosExtras == "c":
  # Añadimos combo, el usuario da un numero.
  x = int(input("Dime un numero..."))
  points = points / int(x)
  print("%s" %name, "SE DIVIDIERON TUS PUNTOS PUNTOS! 🌟 \n")
else:
  # Añadimos combo, el usuario da un numero.
  x = int(input("Dime un numero..."))
  points = points * 100 * int(x)
  print("%s" %name, "HAZ GANADO UN MONTON DE PUNTOS! 🌟 \n")
  print("Vamos a la siguiente! \n")

#Despedida y muestra de puntaje total
print ("\n WHOUU GRACIAS %s," %name, "por jugar mi trivia, me diverti mucho contigo!! \n Y REBLOBLEEE DE TAMBORES (‘• ω • `) ♡")
print(GREENTACHADO +"GANASTE", points, "PUNTOS"+ NORMAL)
print()
print(YELLOWFONDO +"✦✦✦ FIN DE TRIVIA ✦✦✦")
print("✦✦✦ BYE ✦✦✦"+ NORMAL)