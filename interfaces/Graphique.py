import tkinter as tk
from tkinter import ttk
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Graphique des réservations par heure")
        self.geometry("600x500")
        self.configure(bg="#f3f4f6")

        self.build_ui()
        self.draw_graph()

    def build_ui(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")

        title = ttk.Label(frame, text="Réservations par heure", font=("Segoe UI", 16, "bold"))
        title.pack(pady=10)

        self.canvas_frame = ttk.Frame(frame)
        self.canvas_frame.pack(expand=True, fill="both")

    def draw_graph(self):
        # Récupérer les données dans la BD
        conn = sqlite3.connect("reservation.db")
        cur = conn.cursor()

        cur.execute("""
            SELECT heure, COUNT(*) 
            FROM reservations 
            GROUP BY heure
            ORDER BY heure
        """)

        data = cur.fetchall()
        conn.close()

        heures = [row[0] for row in data]
        count = [row[1] for row in data]

        # Création du graphique matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        ax.bar(heures, count)
        ax.set_xlabel("Heures")
        ax.set_ylabel("Nombre de réservations")
        ax.set_title("Réservations par heure")

        ax.grid(axis='y', linestyle='--', alpha=0.5)

        # Intégration dans Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
