import sqlite3

def insert_reservation(prenom, nom, telephone, date, heure, nb_personnes):
    conn = sqlite3.connect("reservation.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO reservations (prenom, nom, telephone, date, heure, nb_personnes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (prenom, nom, telephone, date, heure, nb_personnes))

    conn.commit()
    conn.close()
