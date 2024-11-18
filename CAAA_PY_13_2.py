import tkinter as tk
from math import sqrt

# Función para manejar las operaciones
def agregar(valor):
    contenido = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, contenido + str(valor))

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def cambiar_signo():
    try:
        contenido = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(-contenido))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def porcentaje():
    try:
        contenido = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(contenido / 100))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def raiz_cuadrada():
    try:
        contenido = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(sqrt(contenido)))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def inverso():
    try:
        contenido = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(1 / contenido))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora Científica")
root.geometry("400x500")

# Pantalla de entrada
entrada = tk.Entry(root, font=("Arial", 18), justify="right")
entrada.place(x=10, y=50, width=380, height=40)

# Botones
botones = [
    ("MC", 10, 100), ("MR", 80, 100), ("MS", 150, 100), ("M+", 220, 100), ("sqr", 290, 100),
    ("7", 10, 160), ("8", 80, 160), ("9", 150, 160), ("+/-", 220, 160), ("%", 290, 160),
    ("4", 10, 220), ("5", 80, 220), ("6", 150, 220), ("*", 220, 220), ("1/x", 290, 220),
    ("1", 10, 280), ("2", 80, 280), ("3", 150, 280), ("-", 220, 280), ("=", 290, 280),
    ("0", 10, 340), (".", 80, 340), ("+", 150, 340)
]

# Funciones de los botones
funciones = {
    "MC": limpiar,
    "MR": lambda: None,  # Implementar funcionalidad de memoria si se desea
    "MS": lambda: None,  # Implementar funcionalidad de memoria si se desea
    "M+": lambda: None,  # Implementar funcionalidad de memoria si se desea
    "sqr": raiz_cuadrada,
    "+/-": cambiar_signo,
    "%": porcentaje,
    "1/x": inverso,
    "=": calcular
}

# Crear botones
for texto, x, y in botones:
    if texto in funciones:
        accion = funciones[texto]
    else:
        accion = lambda t=texto: agregar(t)
    boton = tk.Button(root, text=texto, width=5, height=2, command=accion)
    boton.place(x=x, y=y, width=60, height=50)

# Ejecutar la aplicación
root.mainloop()