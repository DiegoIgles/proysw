import tkinter as tk
from tkinter import messagebox
import subprocess  # Módulo para ejecutar archivos del sistema

# Función para verificar las credenciales
def verificar_credenciales():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "admin" and contraseña == "12345":
        messagebox.showinfo("Login", "¡Inicio de sesión exitoso!")
        ventana.destroy()  # Cierra la ventana del login
        abrir_dashboard()  # Llama a la función para abrir el dashboard
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos.")

# Función para abrir el dashboard
def abrir_dashboard():
    dashboard = tk.Tk()  # Nueva ventana para el dashboard
    dashboard.title("Dashboard")
    dashboard.geometry("500x400")
    dashboard.configure(bg="#34495E")  # Color de fondo del dashboard

    # Etiqueta de bienvenida en el dashboard
    label_bienvenida = tk.Label(dashboard, text="¡Bienvenido al Dashboard!", font=("Arial", 20, "bold"), bg="#34495E", fg="white")
    label_bienvenida.pack(pady=20)

    # Botón para ejecutar el archivo de captura de imágenes
    boton_opcion1 = tk.Button(dashboard, text="Ejecutar captura de imágenes", font=("Arial", 14), bg="#3498DB", fg="white", width=30, command=ejecutar_archivo_captura)
    boton_opcion1.pack(pady=10)

    # Botón para ejecutar el archivo de modelo
    boton_opcion2 = tk.Button(dashboard, text="Entrenar modelo", font=("Arial", 14), bg="#E74C3C", fg="white", width=30, command=ejecutar_archivo_modelo)
    boton_opcion2.pack(pady=10)

    # Botón para ejecutar el archivo de reconocimiento de objetos
    boton_opcion3 = tk.Button(dashboard, text="Reconocimiento de objetos", font=("Arial", 14), bg="#8E44AD", fg="white", width=30, command=ejecutar_archivo_reconocimiento)
    boton_opcion3.pack(pady=10)

    # Iniciar el bucle principal del dashboard
    dashboard.mainloop()

# Función para ejecutar el archivo de captura de imágenes y abrir CMD
def ejecutar_archivo_captura():
    try:
        ruta_archivo_captura = r"F:\SOFTWARE PROYECTO\proysw\capturar_imagenes.py"
        
        # Ejecuta el archivo en una nueva ventana del símbolo de sistema (CMD)
        subprocess.Popen(["python", ruta_archivo_captura], creationflags=subprocess.CREATE_NEW_CONSOLE)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el archivo de captura: {str(e)}")

# Función para ejecutar el archivo de modelo y abrir CMD
def ejecutar_archivo_modelo():
    try:
        ruta_archivo_modelo = r"F:\SOFTWARE PROYECTO\proysw\entrenar_modelo.py"
        
        # Ejecuta el archivo en una nueva ventana del símbolo de sistema (CMD)
        subprocess.Popen(["python", ruta_archivo_modelo], creationflags=subprocess.CREATE_NEW_CONSOLE)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el archivo de modelo: {str(e)}")

# Función para ejecutar el archivo de reconocimiento de objetos y abrir CMD
def ejecutar_archivo_reconocimiento():
    try:
        ruta_archivo_reconocimiento = r"F:\SOFTWARE PROYECTO\proysw\reconocimiento_tiempo_real.py"  # Cambia el nombre del archivo aquí
        
        # Ejecuta el archivo en una nueva ventana del símbolo de sistema (CMD)
        subprocess.Popen(["python", ruta_archivo_reconocimiento], creationflags=subprocess.CREATE_NEW_CONSOLE)
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el archivo de reconocimiento: {str(e)}")

# Crear la ventana principal de login
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("400x300")
ventana.configure(bg="#2C3E50")  # Color de fondo principal

# Estilos personalizados para placeholders
def crear_entry_placeholder(entry, placeholder, color_placeholder="gray"):
    entry.insert(0, placeholder)
    entry.config(fg=color_placeholder)
    
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
    
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg=color_placeholder)
    
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Frame central para el login
frame_login = tk.Frame(ventana, bg="#ECF0F1", bd=5, relief="groove")
frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=250)

# Título de la ventana de login
label_titulo = tk.Label(frame_login, text="Iniciar Sesión", font=("Arial", 16, "bold"), bg="#ECF0F1", fg="#34495E")
label_titulo.pack(pady=10)

# Campo de entrada para el usuario con diseño
entry_usuario = tk.Entry(frame_login, font=("Arial", 12), bd=2, relief="solid", justify="center")
crear_entry_placeholder(entry_usuario, "Usuario")
entry_usuario.pack(pady=10, padx=10, ipady=5)

# Campo de entrada para la contraseña con diseño
entry_contraseña = tk.Entry(frame_login, font=("Arial", 12), bd=2, relief="solid", justify="center", show="*")
crear_entry_placeholder(entry_contraseña, "Contraseña")
entry_contraseña.pack(pady=10, padx=10, ipady=5)

# Botón para iniciar sesión
boton_login = tk.Button(frame_login, text="Iniciar sesión", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", 
                        bd=0, relief="flat", command=verificar_credenciales, cursor="hand2")
boton_login.pack(pady=15, ipadx=10, ipady=5)

# Iniciar el bucle principal de la ventana de login
ventana.mainloop()
