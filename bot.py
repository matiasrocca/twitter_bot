import networkx as nx
import random

# TO-DO: completar en función de la representacion asumida para los nodos del grafo (tuplas o string)
BEG = ("__beg__","__beg__")
END = ("__end__","__end__")

def get_next_word(bot, v):
	r = random.random()
	acum = 0.0

	for w in bot.successors(v):
		acum = acum + bot[v][w]['weight']
		if r <= acum:
			return w


def simulate_tweet(bot):
	word = BEG
	ret = word

	# Completar la simulacion. Debe terminar cuando la ultima palabra agregada es END

	# Utilizamos la funcion "while" dado que no tenemos un numero exacto de iteraciones, la condicion que establecimos es que continue añadiendo palabras hasta que la palabra que nos devuelva
	# la funcion auxiliar sea igual a la variable "END". Siempre que no lo sea, llamamos a la funcion auxiliar para obtener una nueva palabra
	# Esta nueva palabra la agregamos a una tupla de muchas posiciones, que representa un tweet
	while word != END:
		word = get_next_word(bot, word)
		ret = ret + word

	# Creamos un string vacio para poder emprolijar el tweet, dado que se encuentra en formato de tupla con muchas posiciones, las palabras estan repetidas, y los signos estan aislados
	tweet = ""
	# Iteramos sobre cada posicion de la tupla para ir añadiendo los strings a la cadena de strings
	for i in range(len(ret) -1):
		if tweet == "":
			tweet = ret[i]
		else:
			if ret[i] != ret[i-1]:
				if (ret[i] == "!") or (ret[i] =="¡") or (ret[i] == "¿") or (ret[i] == "?") or (ret[i] == ",") or (ret[i] == "."):
					tweet = tweet + ret[i]
				else:
					tweet = tweet + " " + ret[i]

	tweet = tweet.strip("__beg__")
	tweet = tweet.strip("__end__")

	# Retornamos el tweet generado.
	return tweet

def main():

	# input user
	username = # ''
	graph_file = username + '.gml'

	# read the digraph
	bot = nx.read_gpickle(graph_file)

	# simulate tweet
	tweet = simulate_tweet(bot)
	print(tweet)

if __name__ == '__main__':
	main()
