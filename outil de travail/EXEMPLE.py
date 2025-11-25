import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_PATH = "../member.db"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("360x180")
        self._init_db()
        self._build_ui()

    def _init_db(self):
        self.conn = sqlite3.connect(DB_PATH)
        cur = self.conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS member (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL                     
                    )
                """)
        self.conn.commit()

    # =============================
    # INSERT
    # =============================
    def _insert(self, nom, prenom, email, mdp):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO member(first_name, last_name, email, password)
                VALUES (?, ?, ?, ?)
            """, (prenom, nom, email, mdp))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Cet email existe déjà.")
            return False

    # =============================
    # FETCH ONE
    # =============================
    def _fetch_one(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM member WHERE email = ?", (email,))
        return cur.fetchone()

    # =============================
    # UI BUILD
    # =============================
    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        form = ttk.LabelFrame(self, text="Formulaire")
        form.grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        form.columnconfigure(1, weight=1)
        form.rowconfigure(0, weight=1)

        ttk.Label(form, text="Email :").grid(row=0, column=0, padx=(6, 8), pady=6, sticky="e")
        self.login_email = ttk.Entry(form)
        self.login_email.grid(row=0, column=1, padx=0, pady=6, sticky="ew")

        ttk.Label(form, text="Mot de passe :").grid(row=1, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_pass = ttk.Entry(form, show="*")
        self.ent_pass.grid(row=1, column=1, padx=0, pady=6, sticky="ew")

        self.btn_login = ttk.Button(form, text="Se connecter", command=self.ouvrir_espace_travail)
        self.btn_signin = ttk.Button(form, text="S'inscrire", command=self.ouvrir_espace_inscription)

        self.btn_login.grid(row=2, column=0, columnspan=2, padx=(80, 0), pady=6, sticky="w")
        self.btn_signin.grid(row=2, column=1, columnspan=2, padx=(0, 80), pady=6, sticky="e")

    # =============================
    # LOGIN
    # =============================
    def ouvrir_espace_travail(self):
        email = self.login_email.get().strip()
        mdp = self.ent_pass.get().strip()

        if not email or not mdp:
            messagebox.showwarning("Champs requis", "Veuillez saisir l'email et le mot de passe.")
            return

        row = self._fetch_one(email)
        if row is None:
            messagebox.showerror("Connexion", "Email introuvable.")
            return

        # row = (id, first, last, email, password)
        if mdp != row[4]:
            messagebox.showerror("Connexion", "Mot de passe incorrect.")
            return

        # OK → Ouvrir espace de travail
        win = tk.Toplevel(self)
        win.title("Espace travail")
        ttk.Label(win, text="Bienvenue dans votre espace de travail !", padding=20).pack()

    # =============================
    # INSCRIPTION WINDOW
    # =============================
    def ouvrir_espace_inscription(self):
        self.withdraw()

        self.win_inscription = tk.Toplevel(self)
        self.win_inscription.title("Inscription")
        self.win_inscription.geometry("520x420")
        self.win_inscription.columnconfigure(0, weight=1)

        form = ttk.LabelFrame(self.win_inscription, text="Créer un compte", padding=12)
        form.grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Prénom :").grid(row=0, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_first = ttk.Entry(form)
        self.ent_first.grid(row=0, column=1, pady=6, sticky="ew")

        ttk.Label(form, text="Nom :").grid(row=1, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_last = ttk.Entry(form)
        self.ent_last.grid(row=1, column=1, pady=6, sticky="ew")

        ttk.Label(form, text="Email :").grid(row=2, column=0, padx=(6, 8), pady=6, sticky="e")
        self.signup_email = ttk.Entry(form)
        self.signup_email.grid(row=2, column=1, pady=6, sticky="ew")

        ttk.Label(form, text="Mot de passe :").grid(row=3, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_pwd = ttk.Entry(form, show="*")
        self.ent_pwd.grid(row=3, column=1, pady=6, sticky="ew")

        ttk.Label(form, text="min. 8 caractères", foreground="#888").grid(row=3, column=2, padx=6, pady=6, sticky="w")

        ttk.Label(form, text="Confirmer :").grid(row=4, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_pwd2 = ttk.Entry(form, show="*")
        self.ent_pwd2.grid(row=4, column=1, pady=6, sticky="ew")

        self.chk_var = tk.BooleanVar(value=False)
        chk = ttk.Checkbutton(form, text="J'accepte les conditions d'utilisation", variable=self.chk_var)
        chk.grid(row=5, column=0, columnspan=3, pady=8, sticky="w")

        btns = ttk.Frame(self.win_inscription, padding=(12, 0))
        btns.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))

        btn_retour = ttk.Button(btns, text="Retour", command=self.retour_connexion)
        btn_creer = ttk.Button(btns, text="Créer le compte", command=self.creer_member)

        btn_retour.grid(row=0, column=0, padx=(0, 8), sticky="e")
        btn_creer.grid(row=0, column=1, sticky="w")

    def retour_connexion(self):
        self.deiconify()
        self.win_inscription.destroy()

    # =============================
    # CREATE ACCOUNT
    # =============================
    def creer_member(self):
        prenom = self.ent_first.get().strip()
        nom = self.ent_last.get().strip()
        email = self.signup_email.get().strip()
        mdp = self.ent_pwd.get().strip()
        mdp2 = self.ent_pwd2.get().strip()

        # 1) Vérifications UI
        if not prenom or not nom or not email or not mdp or not mdp2:
            messagebox.showwarning("Champs requis", "Complétez tous les champs.")
            return

        if len(mdp) < 8:
            messagebox.showwarning("Mot de passe", "Au moins 8 caractères.")
            return

        if mdp != mdp2:
            messagebox.showwarning("Mot de passe", "Les mots de passe ne correspondent pas.")
            return

        if not self.chk_var.get():
            messagebox.showwarning("Conditions", "Vous devez accepter les conditions.")
            return

        # 2) Insertion
        if self._insert(nom, prenom, email, mdp):
            messagebox.showinfo("Inscription", "Compte créé avec succès")

            # 3) Reset
            self.ent_first.delete(0, "end")
            self.ent_last.delete(0, "end")
            self.signup_email.delete(0, "end")
            self.ent_pwd.delete(0, "end")
            self.ent_pwd2.delete(0, "end")

            self.ent_first.focus()

if __name__ == "__main__":
    App().mainloop()