import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant | Aaroncini")
        self.geometry("900x600")
        self.configure(bg="#f4f4f4")
        self.creer_widget()

    def creer_widget(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #FRAME
        self.frame_principal = tk.Frame(self,bg="#f4f4f4")
        self.frame_principal.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=2)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)

        self.frame_top_gauche = tk.Frame(self.frame_principal)
        self.frame_top_gauche.grid(row=0, column=0, sticky="nsew")

        self.frame_bottom_gauche = tk.Frame(self.frame_principal)
        self.frame_bottom_gauche.grid(row=1, column=0, sticky="nsew")

        self.frame_droit = tk.Frame(self.frame_principal)
        self.frame_droit.grid(row=0, column=1, sticky="nsew")

        #LABEL FRAME DROIT
        self.Main_label = tk.Label(self.frame_droit, text="AARONCINI", font=("Arial", 40, "bold"))
        self.Main_label.grid(row=0, column=0, sticky="nsew")

        self.mini_label = tk.Label(self.frame_droit, text="Restaurante Italiano", font=("Arial", 15, "bold"))
        self.mini_label.grid(row=1, column=0, sticky="nsew")

        self.label_legende = tk.Label(self.frame_top_gauche, text="*Apperçu des réservation", font=("Arial", 10))
        self.label_legende.grid(row=2, column=0, sticky="n")

        #BUTTON FRAME DROIT
        self.btn_reserver = tk.Button(self.frame_droit, text = "Réserver", font=("Arial", 20))
        self.btn_reserver.grid(row=2, column=0, sticky="nsew")

        self.btn_connexion = tk.Button(self.frame_droit, text = "Connexion", font=("Arial", 20))
        self.btn_connexion.grid(row=3, column=0, sticky="nsew")

        self.btn_inscription = tk.Button(self.frame_droit, text = "Inscription", font=("Arial", 20))
        self.btn_inscription.grid(row=4, column=0, sticky="nsew")

        #BUTTON FRAME GAUCHE HAUT
        self.btn_gestion = tk.Button(self.frame_top_gauche, text = "Gestion", font=("Arial", 20))
        self.btn_gestion.grid(row=0, column=0, sticky="nsew")

        self.btn_reservations = tk.Button(self.frame_top_gauche, text = "Réservations", font=("Arial", 20))
        self.btn_reservations.grid(row=1, column=0, sticky="nsew")

        #BUTTON FRAME GAUCHE BAS
        self.btn_importer = tk.Button(self.frame_bottom_gauche, text="Importer", font=("Arial", 20))
        self.btn_importer.grid(row=0, column=0, sticky="nsew")

        self.btn_exporter = tk.Button(self.frame_bottom_gauche, text="Exporter", font=("Arial", 20))
        self.btn_exporter.grid(row=1, column=0, sticky="nsew")



if __name__ == "__main__":
    App().mainloop()