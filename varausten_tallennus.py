import sqlite3

#tallennetaan varausten tietoja siten etta tietokannasta voi lukea se

#maaritellaan kaikkien varausten haku ja yhdistetaan se tietokantaan
def hae_kaikki_varaukset():
    yhteys = sqlite3.connect('mokkivaraus.db')
    yhteys = yhteys.cursor()

    #toteutetaan toiminto, jossa otetaan varaukset
    cursor.excecute("SELECT * FROM varaukset")

    #haetaan tiedot kannasta ja muutetaan ne listaksi
    tulokset = yhteys.fetchall()
    for rivi in tulokset:
        #tulostetaan kaikki varaukseen kuuluvat tiedot
        print(rivi)
    yhteys.close()

