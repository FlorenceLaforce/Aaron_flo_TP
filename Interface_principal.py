import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from signup import SignupWindow


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant | Aaroncini")
        self.geometry("900x600")
        self.configure(bg="#F2F2F2")
        self.creer_widget()

    def creer_widget(self):

        #COULEURS
        COLOR_BG = "#F2F2F2"  # gris clair pro
        COLOR_PANEL = "#E6E6E6"  # gris doux
        COLOR_DARK = "#1C1C1C"  # noir/gris anthracite
        COLOR_ACCENT = "#8B0000"  # rouge foncé élégant
        COLOR_BROWN = "#4E342E"  # brun chocolat
        COLOR_BUTTON = "#333333"  # gris foncé moderne
        COLOR_BUTTON_HOVER = "#555555"

        #ECRITURE
        FONT_TITLE = ("Segoe UI", 48, "bold")
        FONT_SUBTITLE = ("Segoe UI", 18, "italic")
        FONT_PANEL_TITLE = ("Segoe UI", 20, "bold")
        FONT_BUTTON = ("Segoe UI", 18, "bold")

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Bg.Frame",
                        background=COLOR_BG,
                        relief= "flat"
        )

        style.configure(
            "Panel.TFrame",
            background=COLOR_PANEL
        )

        style.configure("TLabel", font=FONT_PANEL_TITLE, bg=COLOR_PANEL,fg=COLOR_DARK)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #FRAME
        #principal
        self.frame_principal = ttk.Frame(self, style="TFrame")
        self.frame_principal.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_principal.grid_columnconfigure(0, weight=0)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)

        #gauche en haut
        self.frame_top_gauche = ttk.Frame(self.frame_principal, style="TFrame")
        self.frame_top_gauche.grid(row=0, column=0, sticky="nsew",  padx=(0,20))

        self.frame_top_gauche.grid_columnconfigure(0, weight=1)
        self.frame_top_gauche.grid_rowconfigure(0, weight=0)
        self.frame_top_gauche.grid_rowconfigure(1, weight=0)
        self.frame_top_gauche.grid_rowconfigure(2, weight=0)
        self.frame_top_gauche.grid_rowconfigure(3, weight=1)

        #gauche en bas
        self.frame_bottom_gauche = tk.Frame(self.frame_principal)
        self.frame_bottom_gauche.grid(row=1, column=0, sticky="nsew")

        self.frame_bottom_gauche.grid_columnconfigure(0, weight=1)
        self.frame_bottom_gauche.grid_rowconfigure(0, weight=1)
        self.frame_bottom_gauche.grid_rowconfigure(1, weight=1)

        self.frame_bottom_gauche.grid_propagate(False)
        self.frame_bottom_gauche.config(height=200)

        #droite
        self.frame_droit = ttk.Frame(self.frame_principal,)
        self.frame_droit.grid(row=0, column=1, sticky="nsew")

        self.frame_droit.grid_columnconfigure(0, weight=1)
        self.frame_droit.grid_rowconfigure(0, weight=0)
        self.frame_droit.grid_rowconfigure(1, weight=0)
        self.frame_droit.grid_rowconfigure(2, weight=1)
        self.frame_droit.grid_rowconfigure(3, weight=1)

        #LABEL FRAME DROIT
        self.Main_label = tk.Label(self.frame_droit, text="AARONCINI", font=("Serif", 45, "bold"), bg="#ffffff")
        self.Main_label.grid(row=0, column=0, sticky="nsew",pady=(20,5))

        self.mini_label = tk.Label(self.frame_droit, text="Ristorante Italiano", font=("Serif", 16, "italic"), bg="#ffffff")
        self.mini_label.grid(row=1, column=0, sticky="nsew", pady=(0,20))


        #LABEL FRAME GAUCHE
        self.titre_gauche = tk.Label(self.frame_top_gauche, text="Administration", font=("Arial", 22, "bold"), bg="#e9e9e9")
        self.titre_gauche.grid(row=0, column=0, pady=(20, 10))

        self.label_legende = tk.Label(self.frame_top_gauche, text="*Apperçu des réservation", font=("Arial", 10), bg="#e9e9e9", fg="#555")
        self.label_legende.grid(row=3, column=0)


        #BUTTON FRAME DROIT
        self.btn_reserver = tk.Button(self.frame_droit, text = "Réserver", font=("Arial", 22), bg="#D5E8D4")
        self.btn_reserver.grid(row=2, column=0, pady=10, padx=150, sticky="")

        self.btn_connexion = tk.Button(self.frame_droit, text = "Connexion", font=("Arial", 22), bg="#F8CECC")
        self.btn_connexion.grid(row=3, column=0, pady=10, padx=150, sticky="")

        self.btn_inscription = tk.Button(self.frame_droit, text = "Inscription", font=("Arial", 22), bg="#DAE8FC", command=self)
        self.btn_inscription.grid(row=4, column=0,  pady=10, padx=150, sticky="")

        #BUTTON FRAME GAUCHE HAUT
        self.btn_gestion = tk.Button(self.frame_top_gauche, text = "Gestion", font=("Arial", 18), height=1, bg="#ffffff")
        self.btn_gestion.grid(row=1, column=0, pady=10, padx=30, sticky="")

        self.btn_reservations = tk.Button(self.frame_top_gauche, text = "Réservations", font=("Arial",  18), bg="#ffffff")
        self.btn_reservations.grid(row=2, column=0, pady=10, padx=30, sticky="")

        #BUTTON FRAME GAUCHE BAS
        self.btn_importer = tk.Button(self.frame_bottom_gauche, text="Importer", font=("Arial", 18), bg="#FFE6CC")
        self.btn_importer.grid(row=0, column=0, pady=10, padx=20, sticky="")

        self.btn_exporter = tk.Button(self.frame_bottom_gauche, text="Exporter", font=("Arial",  18), bg="#FFF2CC")
        self.btn_exporter.grid(row=1, column=0, pady=10, padx=20, sticky="")


    def ouvrir_login(self):
        pass


    def ouvrir_signup(self):
        SignupWindow()


if __name__ == "__main__":
    App().mainloop()