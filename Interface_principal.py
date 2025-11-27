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
        #principal
        self.frame_principal = tk.Frame(self,bg="#f4f4f4")
        self.frame_principal.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_principal.grid_columnconfigure(0, weight=0)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)

        #gauche en haut
        self.frame_top_gauche = tk.Frame(self.frame_principal, bg="#e9e9e9", bd=2, relief="groove")
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
        self.frame_droit = tk.Frame(self.frame_principal)
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

        self.btn_inscription = tk.Button(self.frame_droit, text = "Inscription", font=("Arial", 22), bg="#DAE8FC")
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



if __name__ == "__main__":
    App().mainloop()