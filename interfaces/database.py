import sqlite3

DB_NAME = "reservation.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
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


def insert_reservation(prenom, nom, telephone, date, heure, nb_personnes):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO reservations (prenom, nom, telephone, date, heure, nb_personnes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (prenom, nom, telephone, date, heure, nb_personnes))

    conn.commit()
    conn.close()
