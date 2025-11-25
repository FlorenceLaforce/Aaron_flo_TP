import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant | Aaroncini")
        self.geometry("1000x650")
        self.configure(bg="#F2F2F2")   # gris clair classe
        self.creer_widget()

    def creer_widget(self):

        # === PALETTE MODERNE ===
        COLOR_BG = "#F2F2F2"      # gris clair pro
        COLOR_PANEL = "#E6E6E6"   # gris doux
        COLOR_DARK = "#1C1C1C"    # noir/gris anthracite
        COLOR_ACCENT = "#8B0000"  # rouge foncé élégant
        COLOR_BROWN = "#4E342E"   # brun chocolat
        COLOR_BUTTON = "#333333"  # gris foncé moderne
        COLOR_BUTTON_HOVER = "#555555"

        FONT_TITLE = ("Segoe UI", 48, "bold")
        FONT_SUBTITLE = ("Segoe UI", 18, "italic")
        FONT_PANEL_TITLE = ("Segoe UI", 20, "bold")
        FONT_BUTTON = ("Segoe UI", 18, "bold")

        # === CONFIGURE PRINCIPAL LAYOUT ===
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_principal = tk.Frame(self, bg=COLOR_BG)
        self.frame_principal.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

        self.frame_principal.grid_columnconfigure(0, weight=0)  # colonne admin petite
        self.frame_principal.grid_columnconfigure(1, weight=1)  # zone restaurant large

        # =================== ADMIN PANEL GAUCHE ===================
        self.frame_admin = tk.Frame(self.frame_principal, bg=COLOR_PANEL, bd=0, relief="flat")
        self.frame_admin.grid(row=0, column=0, sticky="ns", padx=(0, 30))

        self.frame_admin.grid_columnconfigure(0, weight=1)

        # Titre admin
        self.titre_admin = tk.Label(
            self.frame_admin,
            text="ADMIN",
            font=FONT_PANEL_TITLE,
            bg=COLOR_PANEL,
            fg=COLOR_DARK
        )
        self.titre_admin.grid(row=0, column=0, pady=(20, 20))

        # Boutons admin
        def create_admin_btn(text, row):
            btn = tk.Button(
                self.frame_admin,
                text=text,
                bg=COLOR_BUTTON,
                fg="white",
                font=FONT_BUTTON,
                activebackground=COLOR_BUTTON_HOVER,
                activeforeground="white",
                relief="flat",
                padx=10, pady=10,
                bd=0
            )
            btn.grid(row=row, column=0, padx=20, pady=10, sticky="ew")
            return btn

        self.btn_gestion = create_admin_btn("Gestion", 1)
        self.btn_reservations = create_admin_btn("Réservations", 2)

        # Petite légende
        self.label_legende = tk.Label(
            self.frame_admin,
            text="* Aperçu des réservations",
            font=("Segoe UI", 9),
            bg=COLOR_PANEL,
            fg="#555"
        )
        self.label_legende.grid(row=3, column=0, pady=(40, 10))


        # =============== ZONE RESTAURANT (DROITE) ==================
        self.frame_droit = tk.Frame(self.frame_principal, bg=COLOR_BG)
        self.frame_droit.grid(row=0, column=1, sticky="nsew")

        self.frame_droit.grid_columnconfigure(0, weight=1)

        # TITRE RESTAURANT
        self.Main_label = tk.Label(
            self.frame_droit,
            text="AARONCINI",
            font=FONT_TITLE,
            fg=COLOR_ACCENT,
            bg=COLOR_BG
        )
        self.Main_label.grid(row=0, column=0, pady=(10, 5), sticky="n")

        self.mini_label = tk.Label(
            self.frame_droit,
            text="Ristorante Italiano",
            font=FONT_SUBTITLE,
            fg=COLOR_BROWN,
            bg=COLOR_BG
        )
        self.mini_label.grid(row=1, column=0, pady=(0, 30), sticky="n")

        # BOUTONS PRINCIPAUX
        def create_main_btn(text, row):
            btn = tk.Button(
                self.frame_droit,
                text=text,
                font=FONT_BUTTON,
                bg=COLOR_BUTTON,
                fg="white",
                activebackground=COLOR_ACCENT,
                activeforeground="white",
                relief="flat",
                pady=12,
                padx=20,
                bd=0
            )
            btn.grid(row=row, column=0, pady=10, ipadx=20)
            return btn

        self.btn_reserver = create_main_btn("Réserver", 2)
        self.btn_connexion = create_main_btn("Connexion", 3)
        self.btn_inscription = create_main_btn("Inscription", 4)

        # ================= BAS DE PAGE (Importer / Exporter) =================
        self.frame_export = tk.Frame(self.frame_admin, bg=COLOR_PANEL)
        self.frame_export.grid(row=10, column=0, pady=(40, 10))

        self.btn_importer = create_admin_btn("Importer", 11)
        self.btn_exporter = create_admin_btn("Exporter", 12)



if __name__ == "__main__":
    App().mainloop()