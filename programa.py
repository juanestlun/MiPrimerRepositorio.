import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    if not edad.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la edad.")
    else:
        messagebox.showinfo("Bienvenido", f"Hola {nombre}, tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Registro de Usuario")
ventana.geometry("300x150")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=10)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

btn_registrar = tk.Button(ventana, text="Registrar", command=registrar)
btn_registrar.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
