#Como hacer peticiones a APIs con Python
#con y sin dependencias externas

#1 sin dependencias (Dificil
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"
try:
    # Realizar la solicitud a la API
    with urllib.request.urlopen(api_posts) as response:
        # Leer y decodificar la respuesta
        data = response.read().decode('utf-8')
        # Cargar los datos JSON
        json_data = json.loads(data)
        # Imprimir los datos JSON
        print(json_data)
except urllib.error.URLError as e:
    print(f"Error al acceder a la API: {e}")

import requests

api_posts = "https://jsonplaceholder.typicode.com/posts"

try:
    # Realizar la solicitud a la API
    response = requests.get(api_posts)
    # Verificar si la solicitud fue exitosa
    response.raise_for_status()
    # Cargar los datos JSON
    json_data = response.json()
    # Imprimir los datos JSON
    print(json_data)
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP al acceder a la API: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"Error al acceder a la API: {err}")

#metodos HTTP
#GET soliicitar informacion de un recurso especifico
'''Características:

Los parámetros se envían en la URL.

No debe modificar datos en el servidor.

Es seguro e idempotente (múltiples solicitudes tienen el mismo efecto).

Puede almacenarse en caché y guardarse en el historial del navegador.
'''
#POST  Envía datos al servidor para crear o modificar recursos.
'''Características:

Los datos se envían en el cuerpo de la solicitud.

Puede tener efectos secundarios, como crear múltiples entradas si se repite.

No se almacena en caché ni en el historial del navegador.

Adecuado para formularios o cargas de archivos.'''

#PUT Crear o reemplazar completamente un recurso en una ubicación específica del servidor.
'''Características:

Es idempotente: realizar la misma solicitud varias veces produce el mismo resultado.

Reemplaza por completo el recurso existente con los datos proporcionados.

Si el recurso no existe, puede ser creado en la ubicación especificada.

No se almacena en caché ni en el historial del navegador.'''

#DELETE Elimina un recurso en una ubicación especifica del servidor
'''Características:

Es idempotente: realizar la misma solicitud varias veces produce el mismo resultado.

Elimina el recurso existente en la ubicación especificada.

No se almacena en caché ni en el historial del navegador.

No puede ser revertido.
La respuesta puede variar según el servidor:

200 OK: Recurso eliminado exitosamente.

204 No Content: Recurso eliminado sin contenido adicional en la respuesta.

404 Not Found: El recurso no existe.'''

