import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ReservationTree(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Réservations")
        self.configure(bg="#f3f4f6")
        self.geometry("595x375")
        self.resizable(False, False)
        self._configure_style()
        self.build_ui()
        self.write_tree()

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
        self.frm = ttk.Frame(self)
        self.frm.grid(column=0, row=0, sticky="nsew")
        self.frm.columnconfigure(0, weight=3)  # Treeview
        self.frm.columnconfigure(1, weight=1)  # Buttons
        self.frm.rowconfigure(0, weight=1)
        self.frm.rowconfigure(1, weight=0)

        # Treeview
        self.columns = ("l_name", "f_name", "phone", "date", "hour", "nb")
        self.tree = ttk.Treeview(self.frm, columns=self.columns, show="headings", height=15)
        self.tree.heading("l_name", text="Nom")
        self.tree.heading("f_name", text="Prénom")
        self.tree.heading("phone", text="N. de tél.")
        self.tree.heading("date", text="(JJ/MM/AAAA)")
        self.tree.heading("hour", text="Heure")
        self.tree.heading("nb", text="Nb Clients")

        self.tree.column("l_name", width=100)
        self.tree.column("f_name", width=100)
        self.tree.column("phone", width=130)
        self.tree.column("date", width=100)
        self.tree.column("hour", width=82)
        self.tree.column("nb", width=80)
        self.tree.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Boutons d'action
        self.btn_one = ttk.Button(
            self.frm, style='Primary.TButton',
            text='Supprimer Ligne', command=self.del_one
        )
        self.btn_one.grid(row=1, column=0, sticky="nsew", padx=5)

        self.btn_all = ttk.Button(
            self.frm, style='Primary.TButton',
            text='Supprimer Tout', command=self.del_all
        )
        self.btn_all.grid(row=1, column=1, sticky="nsew", padx=5)

    def write_tree(self):
        """Load all DB reservations into the TreeView."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            conn = sqlite3.connect("reservation.db")
            cur = conn.cursor()
            cur.execute("SELECT id, prenom, nom, telephone, date, heure, nb_personnes FROM reservations")
            rows = cur.fetchall()
            conn.close()

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les réservations :\n{e}")
            return

        for row_id, prenom, nom, telephone, date, heure, nb_personnes in rows:
            self.tree.insert(
                "", "end",
                iid=str(row_id),          # store database ID
                values=(nom, prenom, telephone, date, heure, nb_personnes)
            )


    def del_one(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aucun choix", "Veuillez sélectionner une ligne à supprimer.")
            return

        item_id = selected[0]       # Treeview item ID = database ID
        db_id = int(item_id)

        # Confirmation
        if not messagebox.askyesno("Confirmation", "Supprimer cette réservation ?"):
            return
        try:
            conn = sqlite3.connect("reservation.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM reservations WHERE id = ?", (db_id,))
            conn.commit()
            conn.close()
            self.tree.delete(item_id)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer la réservation :\n{e}")


    def del_all(self):
        if not messagebox.askyesno("Confirmation", "Voulez vous vraiment supprimer TOUTES les réservations ?"):
            return
        try:
            conn = sqlite3.connect("reservation.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM reservations")
            conn.commit()
            conn.close()
            for item in self.tree.get_children():
                self.tree.delete(item)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de tout supprimer :\n{e}")
