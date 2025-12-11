import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ReservationTree(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Réservations")
        self.configure(bg="#f3f4f6")
        self.geometry("595x300")
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
        self.columns = ("l_name", "f_name", "phone", "date", "hour", "nb")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings", height=300)
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
        self.tree.grid(row=0, column=0, sticky="nsew")

    def write_tree(self):
        """Load all reservations from the database into the Treeview."""
        # Clear the table first
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            conn = sqlite3.connect("reservation.db")
            cur = conn.cursor()
            cur.execute("SELECT prenom, nom, telephone, date, heure, nb_personnes FROM reservations")
            rows = cur.fetchall()
            conn.close()

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger les réservations :\n{e}")
            return

        # Insert rows in the right order
        for prenom, nom, telephone, date, heure, nb_personnes in rows:
            # Treeview order: l_name, f_name, phone, date, hour, nb
            self.tree.insert(
                "", "end",
                values=(nom, prenom, telephone, date, heure, nb_personnes)
            )



#if __name__ == "__main__":
#    root = tk.Tk()
 #   root.withdraw()
 #   win = ReservationTree(root)
  #  win.mainloop()
