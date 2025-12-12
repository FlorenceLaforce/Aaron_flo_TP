import tkinter as tk
from tkinter import ttk
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime


class GraphWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Graphique des réservations par jour")
        self.geometry("700x500")
        self.configure(bg="#f3f4f6")

        self.build_ui()
        self.draw_graph()

    def build_ui(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(expand=True, fill="both")

        title = ttk.Label(frame, text="GRAPHIQUE", font=("Segoe UI", 16, "bold"))
        title.pack(pady=10)

        self.canvas_frame = ttk.Frame(frame)
        self.canvas_frame.pack(expand=True, fill="both")

    def draw_graph(self):
        # Nettoyer l'ancien graphique si on redessine
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        # Récupérer les données dans la BD
        conn = sqlite3.connect("reservation.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT date, COUNT(*)
            FROM reservations
            GROUP BY date
            ORDER BY date
        """)
        data = cur.fetchall()
        conn.close()

        # Si aucune donnée
        if not data:
            empty_lb = ttk.Label(
                self.canvas_frame,
                text="Aucune réservation à afficher pour l’instant.",
                font=("Segoe UI", 12)
            )
            empty_lb.pack(expand=True)
            return

        data.sort(key=lambda row: datetime.strptime(row[0], "%d/%m/%Y"))

        dates = [row[0] for row in data]
        counts = [row[1] for row in data]

        # Figure plus "pro"
        fig = Figure(figsize=(7.2, 4.2), dpi=110)
        ax = fig.add_subplot(111)

        # Bar chart
        bars = ax.bar(dates, counts, width=0.75)

        # Titres / labels plus clean
        ax.set_title("Réservations par jour", fontsize=14, fontweight="bold", pad=12)
        ax.set_xlabel("Date (JJ/MM/AAAA)", fontsize=10, labelpad=10)
        ax.set_ylabel("Nombre de réservations", fontsize=10, labelpad=10)

        # Grille plus discrète + sous les barres
        ax.set_axisbelow(True)
        ax.grid(axis="y", linestyle="--", linewidth=0.8, alpha=0.35)

        # Enlever les bordures inutiles
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Ticks X (rotation + lisibilité)
        ax.tick_params(axis="x", labelrotation=45, labelsize=9)
        ax.tick_params(axis="y", labelsize=9)

        # Un peu d’espace au-dessus des barres
        max_y = max(counts)
        ax.set_ylim(0, max_y + max(1, int(max_y * 0.15)))

        # Afficher la valeur au-dessus de chaque barre
        for rect, val in zip(bars, counts):
            ax.annotate(
                str(val),
                (rect.get_x() + rect.get_width() / 2, rect.get_height()),
                textcoords="offset points",
                xytext=(0, 5),
                ha="center",
                fontsize=9
            )

        # Ajuster les marges pour que ça coupe pas les dates
        fig.tight_layout()

        # Intégration Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
