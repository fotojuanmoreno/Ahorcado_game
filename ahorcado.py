import random
#import errores


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

	letra = input("Introduce una letra: \n").upper()
	
	letras_escogidas.append(letra)
	print("letras escogidas: " + str(letras_escogidas))

	palabra_visual = ""
	contador = 0

	for l in la_palabra:
		if l in letras_escogidas:
			indice = letras_escogidas.index(l)
			letra_oculta = letras_escogidas[indice]
			contador = contador + 1
		else:
			letra_oculta = " _"
		palabra_visual = palabra_visual + letra_oculta	

	print(palabra_visual)

	if letra in la_palabra:
		pass
	else:
		errores = errores + 1
		print("Errores: " + str(errores))





def main():
	print("##############")
	print("  AHORCADO")
	print("##############\n")
	print("Aquí esta tu palabra a resolver: \n")
	escoge_palabra()
	while contador < letras:
		recoge_letra()

if __name__ == '__main__':
	main()

