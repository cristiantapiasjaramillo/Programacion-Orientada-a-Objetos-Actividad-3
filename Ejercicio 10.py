import tkinter as tk
class Alumno:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
     self.numero_inscripcion = numero_inscripcion
     self.nombres = nombres
     self.patrimonio = patrimonio
     self.estrato = estrato
    
    def calculador_matricula(self):
     pago_matricula = 50000
     if self.patrimonio>2000000 and self.estrato>3:
        return 50000+0.03*self.patrimonio
     else:
        return pago_matricula

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Matricula alumno")

    self.label_numero_inscripcion = tk.Label(root, text="Numero de inscripción")
    self.label_numero_inscripcion.grid(row=0, column=0)

    self.entry_numero_inscripcion = tk.Entry(root)
    self.entry_numero_inscripcion.grid(row=0, column=1)

    self.label_nombres = tk.Label(root, text = "Nombres")
    self.label_nombres.grid(row=1, column=0)

    self.entry_nombres = tk.Entry(root)
    self.entry_nombres.grid(row=1, column=1)

    self.label_patrimonio = tk.Label(root, text = "Patrimonio")
    self.label_patrimonio.grid(row=2, column=0)

    self.entry_patrimonio = tk.Entry(root)
    self.entry_patrimonio.grid(row=2, column=1)

    self.label_estrato = tk.Label(root, text="Estrato social")
    self.label_estrato.grid(row=3, column=0)

    self.entry_estrato = tk.Entry(root)
    self.entry_estrato.grid(row=3, column=1)

    self.button_calcular = tk.Button(root, text="calcular", command=self.calcular)
    self.button_calcular.grid(row=4, column=0, columnspan=2)

    self.text_resultados = tk.Text(root, height=10, width=40)
    self.text_resultados.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

  def calcular(self):
        numero_inscripcion = self.entry_numero_inscripcion.get()
        nombres = self.entry_nombres.get()
        patrimonio = float(self.entry_patrimonio.get())
        estrato = int(self.entry_estrato.get())

        alumno = Alumno(numero_inscripcion, nombres, patrimonio, estrato)
        pago_matricula = alumno.calculador_matricula()

        self.text_resultados.delete(1.0, tk.END)
        self.text_resultados.insert(tk.END, f"Resultados:\n")
        self.text_resultados.insert(tk.END, f"Número de inscripción: {numero_inscripcion} \n")
        self.text_resultados.insert(tk.END, f"Nombres: {nombres} \n")
        self.text_resultados.insert(tk.END, f"Pago de Matricula: ${pago_matricula:.2f} \n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
