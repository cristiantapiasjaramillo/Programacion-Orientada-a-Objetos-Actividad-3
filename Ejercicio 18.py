import tkinter as tk
class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente):
     self.codigo = codigo
     self.nombres = nombres
     self.horas_trabajadas = horas_trabajadas
     self.valor_hora = valor_hora
     self.retencion_fuente = retencion_fuente

    def salario_bruto(self):
      return self.horas_trabajadas * self.valor_hora

    def salario_neto(self):
      salario_bruto=self.salario_bruto()
      return salario_bruto - (salario_bruto * (self.retencion_fuente/100))
     
class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Salario Empleado")

    self.label_codigo = tk.Label(root, text="Codigo")
    self.label_codigo.grid(row=0, column=0)

    self.entry_codigo = tk.Entry(root)
    self.entry_codigo.grid(row=0, column=1)

    self.label_nombres = tk.Label(root, text = "Nombres")
    self.label_nombres.grid(row=1, column=0)

    self.entry_nombres = tk.Entry(root)
    self.entry_nombres.grid(row=1, column=1)

    self.label_horas_trabajadas = tk.Label(root, text = "Horas trabajadas")
    self.label_horas_trabajadas.grid(row=2, column=0)

    self.entry_horas_trabajadas = tk.Entry(root)
    self.entry_horas_trabajadas.grid(row=2, column=1)

    self.label_valor_hora = tk.Label(root, text="Valor hora")
    self.label_valor_hora.grid(row=3, column=0)

    self.entry_valor_hora = tk.Entry(root)
    self.entry_valor_hora.grid(row=3, column=1)

    self.label_retencion_fuente = tk.Label(root, text="% Retención en la fuente")
    self.label_retencion_fuente.grid(row=4, column=0)

    self.entry_retencion_fuente = tk.Entry(root)
    self.entry_retencion_fuente.grid(row=4, column=1)

    self.button_calcular = tk.Button(root, text="calcular", command=self.calcular)
    self.button_calcular.grid(row=5, column=0, columnspan=2)

    self.text_resultados = tk.Text(root, height=10, width=40)
    self.text_resultados.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

  def calcular(self):
        codigo = self.entry_codigo.get()
        nombres = self.entry_nombres.get()
        horas_trabajadas = float(self.entry_horas_trabajadas.get())
        valor_hora = float(self.entry_valor_hora.get())
        retencion_fuente = float(self.entry_retencion_fuente.get())

        empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente)
        salario_bruto = empleado.salario_bruto()
        salario_neto = empleado.salario_neto()

        self.text_resultados.delete(1.0, tk.END)
        self.text_resultados.insert(tk.END, f"Resultados:\n")
        self.text_resultados.insert(tk.END, f"Código: {codigo} \n")
        self.text_resultados.insert(tk.END, f"Nombres: {nombres} \n")
        self.text_resultados.insert(tk.END, f"Salario bruto: ${salario_bruto:.2f} \n")
        self.text_resultados.insert(tk.END, f"Salario neto: ${salario_neto:.2f} \n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
