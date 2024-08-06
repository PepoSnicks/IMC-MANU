import tkinter as tk
from tkinter import PhotoImage, messagebox, Canvas
import csv

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def mostrar_resultado():
    try:
        peso = float(peso_entry.get())
        altura = float(altura_entry.get())
        
        if altura <= 0:
            raise ValueError("La altura debe ser un valor positivo.")
        
        imc = calcular_imc(peso, altura)
        resultado_label.config(text=f"Su Índice de Masa Corporal es: {imc:.2f}")
        messagebox.showinfo("Resultado", f"Su Índice de Masa Corporal es: {imc:.2f}")
        
        # Mostrar tabla comparativa
        mostrar_tabla_comparativa()
    except ValueError as e:
        messagebox.showerror("Error", f"Error en los datos introducidos: {e}")

def guardar_datos():
    try:
        with open('IMC.csv', mode='a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            nombre = nombre_entry.get()
            peso = float(peso_entry.get())
            altura = float(altura_entry.get())
            sexo = sexo_var.get()
            edad = int(edad_spinbox.get())  # Obtener valor del Spinbox
            
            imc = calcular_imc(peso, altura)
            
            writer.writerow([nombre, peso, altura, sexo, edad, imc])
            
            messagebox.showinfo("Guardado", "Datos guardados exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar los datos: {e}")

def cambiar_imagen_boton(button, imagen):
    button.config(image=imagen)

def mostrar_tabla_comparativa():
    # Crear y mostrar la tabla comparativa de IMC
    tabla_label = tk.Label(ventana, text="Tabla comparativa de IMC", font=("Arial", 16, "bold"), fg="#202C3D", bg="white")
    tabla_label.grid(row=8, column=0, columnspan=2, pady=10)
    
    tabla = tk.Frame(ventana, bg="white")
    tabla.grid(row=9, column=0, columnspan=2, pady=5)
    
    tk.Label(tabla, text="Categoría", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(tabla, text="IMC", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(tabla, text="Bajo peso", font=("Arial", 14), bg="white").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(tabla, text="< 18.5", font=("Arial", 14), bg="white").grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(tabla, text="Peso adecuado", font=("Arial", 14), bg="white").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(tabla, text="18.5 - 24.9", font=("Arial", 14), bg="white").grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(tabla, text="Sobrepeso", font=("Arial", 14), bg="white").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(tabla, text="25 - 29.9", font=("Arial", 14), bg="white").grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(tabla, text="Obesidad", font=("Arial", 14), bg="white").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(tabla, text=">= 30", font=("Arial", 14), bg="white").grid(row=4, column=1, padx=10, pady=5)

ventana = tk.Tk()
ventana.title("Cálculo del Índice de Masa Corporal")
ventana.config(bg="white")

titulo_label = tk.Label(ventana, text="Cuida tu salud", font=("Arial", 26, "bold"), fg="#741D34", bg="white")
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Nombre:", font=("Arial", 14, "bold"), fg="#202C3D", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
nombre_entry = tk.Entry(ventana, width=25)  # Aumentar el ancho de la entrada
nombre_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Peso (kg):", font=("Arial", 14, "bold"), fg="#202C3D", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="w")
peso_entry = tk.Entry(ventana, width=10)
peso_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Altura (m):", font=("Arial", 14, "bold"), fg="#202C3D", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky="w")
altura_entry = tk.Entry(ventana, width=10)
altura_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="Edad (años):", font=("Arial", 14, "bold"), fg="#202C3D", bg="white").grid(row=4, column=0, padx=10, pady=5, sticky="w")
# Reemplazar Entry por Spinbox para seleccionar la edad
edad_spinbox = tk.Spinbox(ventana, from_=0, to=120, width=10, font=("Arial", 14, "bold"))
edad_spinbox.grid(row=4, column=1, padx=10, pady=5)

tk.Label(ventana, text="Sexo:", font=("Arial", 14, "bold"), fg="#202C3D", bg="white").grid(row=5, column=0, padx=10, pady=5, sticky="w")
sexo_var = tk.StringVar(ventana)
sexo_var.set("Masculino")
sexo_frame = tk.Frame(ventana, bg="white")
sexo_frame.grid(row=5, column=1, columnspan=2, sticky="w")
tk.Radiobutton(sexo_frame, text="Masculino", variable=sexo_var, value="Masculino", bg="white", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(sexo_frame, text="Femenino", variable=sexo_var, value="Femenino", bg="white", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=5)

try:
    calcular_img = PhotoImage(file="/home/juarez/Desktop/Python/exe/calcula.png")
    calcular_img_hover = PhotoImage(file="/home/juarez/Desktop/Python/exe/clicc.png")
except Exception as e:
    print(f"Error al cargar la imagen de calcular: {e}")
    calcular_img = None
    calcular_img_hover = None

try:
    guardar_img = PhotoImage(file="/home/juarez/Desktop/Python/exe/guarda.png")
    guardar_img_hover = PhotoImage(file="/home/juarez/Desktop/Python/exe/clicg.png")
except Exception as e:
    print(f"Error al cargar la imagen de guardar: {e}")
    guardar_img = None
    guardar_img_hover = None

if calcular_img:
    calcular_button = tk.Button(ventana, image=calcular_img, command=mostrar_resultado, borderwidth=0)
    calcular_button.image = calcular_img  
    calcular_button.bind("<Enter>", lambda e: cambiar_imagen_boton(calcular_button, calcular_img_hover))
    calcular_button.bind("<Leave>", lambda e: cambiar_imagen_boton(calcular_button, calcular_img))
else:
    calcular_button = tk.Button(ventana, text="Calcular", command=mostrar_resultado, font=("Arial", 14, "bold"))

calcular_button.grid(row=6, column=0, pady=10)

if guardar_img:
    guardar_button = tk.Button(ventana, image=guardar_img, command=guardar_datos, borderwidth=0)
    guardar_button.image = guardar_img  
    guardar_button.bind("<Enter>", lambda e: cambiar_imagen_boton(guardar_button, guardar_img_hover))
    guardar_button.bind("<Leave>", lambda e: cambiar_imagen_boton(guardar_button, guardar_img))
else:
    guardar_button = tk.Button(ventana, text="Guardar", command=guardar_datos, font=("Arial", 14, "bold"))

guardar_button.grid(row=6, column=1, pady=10)

resultado_label = tk.Label(ventana, text="", bg="white", font=("Arial", 14, "bold"))
resultado_label.grid(row=7, column=0, columnspan=2)

# Agregar un canvas para la imagen de fondo
canvas = Canvas(ventana, width=300, height=200, bg="white", highlightthickness=0)
canvas.grid(row=10, column=0, columnspan=2, pady=20)

try:
    fondo_img = PhotoImage(file="/home/juarez/Desktop/Python/exe/salud.png")
    canvas.create_image(150, 100, image=fondo_img)
except Exception as e:
    print(f"Error al cargar la imagen de fondo: {e}")

ventana.mainloop()
