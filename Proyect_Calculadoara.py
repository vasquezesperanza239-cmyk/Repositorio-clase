import customtkinter as ctk

# -------------------------
# CONFIGURACIÓN
# -------------------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()

ventana.title("Calculadora")
ventana.geometry("350x550")
ventana.resizable(False, False)

# -------------------------
# FUNCIONES
# -------------------------

def agregar(valor):
    pantalla.insert("end", valor)

def limpiar():
    pantalla.delete(0, "end")

def borrar():
    texto = pantalla.get()

    pantalla.delete(0, "end")
    pantalla.insert(0, texto[:-1])

def calcular():
    try:
        expresion = pantalla.get()

        expresion = expresion.replace("×", "*")
        expresion = expresion.replace("÷", "/")
        expresion = expresion.replace("−", "-")

        resultado = eval(expresion)

        pantalla.delete(0, "end")
        pantalla.insert(0, resultado)

    except:
        pantalla.delete(0, "end")
        pantalla.insert(0, "Error")

def porcentaje():
    try:
        numero = float(pantalla.get())
        resultado = numero / 100

        pantalla.delete(0, "end")
        pantalla.insert(0, resultado)

    except:
        pantalla.delete(0, "end")
        pantalla.insert(0, "Error")

def cambiar_signo():
    try:
        numero = float(pantalla.get())
        numero = numero * -1

        pantalla.delete(0, "end")
        pantalla.insert(0, numero)

    except:
        pass

# -------------------------
# PANTALLA
# -------------------------

pantalla = ctk.CTkEntry(
    ventana,
    width=320,
    height=80,
    font=("Arial", 35),
    justify="right"
)

pantalla.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=15,
    pady=15
)

# -------------------------
# BOTONES
# -------------------------

botones = [
    ("%", 1, 0),
    ("CE", 1, 1),
    ("C", 1, 2),
    ("⌫", 1, 3),

    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("÷", 2, 3),

    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("×", 3, 3),

    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("−", 4, 3),

    ("+/-", 5, 0),
    ("0", 5, 1),
    (".", 5, 2),
    ("+", 5, 3),

    ("=", 6, 0)
]

# -------------------------
# CREAR BOTONES
# -------------------------

for boton in botones:

    texto = boton[0]
    fila = boton[1]
    columna = boton[2]

    if texto == "=":

        boton_ctk = ctk.CTkButton(
            ventana,
            text=texto,
            width=320,
            height=60,
            font=("Arial", 22),
            fg_color="#0078D4",
            hover_color="#0067B8",
            command=calcular
        )

        boton_ctk.grid(
            row=fila,
            column=0,
            columnspan=4,
            padx=15,
            pady=5
        )

    else:

        if texto == "C":
            comando = limpiar

        elif texto == "CE":
            comando = limpiar

        elif texto == "⌫":
            comando = borrar

        elif texto == "%":
            comando = porcentaje

        elif texto == "+/-":
            comando = cambiar_signo

        else:
            comando = lambda valor=texto: agregar(valor)

        boton_ctk = ctk.CTkButton(
            ventana,
            text=texto,
            width=75,
            height=60,
            font=("Arial", 20),
            fg_color="#C5E6EE",
            text_color="#3B3451",
            hover_color="#D58FEC",
            command=comando
        )

        boton_ctk.grid(
            row=fila,
            column=columna,
            padx=4,
            pady=4
        )

# -------------------------
# EJECUTAR
# -------------------------

ventana.mainloop()