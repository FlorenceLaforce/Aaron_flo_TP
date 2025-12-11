import sqlite3
from tkinter import messagebox
from interfaces.login import LoginWindow

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
import tkinter as tk
from tkinter import ttk

DB_PATH = "inscription.db"


class SignupWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Inscription")
        self.configure(bg="#f3f4f6")
        self.geometry("380x400")
        self.resizable(False, False)
        self.init_db()
        self._configure_style()
        self.build_ui()

    def init_db(self):
        self.conn = sqlite3.connect(DB_PATH)
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS inscription (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        last_name text NOT NULL,
        email text NOT NULL,
        mdp text NOT NULL
        )
        """)
        self.conn.commit()

    def _insert_inscription(self, name, last_name, email, mdp):
        self.conn.execute(
            "INSERT INTO inscription (name, last_name, email, mdp) VALUES (?, ?, ?, ?)",
            (name, last_name, email, mdp)
        )
        self.conn.commit()

    def _update_inscription(self,row_id, name, last_name, email, mdp):
        self.conn.execute(
            "UPDATE inscription SET name = ?, last_name = ?, email = ?, mdp = ? WHERE id= ?",
            (name, last_name, email, mdp, row_id)
        )
        self.conn.commit()

    def _delete_inscription(self, row_id):
        self.conn.execute("DELETE FROM inscription WHERE id= ?", (row_id,))
        self.conn.commit()

    def _fetch_all_inscriptions(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, last_name, email, mdp FROM inscription ORDER BY id")
        return cur.fetchall()


    def _configure_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Card.TFrame", background="white")
        style.configure("Form.TLabel", background="white", font=("Segoe UI", 10))
        style.configure("Title.TLabel", background="white", font=("Segoe UI", 14, "bold"))
        style.configure("Error.TLabel", background="white", foreground="red", font=("Segoe UI", 9))
        style.configure("Hint.TLabel", background="white", foreground="#6b7280", font=("Segoe UI", 8))

        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=(10, 5))

    def build_ui(self):
        Frame1 = tk.Frame(self, bg="#f3f4f6")
        Frame1.pack(expand=True, fill="both", padx=20, pady=20)

        card = ttk.Frame(Frame1, style="Card.TFrame", padding=20)
        card.pack(expand=True)

        # Titre
        title_lb = ttk.Label(card, text="Créer un compte", style="Title.TLabel")
        title_lb.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Prénom
        self.prenom_lb = ttk.Label(card, text="Prénom :", style="Form.TLabel")
        self.prenom_lb.grid(row=1, column=0, sticky="w", pady=3)

        self.prenom_en = ttk.Entry(card)
        self.prenom_en.grid(row=1, column=1, sticky="ew", pady=3)

        # Nom
        self.nom_lb = ttk.Label(card, text="Nom :", style="Form.TLabel")
        self.nom_lb.grid(row=2, column=0, sticky="w", pady=3)

        self.nom_en = ttk.Entry(card)
        self.nom_en.grid(row=2, column=1, sticky="ew", pady=3)

        # Email
        self.email_lb = ttk.Label(card, text="Email :", style="Form.TLabel")
        self.email_lb.grid(row=3, column=0, sticky="w", pady=3)

        self.email_en = ttk.Entry(card)
        self.email_en.grid(row=3, column=1, sticky="ew", pady=3)

        # Mot de passe
        self.mdp_lb = ttk.Label(card, text="Mot de passe :", style="Form.TLabel")
        self.mdp_lb.grid(row=4, column=0, sticky="w", pady=3)

        self.mdp_en = ttk.Entry(card, show="*")
        self.mdp_en.grid(row=4, column=1, sticky="ew", pady=3)

        # ➕ Petite ligne d'information
        self.mdp_hint = ttk.Label(card, text="* doit contenir 5 caractères.",
                                  style="Hint.TLabel")
        self.mdp_hint.grid(row=5, column=0, columnspan=2, sticky="w", pady=(0, 5))

        # Confirmer mot de passe
        self.mdp_check_lb = ttk.Label(card, text="Confirmer :", style="Form.TLabel")
        self.mdp_check_lb.grid(row=6, column=0, sticky="w", pady=3)

        self.mdp_check_en = ttk.Entry(card, show="*")
        self.mdp_check_en.grid(row=6, column=1, sticky="ew", pady=3)

        # Label d’erreur
        self.error_lb = ttk.Label(card, text="", style="Error.TLabel")
        self.error_lb.grid(row=7, column=0, columnspan=2, pady=(5, 0))

        # Bouton VALIDER
        self.validate_bt = ttk.Button(
            card,
            text="Valider",
            style="Primary.TButton",
            command=self.validate_form
        )
        self.validate_bt.grid(row=8, column=0, columnspan=2, sticky="ew", pady=(10, 5))

        # Bouton S'INSCRIRE (désactivé au début)
        self.signup_bt = ttk.Button(
            card,
            text="S'inscrire",
            style="Primary.TButton",
            state="disabled",
            command=self.on_signup
        )
        self.signup_bt.grid(row=9, column=0, columnspan=2, sticky="ew")

        card.columnconfigure(1, weight=1)


    def validate_form(self):
        """Validation : mots de passe identiques + champs non vides + longueur min 5"""
        prenom = self.prenom_en.get().strip()
        nom = self.nom_en.get().strip()
        email = self.email_en.get().strip()
        mdp = self.mdp_en.get()
        mdp_check = self.mdp_check_en.get()

        self.error_lb.config(text="", foreground="red")

        if not prenom or not nom or not email or not mdp or not mdp_check:
            self.error_lb.config(text="Veuillez remplir tous les champs.")
            self.signup_bt.config(state="disabled")
            return

        if len(mdp) != 5:
            self.error_lb.config(text="Le mot de passe doit contenir 5 caractères.")
            self.signup_bt.config(state="disabled")
            return

        if mdp != mdp_check:
            self.error_lb.config(text="Les mots de passe ne correspondent pas.")
            self.signup_bt.config(state="disabled")
            return

        # Si tout est OK
        self.error_lb.config(text="Validé !", foreground="green")
        self.signup_bt.config(state="normal")

    def on_signup(self):
        self.validate_form()
        if self.signup_bt["state"] == "disabled":
            return

        prenom = self.prenom_en.get().strip()
        nom = self.nom_en.get().strip()
        email = self.email_en.get().strip()
        mdp = self.mdp_en.get()

        try:
            self._insert_inscription(prenom, nom, email, mdp)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'enregistrer l'inscription :\n{e}")
            return
        messagebox.showinfo("Inscription réussie!","Vous pouvez maintenant vous connecter")
        LoginWindow(self.master)
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    win = SignupWindow(root)
    win.mainloop()
