import sqlite3

#maaritellaan tietokanta ja luodaan yhteys
def Mokkivaraus_tietokanta():
    yhteys = sqlite3.connect('mokkivaraus.db')
    cursor = yhteys.cursor()

    #toteutetaan taulu
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mokkivaraus (
            asiakas_id INTEGER PRIMARY KEY AUTOINCREMENT,
            asiakas_nimi TEXT,
            sposti TEXT,
            mokki_id INTEGER,
            saap_pvm DATE,
            poist_pvm DATE,
            varaus_tila TEXT
        )
    ''')

    #tallennetaan tietokantaan
    yhteys.commit()
    yhteys.close()
