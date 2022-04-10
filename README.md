# twitter_bot

El objetivo de este programa fue lograr un simulador de usuarios en twitter combinando datos reales, modelos matem ́aticos, procesamiento del lenguaje y programaci ́on para generar un bot (i.e., un programa) que pueda aprender e imitar la forma de construir frases (i.e., tweets) de una cuenta determinada.

# Intro
Él programa comienza con él archivo "Downloader.py", utiliza la librería "Twint" para acceder a los tweets de una cuenta. Para ejecutar el bot será necesario modificar algunas variables de configuración en la función "main()" actualmente vacias y comentadas ("username", que debe tener el handle de la cuenta (sin el @); y "limit", que establece el número máximo de tweets a bajar (máximo 3200)).
Los resultados se guardan en un archivo cuyo nombre es el handle de la cuenta, y la extensión que le asignamos es ".data."
El formato del archivo es el usado por twint, y es relativamente simple. Hay un tweet por línea del archivo, y cada tweet está representado con un formato json para incorporar la distinta información asociada al tweet. 
La librería twint extrae distintos metadatos para cada tweet, más allá del texto y el usuario.

# Extracción de los datos
