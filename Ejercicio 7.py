import tkinter as tk
class Valores:
 def __init__(self, valora, valorb):
    self.valora = valora
    self.valorb= valorb
 def comparador(self):
    if self.valora>self.valorb:
     return "mayor que"
    elif self.valora == self.valorb:
     return "igual que"
    else: 
     return "menor que"
class App:
 def __init__(self, root):
    self.root = root
    self.root.title("Comparador de valores")

    self.label_valora = tk.Label(root, text="Ingrese el valor de A")
    self.label_valora.grid(row=0, column=0)

    self.entry_valora = tk.Entry(root)
    self.entry_valora.grid(row=0, column=1)

    self.label_valorb = tk.Label(root, text="Ingrese el valor de B")
    self.label_valorb.grid(row=1, column=0)

    self.entry_valorb = tk.Entry(root)
    self.entry_valorb.grid(row=1, column=1)

    self.button = tk.Button(root, text="Comparar", command=self.calcular)
    self.button.grid(row=2, column=0, columnspan=2)

    self.text_resultados = tk.Text(root)
    self.text_resultados.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

 def calcular(self):
        valora = float(self.entry_valora.get())
        valorb = float(self.entry_valorb.get())

        valores = Valores(valora, valorb)
        comparador = valores.comparador()

        self.text_resultados.delete(1.0, tk.END)
        self.text_resultados.insert(tk.END, f"Resultados:\n")
        self.text_resultados.insert(tk.END, f"{valora} es {comparador} {valorb} \n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
