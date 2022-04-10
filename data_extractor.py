import json

def extract_tweets_text(input_file, input_file_2, output_file):
	# 1. Abre el archivo input_file como lectura y output_file como escritura.
	# Repetimos el proceso de apertura de archivos ya que decidimos utilizar dos usuarios distintos, por lo que tambien modificamos la cantidad de parametros en la funcion.
	apertura = open(input_file, "r")
	
	# La variable "lectura" contiene todos los tweets en formato de string
	lectura = apertura.readlines()
	apertura.close()

	# 2. Para cada linea, genera el json usando json.loads.
	# Iteramos sobre cada tweet para generar un json y poder añadirlo a la lista vacia "lista_json"
	lista_json = []
	for twit in lectura:
		nuevo_json = json.loads(twit)
		lista_json.append(nuevo_json)

	apertura_2 = open(input_file_2, "r")

	lectura_2 = apertura_2.readlines()
	apertura_2.close()

	lista_json_2 = []
	for twit in lectura_2:
		nuevo_json = json.loads(twit)
		lista_json_2.append(nuevo_json)

	# Abrimos un unico archivo "write" sobre el que incluiremos los 6400 tweets
	escritura = open(output_file, "w")
	
	# Usamos el formato json para poder corroborar que el tweet sea efectivamente un tweet y no un retweet, accediendo a esa clave y viendo su valor booleano
	for twit in lista_json:
		# 3. Si el archivo no es un retweet, entonces guardamos el texto en el archivo de output en una nueva linea.
		if twit["retweet"] != True:
			texto = twit["tweet"]
			escritura.write(texto)
			escritura.write("\n")

	for twit in lista_json_2:
		if twit["retweet"] != True:
			texto = twit["tweet"]
			escritura.write(texto)
			escritura.write("\n")

	escritura.close()


def main():

	# input user
	username = # ''
	filename = username + '.data'
	limit = 3200

	username_2 = # ""
	filename_2 = username_2 + ".data"


	# Extract tweets from raw data
	tweets_filename = username + "&" + username_2 + '.tweets.txt'
	extract_tweets_text(filename, filename_2, tweets_filename)



if __name__ == '__main__':
	main()