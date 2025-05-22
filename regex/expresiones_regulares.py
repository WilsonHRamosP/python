#expresiones regulares 
'''las expresiones regulares permiten buscar patrones en cadenas de texto,
para ello se utiliza la libreria re (regular expression) validación de datos,
busqueda de cadenas de texto, entre otras cosas'''

'''Por que aprender Regex
- Validación de datos
- Busqueda de cadenas de texto
- Reemplazo de cadenas de texto
- Manipulación de cadenas de texto
- Extracción de cadenas de texto'''
#importamos la libreria
import re
#"crear un patron"
pattern = "Hola"
texto = "Hola mundo developer"
result = re.search(pattern, texto) #buscamos el patron 

if result:
    print("Patron encontrado en el texto")
else:
    print("Patron no encontrado en el texto")

#.group() para extraer el patron
print(result.group())

#.start() y .end() para obtener la posicion del patron
print(result.start())
print(result.end())

#Ejercicio 1
#Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto:
#Indica en que posicion se encuentra la palabra "IA" coincidencia.
text = ("Todo el mundo dice que la IA nos va a quitar el trabajo." 
"pero solo hace falta aprender a trabajar con la IA.")
pattern = "IA"
found_ia = re.search(pattern, text)
if found_ia:
    print(f"La palabra {pattern} se encuentra en la posición: {found_ia.start()}, "
          f" y termina en la posición {found_ia.end()}")
else:
    print(F"La palabra {pattern} en el texto no se encuentra en el texto.")

#Ejercicio 2
#Encuentra todas las ocurrencias de la palabra "IA" en el siguiente texto:
#Indica en que posicion se encuentra la palabra "IA" coincidencia.
#.findarall() devuelve una lista con todas las coincidencias en el texto


text = ("Todo el mundo dice que la IA nos va a quitar el trabajo." 
"pero solo hace falta aprender a trabajar con la IA."
"por ahora la IA puede ayudarnos a programar.")
pattern = "IA"
matches = re.findall(pattern, text)
print(matches)
print(len(matches))

#metodo iter
text = ("Todo el mundo dice que la iA nos va a quitar el trabajo." 
"pero solo hace falta aprender a trabajar con la Ia."
"por ahora la IA puede ayudarnos a programar.")
pattern = "IA" #buscar cualquier caracter
matches = re.finditer(pattern, text, re.IGNORECASE)
for match in matches:
    print(match.group(), match.start(), match.end())