from nltk.tokenize import TweetTokenizer
import pickle
import networkx as nx
import random
import matplotlib.pyplot as plt

BEG = '__beg__ __beg__'
END = '__end__ __end__'

def process_tweets(tweets_filename):
	# Toma los textos del archivo con los tweets procesados, y devuelve una lista de lista de strings
	# con los tweets tokenizados.
	# La posicion i de la lista principal corresponde al tweet i del archivo de entrada tokenizado.
	tweets = open(tweets_filename, "r")
	lectura = tweets.readlines()
	tweets.close()

	tknzr = TweetTokenizer()
	lista = []
	# Iteramos por cada tweet del texto
	for elem in lectura:
		# Eliminamos el salto "\n" = a un salto de linea
		clean_elem = elem.strip("\n")
		# Añadimos las aperturas y cierres del tweet requeridas para la cadena de Markowitz
		tweet_final = BEG + " " + clean_elem + " " + END
		tokens = tknzr.tokenize(tweet_final)
		# Añadimos el tweet tokenizado a la lista vacia, esto es, una lista de strings, cada palabra es una posicion
		lista.append(tokens)

	lista_de_listas = []
	#Iteramos primero por cada tweet tokenizado de la lista creada arriba
	for tweet_token in lista:
		lista_de_tuplas = []
		# Para luego poder iterar por cada posicion = token del tweet y generar una lista de tuplas = nodos del futuro digrafo
		for i in range(len(tweet_token) - 1):
			v = tweet_token[i]
			w = tweet_token[i + 1]
			lista_de_tuplas.append((v,w))
		# Añadimos la lista de tuplas a una lista que contenga a todos los tweets
		lista_de_listas.append(lista_de_tuplas)

	return lista_de_listas

def add_text_to_digraph(text, D):
	# Agrega un determinado texto tokenizado al grafo, actualizando correctamente los pesos del mismo.
	# Notar que algunos ejes ya podrian estar definidos de tweets anteriores.
	# Los pesos deben ser la cantidad de apariciones del correspondiente eje (bigrama)
	# Los cambios se aplican directamente sobre D.
	# Funcion explicada en el informe...
	for i in range(len(text) - 1):
		v = text[i]
		w = text[i + 1]
		if D.has_edge(v,w):
			D[v][w]["weight"] += 1
		else:
			D.add_edge(v,w, weight = 1)
			

def generate_graph(tknzd_text):
	# Funcion general encargada de armar la primera version del grafo.
	# Llama a la funcion auxiliar add_text_to_digraph.
	# Creamos el digrafo
	# Iteramos por cada tweet de la lista de listas de tuplas "tknzd_text" para hacer el llamado a la funcion auxiliar en cada caso
	D = nx.DiGraph()
	for tweet_token in tknzd_text:
		add_text_to_digraph(tweet_token, D)

	# Retornamos el grafo completo
	return D
		
	#print(D.nodes)
	#print(D.edges)

def adjust_out_edges_weight(D,v):
	# Funcion que se encarga de convertir los pesos de los ejes salientes de v en frecuencias.
	# Trabaja directamente sobre el grafo D.
	# Creamos la variable suma para poder guardar la suma total de pesos por cada nodo, denominador en el calculo de frecuencias
	suma = 0

	# Recorremos todos los sucesores del nodo "v", sumando su peso a la variable suma
	for i in D.successors(v):
		suma = D[v][i]["weight"] + suma

	# Recorremos nuevamente los sucesores del nodo "v" para actualizar su peso y convertirlo en probabilidad, hicimos esto calculando la frecuencia del peso sobre la suma total de pesos del nodo
	for i in D.successors(v):
		D[v][i]["weight"] = D[v][i]["weight"] / suma


def calculate_markov_chain(D):
	# Iteramos sobre cada nodo para convertir los pesos de los vertices en probabilidades, llamando a la funcion auxiliar "adjust_out_edges_weight"
	for v in D.nodes:
		adjust_out_edges_weight(D,v)


def main():

	# input user
	username = # ''
	tweets_filename = username + '.tweets.txt'

	# Process tweets
	# Usamos como parametro el archivo .txt generado en el script "data_extractor.py"
	tknzd_text = process_tweets(tweets_filename)
	
	# Generate weighted graph
	D = generate_graph(tknzd_text)
	
	# Convert edges weights to probabilities.
	calculate_markov_chain(D)

	# Some debug info
	print('Graph statistics:', D.number_of_nodes(), D.number_of_edges())

	# persist the digraph.
	graph_file = username + '.gml'
	#nx.write_gml(D, graph_file)
	# si se utilizan tuplas como nodos, usar la siguiente linea
	# actualizar convenientemente en bot.py
	nx.write_gpickle(D, graph_file)

if __name__ == '__main__':
	main()