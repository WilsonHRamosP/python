# 📄 Proyecto: Clase `Persona` en Python

Este proyecto es un ejemplo básico en Python que demuestra cómo crear una clase con atributos y métodos, así como su uso desde una función principal. Ideal para quienes están comenzando en la programación orientada a objetos.

---

## 🧱 Estructura del Proyecto

```
/mi_proyecto_persona
│
├── persona.py          # Contiene la definición de la clase Persona
└── main.py             # Crea objetos de la clase y llama a sus métodos
```

---

## 📌 Objetivo

- Aprender a definir una clase en Python.
- Crear un constructor (`__init__`) con atributos.
- Definir métodos que interactúan con los atributos del objeto.
- Usar una clase desde otra parte del programa (función `main`).

---

## 🧠 Descripción de la Clase `Persona`

```python
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años")

    def saludar2(self):
        print(f"Buenos días {self.apellido} {self.nombre}, tienes {self.edad} años")

    def mostrar_edad(self):
        print(f"Tengo {self.edad} años")
```

### Atributos
- `nombre`: nombre de la persona.
- `apellido`: apellido de la persona.
- `edad`: edad en años.

### Métodos
- `saludar()`: imprime un saludo informal.
- `saludar2()`: imprime un saludo más formal.
- `mostrar_edad()`: imprime la edad.

---

## 🛠️ Cómo Ejecutar

1. Asegúrate de tener Python instalado.
2. Guarda los archivos `persona.py` y `main.py` en la misma carpeta.
3. Ejecuta el archivo `main.py` desde la terminal:

```bash
python main.py
```

---

## 💡 Ejemplo de Salida

```
Hola soy Wilson Ramos y tengo 32 años
Buenos días Ramos Wilson, tienes 32 años
```

---

## ✅ Requisitos

- Python 3.x

---

## 🧑‍💻 Autor

Wilson Herley Ramos Parrado