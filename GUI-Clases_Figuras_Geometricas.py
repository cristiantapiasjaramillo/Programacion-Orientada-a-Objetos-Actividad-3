import tkinter as tk
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio**2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado**2

    def calcularPerimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.base + self.altura + self.calcularHipotenusa()

    def calcularHipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def tipo_triangulo(self):
        hipotenusa = self.calcularHipotenusa()
        if self.base == self.altura:
            return "Equilátero"
        elif self.base == hipotenusa or self.altura == hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"

class Rombo:
    def __init__(self, diagonal_menor, diagonal_mayor):
        self.diagonal_menor = diagonal_menor
        self.diagonal_mayor = diagonal_mayor

    def calcularLado(self):
        cateto1 = self.diagonal_menor / 2
        cateto2 = self.diagonal_mayor / 2
        return math.sqrt(cateto1**2 + cateto2**2)

    def calcularArea(self):
        return (self.diagonal_menor * self.diagonal_mayor) / 2

    def calcularPerimetro(self):
        return 4 * self.calcularLado()

class Trapecio:
    def __init__(self, base1, base2, altura):
        self.base1 = base1
        self.base2 = base2
        self.altura = altura

    def calcularArea(self):
        return ((self.base1 + self.base2) / 2) * self.altura

    def calcularPerimetro(self):
        return self.base1 + self.base2 + 2 * self.calcularDiagonal()

    def calcularDiagonal(self):
        cateto = abs(self.base1 - self.base2) / 2
        return math.sqrt(cateto**2 + self.altura**2)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometría")
        self.create_buttons()

    def create_buttons(self):
        figuras = ["Círculo", "Rectángulo", "Cuadrado", "TriánguloRectangulo", "Rombo", "Trapecio"]
        for i, figura in enumerate(figuras):
            button = tk.Button(self.root, text=figura, command=lambda i=i: self.open_window(i))
            button.grid(row=i, column=0, padx=10, pady=5)

    def open_window(self, figura_index):
        figuras = [
            self.ventana_circulo,
            self.ventana_rectangulo,
            self.ventana_cuadrado,
            self.ventana_triangulo,
            self.ventana_rombo,
            self.ventana_trapecio,
        ]
        figuras[figura_index]()

    def ventana_circulo(self):
        self.crear_ventana("Círculo", ["Radio"], Circulo)

    def ventana_rectangulo(self):
        self.crear_ventana("Rectángulo", ["Base", "Altura"], Rectangulo)

    def ventana_cuadrado(self):
        self.crear_ventana("Cuadrado", ["Lado"], Cuadrado)

    def ventana_triangulo(self):
        self.crear_ventana("Triángulo Rectángulo", ["Base", "Altura"], TrianguloRectangulo)

    def ventana_rombo(self):
        self.crear_ventana("Rombo", ["Diagonal Menor", "Diagonal Mayor"], Rombo)

    def ventana_trapecio(self):
        self.crear_ventana("Trapecio", ["Base 1", "Base 2", "Altura"], Trapecio)

    def crear_ventana(self, titulo, parametros, clase):
        new_window = tk.Toplevel(self.root)
        new_window.title(titulo)

        inputs = []
        for i, param in enumerate(parametros):
            label = tk.Label(new_window, text=param)
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(new_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            inputs.append(entry)

        def calcular():
            valores = [float(entry.get()) for entry in inputs]
            figura = clase(*valores)
            area = figura.calcularArea()
            perimetro = figura.calcularPerimetro()
            resultados.delete(1.0, tk.END)
            resultados.insert(tk.END, f"Área: {area:.2f}\n")
            resultados.insert(tk.END, f"Perímetro: {perimetro:.2f}\n")

            
            if isinstance(figura, TrianguloRectangulo):
                tipo = figura.tipo_triangulo()
                resultados.insert(tk.END, f"Tipo de triángulo: {tipo}\n")

        calcular_button = tk.Button(new_window, text="Calcular", command=calcular)
        calcular_button.grid(row=len(parametros), column=0, columnspan=2, pady=10)

        resultados = tk.Text(new_window, height=7, width=40)
        resultados.grid(row=len(parametros) + 1, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
