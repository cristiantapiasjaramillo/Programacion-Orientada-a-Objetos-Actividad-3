import tkinter as tk
import math

class Ecuacion:
 def __init__(self, parametroA, parametroB, parametroC):
   self.parametroA = parametroA
   self.parametroB = parametroB
   self.parametroC= parametroC
    
 def calculador_soluciones(self):
  discriminante = self.parametroB**2 - 4*self.parametroA* self.parametroC
  if discriminante > 0:
          x1 = (-self.parametroB + math.sqrt(discriminante)) / (2 * self.parametroA)
          x2 = (-self.parametroB - math.sqrt(discriminante)) / (2 * self.parametroA)
          return f"x1 = {x1:.2f}, x2 = {x2:.2f}"
  elif discriminante == 0:
          x = -self.parametroB / (2 * self.parametroA)
          return f"x = {x:.2f}"
  else:
          return "La ecuación no tiene soluciones reales."

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Solucionador ecuación de segundo grado")

    self.label_parametroA = tk.Label(root, text="Ingrese parametro A")
    self.label_parametroA.grid(row=0, column=0)

    self.entry_parametroA = tk.Entry(root)
    self.entry_parametroA.grid(row=0, column=1)

    self.label_parametroB = tk.Label(root, text = "Ingrese parametro B")
    self.label_parametroB.grid(row=1, column=0)

    self.entry_parametroB = tk.Entry(root)
    self.entry_parametroB.grid(row=1, column=1)

    self.label_parametroC = tk.Label(root, text = "Ingrese Parametro C")
    self.label_parametroC.grid(row=2, column=0)

    self.entry_parametroC = tk.Entry(root)
    self.entry_parametroC.grid(row=2, column=1)

    self.button_calcular = tk.Button(root, text="calcular", command=self.calcular)
    self.button_calcular.grid(row=3, column=0, columnspan=2)

    self.text_resultados = tk.Text(root, height=5, width=60)
    self.text_resultados.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

  def calcular(self):
        parametroA = float(self.entry_parametroA.get())
        parametroB = float(self.entry_parametroB.get())
        parametroC = float(self.entry_parametroC.get())

        ecuacion = Ecuacion(parametroA, parametroB, parametroC)
        soluciones = ecuacion.calculador_soluciones()

        self.text_resultados.delete(1.0, tk.END)
        self.text_resultados.insert(tk.END, f"Resultados:\n")
        self.text_resultados.insert(tk.END, f"Soluciones: {soluciones} \n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
