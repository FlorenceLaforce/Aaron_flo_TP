import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import json
from interfaces.signup import SignupWindow
from interfaces.login import LoginWindow
from reservation import ReservationWindow
from Reserv_tree import ReservationTree
from Graphique import GraphWindow

#TODO Ajouter un bouton déconnexion et lorsque nous somme connecter rendre les boutons inscription et connexion disabled

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant | Aaroncini")
        self.geometry("900x700")
        self.configure(bg="#F2F2F2")
        self.init_db()
        self.creer_widget()
        self.is_logged_in = False

    def init_db(self):
        conn = sqlite3.connect("reservation.db")
        cur = conn.cursor()

        cur.execute("""
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prenom TEXT NOT NULL,
                    nom TEXT NOT NULL,
                    telephone TEXT NOT NULL,
                    date TEXT NOT NULL,
                    heure TEXT NOT NULL,
                    nb_personnes INTEGER NOT NULL
                )
            """)

        conn.commit()
        conn.close()

    def creer_widget(self):

        self.resizable(width=False, height=False)

        #COULEURS
        COLOR_BG = "#F2F2F2"  # gris clair pro
        COLOR_PANEL = "#E6E6E6"  # gris doux
        COLOR_DARK = "#1C1C1C"  # noir/gris anthracite
        COLOR_ACCENT = "#8B0000"  # rouge foncé élégant
        COLOR_BROWN = "#4E342E"  # brun chocolat
        COLOR_BUTTON = "#333333"  # gris foncé moderne
        COLOR_BUTTON_HOVER = "#555555"
        COLOR_BUTTON_HOVER2 = "#8B0000"

        #ECRITURE
        FONT_TITLE = ("Segoe UI", 48, "bold")
        FONT_SUBTITLE = ("Segoe UI", 18, "italic")
        FONT_PANEL_TITLE = ("Segoe UI", 20, "bold")
        FONT_BUTTON = ("Segoe UI", 18, "bold")

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Bg.TFrame",
                        background=COLOR_BG,
                        relief= "flat"
        )

        style.configure(
            "Panel.TFrame",
            background=COLOR_PANEL
        )
        style.configure(
            "Main.TLabel",
            background=COLOR_BG,
            foreground=COLOR_ACCENT,
            font=FONT_TITLE
        )

        style.configure(
            "Sub.TLabel",
            background=COLOR_BG,
            foreground=COLOR_BROWN,
            font=FONT_SUBTITLE
        )

        style.configure(
            "PanelTitle.TLabel",
            background=COLOR_PANEL,
            foreground=COLOR_DARK,
            font=FONT_PANEL_TITLE
        )

        style.configure(
            "Text.TLabel",
            background=COLOR_PANEL,
            foreground="#555",
            font=("Segoe UI", 9)
        )

        # === Boutons TTK custom ===
        style.configure(
            "Main.TButton",
            background=COLOR_BUTTON,
            foreground="white",
            font=FONT_BUTTON,
            relief="flat",
            padding=10
        )

        style.map(
            "Main.TButton",
            background=[("active", COLOR_BUTTON_HOVER2)]
        )

        style.configure(
            "Panel.TButton",
            background=COLOR_BUTTON,
            foreground="white",
            font=FONT_BUTTON,
            relief="flat",
            padding=10
        )

        style.map(
            "Panel.TButton",
            background=[("active", COLOR_BUTTON_HOVER)]
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #FRAME
        #principal
        temp_global_weight_var = 0
        self.frame_principal = ttk.Frame(self, style="Bg.TFrame")
        self.frame_principal.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)

        #gauche en haut
        self.frame_top_gauche = ttk.Frame(self.frame_principal, style="Panel.TFrame")
        self.frame_top_gauche.grid(row=0, column=0, sticky="nsew",  padx=(0,20))

        self.frame_top_gauche.grid_columnconfigure(0, weight=1)
        self.frame_top_gauche.grid_rowconfigure(0, weight=0)
        self.frame_top_gauche.grid_rowconfigure(1, weight=0)
        self.frame_top_gauche.grid_rowconfigure(2, weight=0)
        self.frame_top_gauche.grid_rowconfigure(3, weight=0)

        #gauche en bas
        self.frame_bottom_gauche = ttk.Frame(self.frame_principal, style="Panel.TFrame")
        self.frame_bottom_gauche.grid(row=1, column=0, sticky="nsew", padx=(0,20))

        self.frame_bottom_gauche.grid_columnconfigure(0, weight=1)
        self.frame_bottom_gauche.grid_rowconfigure(0, weight=0)
        self.frame_bottom_gauche.grid_rowconfigure(1, weight=0)

        self.frame_bottom_gauche.grid_propagate(False)
        self.frame_bottom_gauche.config(height=200)

        #droite
        self.frame_droit = ttk.Frame(self.frame_principal, style="Bg.TFrame")
        self.frame_droit.grid(row=0, column=1, sticky="nsew")

        self.frame_droit.grid_columnconfigure(0, weight=1)
        self.frame_droit.grid_rowconfigure(0, weight=1)
        self.frame_droit.grid_rowconfigure(1, weight=1)
        self.frame_droit.grid_rowconfigure(2, weight=1)
        self.frame_droit.grid_rowconfigure(3, weight=1)
        self.frame_droit.grid_rowconfigure(4, weight=1)
        #

        #LABEL FRAME DROIT
        self.Main_label = ttk.Label(
            self.frame_droit,
            text="AARONCINI",
            style="Main.TLabel"
        )
        self.Main_label.grid(row=0, column=0, pady=(10, 5))

        self.mini_label = ttk.Label(
            self.frame_droit,
            text="Ristorante Italiano",
            style="Sub.TLabel"
        )
        self.mini_label.grid(row=1, column=0, pady=(0, 20))


        #LABEL FRAME GAUCHE
        self.titre_admin = ttk.Label(
            self.frame_top_gauche,
            text="ADMINISTRATION",
            style="PanelTitle.TLabel"
        )
        self.titre_admin.grid(row=0, column=0, pady=(20, 20))

        self.label_legende = ttk.Label(
            self.frame_top_gauche,
            text="* Aperçu des réservations",
            style="Text.TLabel"
        )
        self.label_legende.grid(row=3, column=0, pady=(40, 10))


        #BUTTON FRAME DROIT
        self.btn_reserver = ttk.Button(self.frame_droit, text = "Réserver", style = "Main.TButton", width=15, command=self.ouvrir_reserver, state="disabled")
        self.btn_reserver.grid(row=2, column=0, pady=10, padx=150, sticky="")

        self.btn_connexion = ttk.Button(self.frame_droit, text = "Connexion",  style = "Main.TButton", width=15, command=self.ouvrir_login)
        self.btn_connexion.grid(row=3, column=0, pady=10, padx=150, sticky="")

        self.btn_inscription = ttk.Button(self.frame_droit, text = "Inscription",  style = "Main.TButton", width=15, command=self.ouvrir_signup)
        self.btn_inscription.grid(row=4, column=0,  pady=10, padx=150, sticky="")

        self.btn_signout = ttk.Button(self.frame_droit, text="Déconexion", style="Panel.TButton", command=self.deco)
        self.btn_signout.grid(row=5, column=0, pady=10, padx=150, sticky="")

        #BUTTON FRAME GAUCHE HAUT
        self.btn_gestion = ttk.Button(self.frame_top_gauche, text = "Gestion", style = "Panel.TButton",  command=self.ouvrir_gestion)
        self.btn_gestion.grid(row=1, column=0, pady=10, padx=30, sticky="")

        self.btn_reservations = ttk.Button(self.frame_top_gauche, text = "Réservations", style = "Panel.TButton", command= self.ouvrir_reservations)
        self.btn_reservations.grid(row=2, column=0, pady=10, padx=30, sticky="")

        #BUTTON FRAME GAUCHE BAS
        self.btn_importer = ttk.Button(self.frame_bottom_gauche, text="Importer", style = "Panel.TButton", command=self.import_json)
        self.btn_importer.grid(row=0, column=0, pady=10, padx=20, sticky="")

        self.btn_exporter = ttk.Button(self.frame_bottom_gauche, text="Exporter",  style = "Panel.TButton", command=self.export_json)
        self.btn_exporter.grid(row=1, column=0, pady=10, padx=20, sticky="")


        # Boutons désactivés avant connexion
        self.btn_gestion.config(state="disabled")
        self.btn_reservations.config(state="disabled")
        self.btn_importer.config(state="disabled")
        self.btn_exporter.config(state="disabled")
        self.btn_signout.config(state="disabled")

        # Boutons autorisés avant connexion
        self.btn_connexion.config(state="normal")
        self.btn_inscription.config(state="normal")

    def ouvrir_login(self):
        LoginWindow(self)

    def ouvrir_signup(self):
        SignupWindow(self)

    def ouvrir_reserver(self):
        ReservationWindow(self)

    def ouvrir_gestion(self):
        ReservationTree(self)

    def ouvrir_reservations(self):
        GraphWindow(self)

    def export_json(self):
        try:
            conn = sqlite3.connect("reservation.db")
            cur = conn.cursor()

            cur.execute("SELECT nom, prenom, telephone, date, heure, nb_personnes FROM reservations")
            data = cur.fetchall()
            conn.close()

            #transformer en dict pour facilititer l'exp.
            formatted = [
                {
                    "nom": row[0],
                    "prenom": row[1],
                    "telephone": row[2],
                    "date": row[3],
                    "heure": row[4],
                    "nb_personnes": row[5]
                }
                for row in data
            ]

            filepath = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json")],
                title="Exporter les réservations"
            )
            if not filepath:
                return
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(formatted, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Exportation", "Exportation réussie.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'exportation:\n{e}")

    def import_json(self):
        try:
            filepath = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json")],
                title="Importer des réservations"
            )

            if not filepath:
                return

            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            conn = sqlite3.connect("reservation.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM reservations")
            conn.commit()

            for entry in data:
                cur.execute("""
                    INSERT INTO reservations (prenom, nom, telephone, date, heure, nb_personnes)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    entry["prenom"],
                    entry["nom"],
                    entry["telephone"],
                    entry["date"],
                    entry["heure"],
                    entry["nb_personnes"]
                ))

            conn.commit()
            conn.close()

            for window in self.winfo_children():
                if isinstance(window, ReservationTree):
                    window.write_tree()

            messagebox.showinfo("Importation", "Importation réussie.")

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'importation:\n{e}")

    def deco(self):
        if not messagebox.askokcancel("Quitter", "Voulez vous fermer votre session?"):
            return

        self.btn_gestion.config(state="disabled")
        self.btn_reservations.config(state="disabled")
        self.btn_importer.config(state="disabled")
        self.btn_exporter.config(state="disabled")
        self.btn_signout.config(state="disabled")

        self.btn_connexion.config(state="normal")
        self.btn_inscription.config(state="normal")

        messagebox.showinfo("Déconnection réussie", "Vous êtes maintenant déconnecté")


if __name__ == "__main__":
    App().mainloop()