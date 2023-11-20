import tkinter as tk

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Básica")

        # Pantalla de la calculadora
        self.lbl_pantalla = tk.Label(master, text="", font=("Arial", 16))
        self.lbl_pantalla.grid(row=0, column=0, columnspan=4)

        # Botones de números
        numeros = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
        row_num = 1
        col_num = 0
        for num in numeros:
            btn = tk.Button(master, text=num, padx=20, pady=20, command=lambda n=num: self.agregar_numero(n))
            btn.grid(row=row_num, column=col_num)
            col_num += 1
            if col_num > 2:
                col_num = 0
                row_num += 1

        # Botones de operadores
        operadores = [("+", "-"), ("*", "/")]
        row_op = 1
        col_op = 3
        for op in operadores:
            for o in op:
                btn = tk.Button(master, text=o, padx=20, pady=20, command=lambda o=o: self.agregar_operador(o))
                btn.grid(row=row_op, column=col_op)
                row_op += 1
            col_op += 1
            row_op = 1

        # Botón de igual
        btn_igual = tk.Button(master, text="=", padx=20, pady=20, command=self.mostrar_resultado)
        btn_igual.grid(row=4, column=2)

        # Botón de borrar
        btn_borrar = tk.Button(master, text="C", padx=20, pady=20, command=self.borrar_todo)
        btn_borrar.grid(row=4, column=0)

    def agregar_numero(self, numero):
        current_text = self.lbl_pantalla.cget("text")
        self.lbl_pantalla.config(text=current_text + numero)

    def agregar_operador(self, operador):
        current_text = self.lbl_pantalla.cget("text")
        self.lbl_pantalla.config(text=current_text + operador)

    def mostrar_resultado(self):
        try:
            resultado = eval(self.lbl_pantalla.cget("text"))
            self.lbl_pantalla.config(text=str(resultado))
        except Exception as e:
            self.lbl_pantalla.config(text="Error")

    def borrar_todo(self):
        self.lbl_pantalla.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()