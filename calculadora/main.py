import tkinter as tk

def realizar_operacion():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def limpiar_pantalla():
    entrada.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear la entrada para la pantalla
entrada = tk.Entry(ventana, width=16, font=('Arial', 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4)

# Definir los botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Crear los botones y asignarles funciones
for boton_texto, fila, columna in botones:
    boton = tk.Button(ventana, text=boton_texto, width=4, height=2,
                      font=('Arial', 14), command=lambda texto=boton_texto: agregar_caracter(texto) if texto != '=' else realizar_operacion())
    boton.grid(row=fila, column=columna)

# Botón para limpiar la pantalla
limpiar_boton = tk.Button(ventana, text="C", width=4, height=2, font=('Arial', 14), command=limpiar_pantalla)
limpiar_boton.grid(row=5, column=0, columnspan=3)

# Iniciar la aplicación
ventana.mainloop()
