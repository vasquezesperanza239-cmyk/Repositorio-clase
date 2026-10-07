import customtkinter as ctk

# ---------------------------------------------------------------
# FUNCIONES DEL DOCENTE
# Si el docente te dio sus propias funciones, reemplaza el contenido
# de estas dos funciones (o pega las suyas con el mismo nombre).
# ---------------------------------------------------------------
def registrar():
    producto = entry_producto.get().strip()
    precio = entry_precio.get().strip()

    if producto == "" or precio == "":
        lbl_resultado.configure(text="Complete todos los campos", text_color="red")
        return

    try:
        precio_num = float(precio)
    except ValueError:
        lbl_resultado.configure(text="El precio debe ser un número", text_color="red")
        return

    lbl_resultado.configure(
        text=f"Producto registrado: {producto} - Q{precio_num:.2f}",
        text_color="green",
    )


def limpiar():
    entry_producto.delete(0, "end")
    entry_precio.delete(0, "end")
    lbl_resultado.configure(text="", text_color="white")
    entry_producto.focus()


# ---------------------------------------------------------------
# VENTANA PRINCIPAL
# ---------------------------------------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Registro de Producto")
ventana.geometry("400x380")
ventana.resizable(False, False)
ventana.grid_columnconfigure((0, 1), weight=1)

# Título
lbl_titulo = ctk.CTkLabel(
    ventana, text="Registro de Producto", font=ctk.CTkFont(size=22, weight="bold")
)
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(25, 20))

# Producto
lbl_producto = ctk.CTkLabel(ventana, text="Producto:")
lbl_producto.grid(row=1, column=0, columnspan=2, padx=40, sticky="w")

entry_producto = ctk.CTkEntry(ventana, placeholder_text="Ingrese el producto", width=320)
entry_producto.grid(row=2, column=0, columnspan=2, padx=40, pady=(0, 15))

# Precio
lbl_precio = ctk.CTkLabel(ventana, text="Precio:")
lbl_precio.grid(row=3, column=0, columnspan=2, padx=40, sticky="w")

entry_precio = ctk.CTkEntry(ventana, placeholder_text="Ingrese el precio", width=320)
entry_precio.grid(row=4, column=0, columnspan=2, padx=40, pady=(0, 20))

# Botones
btn_registrar = ctk.CTkButton(ventana, text="Registrar", command=registrar, width=140)
btn_registrar.grid(row=5, column=0, padx=(40, 10), pady=10)

btn_limpiar = ctk.CTkButton(
    ventana,
    text="Limpiar",
    command=limpiar,
    width=140,
    fg_color="gray40",
    hover_color="gray30",
)
btn_limpiar.grid(row=5, column=1, padx=(10, 40), pady=10)

# Etiqueta de resultado
lbl_resultado = ctk.CTkLabel(ventana, text="", wraplength=320)
lbl_resultado.grid(row=6, column=0, columnspan=2, padx=40, pady=20)

ventana.mainloop()