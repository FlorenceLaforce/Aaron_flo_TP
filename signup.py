import tkinter as tk
from tkinter import ttk, messagebox

#TODO
#   -finir le build_ui
#   -eula checkbox
#   -bouton inscrire
#   -valider mots de passe
#   -database type shi

"""
cette classe sort un écran d'inscription. Il faut un prénom, nom, email et mot de passe à double
validation (min. 5 chars). Il doit aussi cocher la boite pour accepter les conditions d'utilisateur
"""
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

        #Labels
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

        #entries
        self.prenom_en = ttk.Entry(self.frm, width=15)
        self.prenom_en.grid(row=0, column=1, sticky="nsew")

        self.nom_en = ttk.Entry(self.frm, width=15)
        self.nom_en.grid(row=1, column=1, sticky="nsew")

        self.email_en = ttk.Entry(self.frm, width=15)
        self.email_en.grid(row=2, column=1, sticky="nsew")

        self.mdp_en = ttk.Entry(self.frm, width=15)
        self.mdp_en.grid(row=3, column=1, sticky="nsew")

        self.mdp_check_en = ttk.Entry(self.frm, width=15)
        self.mdp_check_en.grid(row=4, column=1, sticky="nsew")

        #chechbutton
        self.chk_lb = ttk.Checkbutton(self.frm, text="Valider", variable=self)
        self.chk_lb.grid(row=5, column=1, sticky="nsew")


if __name__ == '__main__':
    app = SignupWindow()
    app.mainloop()