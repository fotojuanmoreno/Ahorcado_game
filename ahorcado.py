import random
import string
import errores as muerto


la_palabra = ""
palabra_visual = ""
contador = 0
letras = 3
letras_escogidas = []
errores = 0

def escoge_palabra():
	global palabra_visual
	global la_palabra
	global letras
	#Recoge las distntas palabras que pueden aparecer en el juego:
	palabras = open("recursos.txt", mode = "r", encoding = "utf-8")
	p = palabras.read().split()
	palabras.close()

	#Elegimos una palabra para jugar con ella:
	la_palabra = random.choice(p).upper()

	#print(la_palabra)

	letras = len(la_palabra)

	#Ocultamos la palabra
	
	letra_oculta = " _"

	for l in la_palabra:
		palabra_visual = palabra_visual + letra_oculta
	print(palabra_visual)

def recoge_letra():
	global la_palabra
	global palabra_visual
	global letras
	global contador
	global letras_escogidas
	global errores
	global error_inicio

	letra = input("\nIntroduce una letra: \n").upper()

	if letra == "A":
		letras_escogidas.append("Á")
	elif letra == "E":
		letras_escogidas.append("É")
	elif letra == "I":
		letras_escogidas.append("Í")
	elif letra == "O":
		letras_escogidas.append("Ó")
	elif letra == "U":
		letras_escogidas.append("Ú")
		letras_escogidas.append("Ü")

	letras_escogidas.append(letra)
	print("\nletras escogidas: \n" + str(letras_escogidas))

	palabra_visual = ""
	contador = 0

	for l in la_palabra:
		if l in letras_escogidas:
			indice = letras_escogidas.index(l)
			letra_oculta = " " + letras_escogidas[indice]
			contador = contador + 1
		else:
			letra_oculta = " _"
		palabra_visual = palabra_visual + letra_oculta	

	

	if letra in la_palabra:
		pass
	else:
		errores = errores + 1
		print("\nErrores: " + str(errores) + "\n")

	if errores == 1:
		print(muerto.error_uno)
	elif errores == 2:
		print(muerto.error_dos)
	elif errores == 3:
		print(muerto.error_tres)
	elif errores == 4:
		print(muerto.error_cuatro)
	elif errores == 5:
		print(muerto.error_cinco)
	elif errores == 6:
		print(muerto.error_seis)
	print("\n" + palabra_visual + "\n")

def eljuego():
	print(muerto.error_inicio + "\n")
	#print("##############\n")
	print("Aquí esta tu palabra a resolver: \n")
	
	escoge_palabra()
	while contador < letras and errores < 6:
		recoge_letra()
	if contador == letras:
		print("\n¡¡Ole tú!!\n Has ganado al acertar la palabara " + la_palabra)
	elif errores > 5:
		print("Vaya...\nParece que has perdido. Otra vez será.\nLa pablabra era: " + la_palabra)
	print("¿Quieres jugar otra vez?")
	repetir = input("y/n: ")
	repetir = repetir.lower()
	if repetir == "n":
		print("Hasta la próxima. ¿Debería de poner un contador?")
	else:
		la_palabra = ""
		la_palabra = ""
		palabra_visual = ""
		contador = 0
		letras = 3
		letras_escogidas = []
		errores = 0
		eljuego()

def main():
	print("    ############\n")
	print("      AHORCADO")
	eljuego()



if __name__ == '__main__':
	main()

