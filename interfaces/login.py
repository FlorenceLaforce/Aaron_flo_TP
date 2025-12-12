import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
DB_PATH = "inscription.db"

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Connexion")
        self.configure(bg="#f3f4f6")
        self.geometry("340x290")
        self.resizable(False, False)
        self._configure_style()
        self.form_is_valid = False
        self.build_ui()

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
        title_lb = ttk.Label(card, text="Se connecter", style="Title.TLabel")
        title_lb.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Email
        self.email_lb = ttk.Label(card, text="Email :", style="Form.TLabel")
        self.email_lb.grid(row=1, column=0, sticky="w", pady=3)

        self.email_en = ttk.Entry(card)
        self.email_en.grid(row=1, column=1, sticky="ew", pady=3)

        # Mot de passe
        self.mdp_lb = ttk.Label(card, text="Mot de passe :", style="Form.TLabel")
        self.mdp_lb.grid(row=2, column=0, sticky="w", pady=3)

        self.mdp_en = ttk.Entry(card, show="*")
        self.mdp_en.grid(row=2, column=1, sticky="ew", pady=3)

        # Petite ligne d'info sous le mot de passe
        self.mdp_hint = ttk.Label(
            card,
            text="* doit contenir 5 caractères.",
            style="Hint.TLabel"
        )
        self.mdp_hint.grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 5))

        # Label d’erreur
        self.error_lb = ttk.Label(card, text="", style="Error.TLabel")
        self.error_lb.grid(row=4, column=0, columnspan=2, pady=(5, 0))

        # Bouton VALIDER
        self.validate_bt = ttk.Button(
            card,
            text="Valider",
            style="Primary.TButton",
            command=self.validate_form
        )
        self.validate_bt.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(10, 5))

        # Bouton SE CONNECTER (désactivé au début)
        self.login_bt = ttk.Button(
            card,
            text="Se connecter",
            style="Primary.TButton",
            state="disabled",
            command=self.on_login
        )
        self.login_bt.grid(row=6, column=0, columnspan=2, sticky="ew")

        card.columnconfigure(1, weight=1)

    def check_login(self, email, mdp):
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(
                "SELECT id FROM inscription WHERE email = ? AND mdp = ?",
                (email, mdp)
            )
            row = cur.fetchone()
            conn.close()
        except Exception as e:
            messagebox.showerror("Erreur", f"Problème avec la base d'inscriptions :\n{e}")
            return False

        return row is not None

    def validate_form(self):
        """Validation : champs non vides + mdp min 5 caractères"""
        email = self.email_en.get().strip()
        mdp = self.mdp_en.get()

        self.error_lb.config(text="", foreground="red")

        if not email or not mdp:
            self.error_lb.config(text="Veuillez remplir tous les champs.")
            self.login_bt.config(state="disabled")
            return

        if len(mdp) != 5:
            self.error_lb.config(text="Le mot de passe doit contenir 5 caractères.")
            self.login_bt.config(state="disabled")
            return

        # Si tout est OK
        self.error_lb.config(text="Validé !", foreground="green")
        self.login_bt.config(state="normal")

        self.form_is_valid = True
        self.login_bt.config(state="normal")

    def on_login(self):
        """Appelé quand on clique sur 'Se connecter' après validation."""
        if not self.form_is_valid:
            # au cas où quelqu'un clique sans avoir validé
            self.validate_form()
            if not self.form_is_valid:
                return

        email = self.email_en.get().strip()
        mdp = self.mdp_en.get()

        if not self.check_login(email, mdp):
            self.error_lb.config(text="Email ou mot de passe incorrect.", foreground="red")
            self.login_bt.config(state="disabled")
            return

        if hasattr(self.master, "is_logged_in"):
            self.master.is_logged_in = True

        if hasattr(self.master, "btn_reserver"):
            self.master.btn_reserver.config(state="normal")

        # Activer les boutons dans l'app principale
        if hasattr(self.master, "btn_gestion"):
            self.master.btn_gestion.config(state="normal")

        if hasattr(self.master, "btn_reservations"):
            self.master.btn_reservations.config(state="normal")

        if hasattr(self.master, "btn_importer"):
            self.master.btn_importer.config(state="normal")

        if hasattr(self.master, "btn_exporter"):
            self.master.btn_exporter.config(state="normal")

        messagebox.showinfo("Connexion réussie", "Vous êtes maintenant connecté.")
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    win = LoginWindow(root)
    win.mainloop()


