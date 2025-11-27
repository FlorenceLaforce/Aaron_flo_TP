import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurant | Aaroncini")
        self.geometry("1000x650")
        self.configure(bg="#F2F2F2")  # Fond racine
        self.creer_styles()
        self.creer_widget()

    # ======================================================================
    # ███ STYLE TTK GLOBAL (couleurs, boutons, labels, frames)
    # ======================================================================
    def creer_styles(self):

        # Palette
        self.COLOR_BG = "#F2F2F2"
        self.COLOR_PANEL = "#E6E6E6"
        self.COLOR_DARK = "#1C1C1C"
        self.COLOR_ACCENT = "#8B0000"
        self.COLOR_BROWN = "#4E342E"
        self.COLOR_BUTTON = "#333333"
        self.COLOR_BUTTON_HOVER = "#555555"

        # Fonts
        self.FONT_TITLE = ("Segoe UI", 48, "bold")
        self.FONT_SUBTITLE = ("Segoe UI", 18, "italic")
        self.FONT_PANEL_TITLE = ("Segoe UI", 20, "bold")
        self.FONT_BUTTON = ("Segoe UI", 18, "bold")

        # Style ttk
        style = ttk.Style()
        style.theme_use("clam")

        # === Frame claire ===
        style.configure(
            "BG.TFrame",
            background=self.COLOR_BG
        )

        # === Panel gris ===
        style.configure(
            "Panel.TFrame",
            background=self.COLOR_PANEL
        )

        # === Labels généraux ===
        style.configure(
            "Main.TLabel",
            background=self.COLOR_BG,
            foreground=self.COLOR_ACCENT,
            font=self.FONT_TITLE
        )

        style.configure(
            "Sub.TLabel",
            background=self.COLOR_BG,
            foreground=self.COLOR_BROWN,
            font=self.FONT_SUBTITLE
        )

        style.configure(
            "PanelTitle.TLabel",
            background=self.COLOR_PANEL,
            foreground=self.COLOR_DARK,
            font=self.FONT_PANEL_TITLE
        )

        style.configure(
            "Text.TLabel",
            background=self.COLOR_PANEL,
            foreground="#555",
            font=("Segoe UI", 9)
        )

        # === Boutons TTK custom ===
        style.configure(
            "Main.TButton",
            background=self.COLOR_BUTTON,
            foreground="white",
            font=self.FONT_BUTTON,
            relief="flat",
            padding=10
        )

        style.map(
            "Main.TButton",
            background=[("active", self.COLOR_BUTTON_HOVER)]
        )

        style.configure(
            "Panel.TButton",
            background=self.COLOR_BUTTON,
            foreground="white",
            font=self.FONT_BUTTON,
            relief="flat",
            padding=10
        )

        style.map(
            "Panel.TButton",
            background=[("active", self.COLOR_BUTTON_HOVER)]
        )

    # ======================================================================
    # ███ CREATION DES WIDGETS
    # ======================================================================
    def creer_widget(self):

        # ================================================================
        # FRAMES (tous regroupés)
        # ================================================================
        self.frame_principal = ttk.Frame(self, style="BG.TFrame")
        self.frame_principal.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

        self.frame_admin = ttk.Frame(self.frame_principal, style="Panel.TFrame")
        self.frame_admin.grid(row=0, column=0, sticky="ns", padx=(0, 30))

        self.frame_droit = ttk.Frame(self.frame_principal, style="BG.TFrame")
        self.frame_droit.grid(row=0, column=1, sticky="nsew")

        self.frame_export = ttk.Frame(self.frame_admin, style="Panel.TFrame")
        self.frame_export.grid(row=10, column=0, pady=(40, 10))

        # ================================================================
        # LABELS (tous regroupés)
        # ================================================================
        self.titre_admin = ttk.Label(
            self.frame_admin,
            text="ADMIN",
            style="PanelTitle.TLabel"
        )
        self.titre_admin.grid(row=0, column=0, pady=(20, 20))

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
        self.mini_label.grid(row=1, column=0, pady=(0, 30))

        self.label_legende = ttk.Label(
            self.frame_admin,
            text="* Aperçu des réservations",
            style="Text.TLabel"
        )
        self.label_legende.grid(row=3, column=0, pady=(40, 10))

        # ================================================================
        # BOUTONS (tous regroupés)
        # ================================================================

        def create_admin_btn(text, row):
            btn = ttk.Button(
                self.frame_admin,
                text=text,
                style="Panel.TButton"
            )
            btn.grid(row=row, column=0, padx=20, pady=10, sticky="ew")
            return btn

        self.btn_gestion = create_admin_btn("Gestion", 1)
        self.btn_reservations = create_admin_btn("Réservations", 2)
        self.btn_importer = create_admin_btn("Importer", 11)
        self.btn_exporter = create_admin_btn("Exporter", 12)

        def create_main_btn(text, row):
            btn = ttk.Button(
                self.frame_droit,
                text=text,
                style="Main.TButton"
            )
            btn.grid(row=row, column=0, pady=10, ipadx=20)
            return btn

        self.btn_reserver = create_main_btn("Réserver", 2)
        self.btn_connexion = create_main_btn("Connexion", 3)
        self.btn_inscription = create_main_btn("Inscription", 4)


# ======================================================================
# LANCEMENT
# ======================================================================
if __name__ == "__main__":
    App().mainloop()
