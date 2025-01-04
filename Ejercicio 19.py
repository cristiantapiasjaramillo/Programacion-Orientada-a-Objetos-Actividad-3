import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 3 * self.lado

    def altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def area(self):
        return (math.sqrt(3) / 4) * (self.lado ** 2)

class App:
    def __init__(self, root): 
        self.root = root
        self.root.title("Cálculos de Triángulo Equilátero")
        
        self.label_lado = tk.Label(root, text="Lado del triángulo:")
        self.label_lado.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_lado = tk.Entry(root)
        self.entry_lado.grid(row=0, column=1, padx=10, pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.button_calcular.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.text_resultados = tk.Text(root, height=10, width=40)
        self.text_resultados.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            lado = float(self.entry_lado.get())
            if lado <= 0:
                raise ValueError("El lado debe ser un número positivo.")

            triangulo = TrianguloEquilatero(lado)
            perimetro = triangulo.perimetro()
            altura = triangulo.altura()
            area = triangulo.area()

            self.text_resultados.delete(1.0, tk.END)
            self.text_resultados.insert(tk.END, f"Resultados:\n")
            self.text_resultados.insert(tk.END, f"Perímetro: {perimetro:.2f} unidades\n")
            self.text_resultados.insert(tk.END, f"Altura: {altura:.2f} unidades\n")
            self.text_resultados.insert(tk.END, f"Área: {area:.2f} unidades cuadradas\n")

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
