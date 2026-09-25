import customtkinter as ctk

# Configuración
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("350x500")
        self.resizable(False, False)

        self.expresion = ""

        # Pantalla
        self.pantalla = ctk.CTkEntry(
            self,
            width=310,
            height=70,
            font=("Arial", 30),
            justify="right",
            corner_radius=10
        )
        self.pantalla.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=20
        )

        # Botones
        botones = [
            ("C", 1, 0),
            ("⌫", 1, 1),
            ("÷", 1, 2),
            ("×", 1, 3),

            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("-", 2, 3),

            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("+", 3, 3),

            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("=", 4, 3),

            ("0", 5, 0),
            (".", 5, 1),
        ]

        for texto, fila, columna in botones:
            if texto == "=":
                color = "#2FA572"
            elif texto in ["+", "-", "×", "÷"]:
                color = "#E67E22"
            elif texto in ["C", "⌫"]:
                color = "#C0392B"
            else:
                color = "#3A3A3A"

            boton = ctk.CTkButton(
                self,
                text=texto,
                width=70,
                height=60,
                font=("Arial", 22),
                fg_color=color,
                hover_color="#555555",
                command=lambda t=texto: self.presionar(t)
            )

            boton.grid(
                row=fila,
                column=columna,
                padx=5,
                pady=5
            )

    def presionar(self, tecla):
        if tecla == "C":
            self.expresion = ""
            self.pantalla.delete(0, "end")

        elif tecla == "⌫":
            self.expresion = self.expresion[:-1]
            self.pantalla.delete(0, "end")
            self.pantalla.insert(0, self.expresion)

        elif tecla == "=":
            try:
                expresion = self.expresion.replace("×", "*")
                expresion = expresion.replace("÷", "/")

                resultado = eval(expresion)

                self.expresion = str(resultado)

                self.pantalla.delete(0, "end")
                self.pantalla.insert(0, self.expresion)

            except:
                self.expresion = ""
                self.pantalla.delete(0, "end")
                self.pantalla.insert(0, "Error")

        else:
            self.expresion += tecla

            self.pantalla.delete(0, "end")
            self.pantalla.insert(0, self.expresion)


# Ejecutar
app = Calculadora()
app.mainloop()
