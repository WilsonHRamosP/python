# Fecha y hora en español
import locale
from datetime import datetime

# Establecer la configuración regional a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Obtener la fecha y hora actual

ahora = datetime.now()

# Formatear la fecha y hora en español
print(ahora.strftime("%A, %d de %B de %Y"))

# Determinar si es AM o PM
indicador = "AM" if ahora.hour < 12 else "PM"

# Obtener la fecha y hora actual
ahora = datetime.now()

# Determinar si es AM o PM
indicador = "AM" if ahora.hour < 12 else "PM"

# Formatear la fecha y hora
formato = ahora.strftime("Fecha: %d de %B de %Y. \nHora: %I:%M")

# Imprimir la fecha y hora con el indicador AM/PM
print(f"{formato} {indicador}")


