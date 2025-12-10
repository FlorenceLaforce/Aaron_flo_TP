import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from database import insert_reservation, init_db



class ReservationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Réserver")
        self.configure(bg="#f3f4f6")
        self.geometry("420x480")
        self.resizable(False, False)
        self._configure_style()
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
        frame_bg = tk.Frame(self, bg="#f3f4f6")
        frame_bg.pack(expand=True, fill="both", padx=20, pady=20)

        card = ttk.Frame(frame_bg, style="Card.TFrame", padding=20)
        card.pack(expand=True, fill="both")

        # Titre
        title_lb = ttk.Label(card, text="Nouvelle réservation", style="Title.TLabel")
        title_lb.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Prénom
        self.prenom_lb = ttk.Label(card, text="Prénom :", style="Form.TLabel")
        self.prenom_lb.grid(row=1, column=0, sticky="w", pady=3)
        self.prenom_en = ttk.Entry(card)
        self.prenom_en.grid(row=1, column=1, sticky="ew", pady=3)

        # Nom de famille
        self.nom_lb = ttk.Label(card, text="Nom de famille :", style="Form.TLabel")
        self.nom_lb.grid(row=2, column=0, sticky="w", pady=3)
        self.nom_en = ttk.Entry(card)
        self.nom_en.grid(row=2, column=1, sticky="ew", pady=3)

        # Téléphone
        self.tel_lb = ttk.Label(card, text="Téléphone :", style="Form.TLabel")
        self.tel_lb.grid(row=3, column=0, sticky="w", pady=3)
        self.tel_en = ttk.Entry(card)
        self.tel_en.grid(row=3, column=1, sticky="ew", pady=3)

        # Date
        self.date_lb = ttk.Label(card, text="Date (JJ/MM/AAAA) :", style="Form.TLabel")
        self.date_lb.grid(row=4, column=0, sticky="w", pady=3)
        self.date_en = ttk.Entry(card)
        self.date_en.grid(row=4, column=1, sticky="ew", pady=3)

        # Heure (liste déroulante 11h à 21h)
        self.heure_lb = ttk.Label(card, text="Heure :", style="Form.TLabel")
        self.heure_lb.grid(row=5, column=0, sticky="w", pady=3)
        heures = [f"{h}:00" for h in range(11, 22)]  # 11 -> 21
        self.heure_cb = ttk.Combobox(card, values=heures, state="readonly")
        self.heure_cb.grid(row=5, column=1, sticky="ew", pady=3)
        self.heure_cb.current(0)

        # Nombre de personnes (1 à 10)
        self.nb_lb = ttk.Label(card, text="Nombre de personnes :", style="Form.TLabel")
        self.nb_lb.grid(row=6, column=0, sticky="w", pady=3)
        nb_values = [str(i) for i in range(1, 11)]
        self.nb_cb = ttk.Combobox(card, values=nb_values, state="readonly")
        self.nb_cb.grid(row=6, column=1, sticky="ew", pady=3)
        self.nb_cb.current(1 if len(nb_values) > 1 else 0)  # par défaut 2 pers

        # Message pour > 10
        self.nb_hint = ttk.Label(
            card,
            text="* Pour plus de 10 personnes, veuillez nous appeler.",
            style="Hint.TLabel"
        )
        self.nb_hint.grid(row=7, column=0, columnspan=2, sticky="w", pady=(0, 5))


        # Label d'erreur
        self.error_lb = ttk.Label(card, text="", style="Error.TLabel")
        self.error_lb.grid(row=9, column=0, columnspan=2, pady=(5, 0))

        # Bouton VALIDER
        self.validate_bt = ttk.Button(
            card,
            text="Valider",
            style="Primary.TButton",
            command=self.validate_form
        )
        self.validate_bt.grid(row=10, column=0, columnspan=2, sticky="ew", pady=(10, 5))

        # Bouton RÉSERVER (désactivé au début)
        self.reserve_bt = ttk.Button(
            card,
            text="Réserver",
            style="Primary.TButton",
            state="disabled",
            command=self.on_reserve
        )
        self.reserve_bt.grid(row=11, column=0, columnspan=2, sticky="ew")

        card.columnconfigure(1, weight=1)

    def validate_form(self):
        """Validation simple de la réservation."""
        prenom = self.prenom_en.get().strip()
        nom = self.nom_en.get().strip()
        tel = self.tel_en.get().strip()
        date_str = self.date_en.get().strip()
        heure = self.heure_cb.get().strip()
        nb = self.nb_cb.get().strip()

        self.error_lb.config(text="", foreground="red")
        self.reserve_bt.config(state="disabled")

        if not prenom or not nom or not tel or not date_str or not heure or not nb:
            self.error_lb.config(text="Veuillez remplir tous les champs obligatoires.")
            return

        if len(tel) != 10:
            self.error_lb.config(text="Veuillez rentrer un téléphone valide (10 numéros)")
            return

        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            self.error_lb.config(text="La date doit être valide et au format JJ/MM/AAAA.")
            return

            # ✅ Refuser les dates dans le passé
        today = datetime.today().date()
        if date_obj < today:
            self.error_lb.config(text="La date ne peut pas être dans le passé.")
            return


        self.error_lb.config(text="Validé !", foreground="green")
        self.reserve_bt.config(state="normal")

    def on_reserve(self):
        """Action quand on clique sur 'Réserver' après validation."""
        prenom = self.prenom_en.get().strip()
        nom = self.nom_en.get().strip()
        tel = self.tel_en.get().strip()
        date = self.date_en.get().strip()
        heure = self.heure_cb.get().strip()
        nb = self.nb_cb.get().strip()

        # Sauvegarde dans la base de données
        try:
            insert_reservation(prenom, nom, tel, date, heure, int(nb))
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d’enregistrer la réservation :\n{e}")
            return

        messagebox.showinfo(
            "Réservation confirmée",
            f"Réservation au nom de {prenom} {nom}\n"
            f"Téléphone : {tel}\n"
            f"Date : {date}\nHeure : {heure}\nPersonnes : {nb}"
        )

        # Fermer la fenêtre après la réservation
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    win = ReservationWindow(root)
    win.mainloop()
