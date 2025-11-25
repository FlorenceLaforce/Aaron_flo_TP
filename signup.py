import tkinter as tk
from tkinter import ttk, messagebox

#TODO
#   -finir le build_ui
#   -eula checkbox
#   -bouton inscrire
#   -valider mots de passe
#   -database type shi


class SignupWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window = tk.Toplevel()
        self.window.title("Inscription")
        self.window.geometry("300x200")
        self.build_ui()

    def build_ui(self):
        self.frm = tk.Frame(self)
        self.frm.grid(row=0, column=0, sticky="nsew")

        self.prenom_lb = ttk.Label(self.frm, text="prenom :")
        self.prenom_lb.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        self.nom_lb = ttk.Label(self.frm, text="Nom :")
        self.nom_lb.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        self.email_lb = ttk.Label(self.frm, text="Email :")
        self.email_lb.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

        self.mdp_lb = ttk.Label(self.frm, text="Mot de passe :")
        self.mdp_lb.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        self.mdp_check_lb = ttk.Label(self.frm, text="Mot de passe :")
        self.mdp_check_lb.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)