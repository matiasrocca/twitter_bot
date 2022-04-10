# twitter_bot

El objetivo de este programa fue lograr un simulador de usuarios en twitter combinando datos reales, modelos matemáticos, procesamiento del lenguaje y programación para generar un bot (i.e., un programa) que pueda aprender e imitar la forma de construir frases (i.e., tweets) de una o en este caso, dos cuentas determinadas.

Él bot que generemos intentará aprender en base al contenido generado por un usuario sus reglas de construcción de tweets en general, para luego generar de manera automatizada e independiente nuevos contenidos. Es importante destacar que los métodos aplicados en este trabajo han sido considerados estado del arte en la temática hasta hace algunos años, previo a la irrupción de métodos más sofisticados. Para construir el bot generador de tweets se implementa un Modelo de Lenguaje basado en n-grams y Modelos de Markov usando grafos y simulación.

# Intro
Él programa comienza con él archivo "Downloader.py", utiliza la librería "Twint" para acceder a los tweets de una cuenta. Para ejecutar el bot será necesario modificar algunas variables de configuración en la función "main()" actualmente vacias y comentadas ("username", que debe tener el handle de la cuenta (sin el @); y "limit", que establece el número máximo de tweets a bajar (máximo 3200)).
Los resultados se guardan en un archivo cuyo nombre es el handle de la cuenta, y la extensión que le asignamos es ".data."
El formato del archivo es el usado por twint, y es relativamente simple. Hay un tweet por línea del archivo, y cada tweet está representado con un formato json para incorporar la distinta información asociada al tweet. 
La librería twint extrae distintos metadatos para cada tweet, más allá del texto y el usuario.

# Extracción de los datos
Lo que el archivo "data_extractor.py" hace es, escencialmente, en base a un archivo de entrada, extraer el texto de cada tweet, guardándolo en un archivo nuevo con un tweet (pero ahora, solo texto) por línea. De esta forma, se evita tener el resto de la metadata obtenida por la librería.

# Armado e implementación del modelo
El procesamiento de los datos y el armado del modelo se realiza principalmente en el archivo "graph_generator.py.". Utiliza el paquete ".tokenize" del kit de herramientas de lenguaje natural de Python, el módulo de Python "Pickle", la librería "networkx" para la creación, manipulación y visualización de grafos y el módulo "pyplot" de la libreria "Matplotlib" para la visualización de los grafos en caso de así desearlo.

# Experimentación

Finalmente, él archivo "bot.py" es necesario para simular tweets utilizando el modelo construido. Este archivo lee el modelo exportado en formato ".gml" y simula un camino aleatorio usando la función "simulate_tweet()", dentro de este archivo vuelve a usarse a librería "networkx".

