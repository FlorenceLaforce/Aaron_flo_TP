import tkinter as tk
from tkinter import ttk, messagebox

#TODO
#   -créer l'ui
#   -check les infos de login avec le db
#   -pas mal tout dans le fond


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window = tk.Toplevel(self)
        self.window.title("Connexion")
        self.build_ui()

    def build_ui(self):
        pass

