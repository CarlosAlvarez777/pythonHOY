import tkinter as tk

# Función para realizar operaciones
def calcular(operador):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            resultado = num1 / num2 if num2 != 0 else "Error"
        else:
            resultado = "Error"
        label_resultado.config(text=str(resultado))
    except ValueError:
        label_resultado.config(text="Error")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Operaciones Básicas")
root.geometry("400x300")

# Etiqueta de título
label_titulo = tk.Label(root, text="CALCULADORA OPERACIONES BÁSICAS", font=("Arial", 12, "bold"))
label_titulo.place(x=50, y=10)

# Etiqueta y entrada para número 1
label_num1 = tk.Label(root, text="Numero 1")
label_num1.place(x=50, y=50)
entry_num1 = tk.Entry(root)
entry_num1.place(x=50, y=80)

# Etiqueta y entrada para número 2
label_num2 = tk.Label(root, text="Numero 2")
label_num2.place(x=150, y=50)
entry_num2 = tk.Entry(root)
entry_num2.place(x=150, y=80)

# Etiqueta de "Resultado"
label_res = tk.Label(root, text="Resultado")
label_res.place(x=250, y=50)
label_resultado = tk.Label(root, text="0", font=("Arial", 12, "bold"))
label_resultado.place(x=250, y=80)

# Botones para las operaciones
btn_sumar = tk.Button(root, text="+", width=5, command=lambda: calcular("+"))
btn_sumar.place(x=50, y=150)

btn_restar = tk.Button(root, text="-", width=5, command=lambda: calcular("-"))
btn_restar.place(x=120, y=150)

btn_multiplicar = tk.Button(root, text="*", width=5, command=lambda: calcular("*"))
btn_multiplicar.place(x=190, y=150)

btn_dividir = tk.Button(root, text="/", width=5, command=lambda: calcular("/"))
btn_dividir.place(x=260, y=150)

# Iniciar el bucle principal
root.mainloop()
