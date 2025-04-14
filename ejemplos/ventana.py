import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x200")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="¡Hola mundo!")
etiqueta.pack()

# Función que se ejecuta al presionar el botón
def saludar():
    etiqueta.config(text="¡Hola desde el botón!")

# Crear botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Ejecutar la ventana
ventana.mainloop()