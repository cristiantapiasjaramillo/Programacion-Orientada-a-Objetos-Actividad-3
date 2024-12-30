import tkinter as tk
class Empleado:
    def __init__(self, nombres, salario_hora, horas_trabajadas_mes):
     self.nombres = nombres
     self.salario_hora = salario_hora
     self.horas_trabajadas_mes = horas_trabajadas_mes
    
    def calculador_salario(self):
     salario_mensual = self.salario_hora*self.horas_trabajadas_mes
     if salario_mensual>450000:
        return salario_mensual
     else:
        return None

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Salario mesual empleado")

    self.label_nombres = tk.Label(root, text="Nombres")
    self.label_nombres.grid(row=0, column=0)

    self.entry_nombres = tk.Entry(root)
    self.entry_nombres.grid(row=0, column=1)

    self.label_salario_hora = tk.Label(root, text = "Salario por hora")
    self.label_salario_hora.grid(row=1, column=0)

    self.entry_salario_hora = tk.Entry(root)
    self.entry_salario_hora.grid(row=1, column=1)

    self.label_horas_trabajadas_mes = tk.Label(root, text = "Horas trabajadas en el mes")
    self.label_horas_trabajadas_mes.grid(row=2, column=0)

    self.entry_horas_trabajadas_mes = tk.Entry(root)
    self.entry_horas_trabajadas_mes.grid(row=2, column=1)

    self.button_calcular = tk.Button(root, text="calcular", command=self.calcular)
    self.button_calcular.grid(row=3, column=0, columnspan=2)

    self.text_resultados = tk.Text(root, height=10, width=40)
    self.text_resultados.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

  def calcular(self):
        nombres = self.entry_nombres.get()
        salario_hora = float(self.entry_salario_hora.get())
        horas_trabajadas_mes = int(self.entry_horas_trabajadas_mes.get())

        empleado = Empleado(nombres, salario_hora, horas_trabajadas_mes)
        salario = empleado.calculador_salario()

        self.text_resultados.delete(1.0, tk.END)

        if salario is not None:
         self.text_resultados.insert(tk.END, f"Resultados:\n")
         self.text_resultados.insert(tk.END, f"Nombres: {nombres} \n")
         self.text_resultados.insert(tk.END, f"Salario mensual: ${salario} \n")
        else:
         self.text_resultados.insert(tk.END, f"Resultados:\n")
         self.text_resultados.insert(tk.END, f"Nombres: {nombres} \n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
