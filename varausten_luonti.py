import sqlite3

#maaritellaan  ja luodaan yhteys
def varausten_luonti(asiakas_id, asiakas_nimi, mokki_id, sposti, saap_pvm, poist_pvm, varaus_tila):
    yhteys = sqlite3.connect('mokkivaraus.db')
    cursor = yhteys.cursor()

    #sijoitetaan varaukseem kuuluvat tiedot ja toteutetaan se
    sql = ''' INSERT INTO varaukset (asiakas_id, mokki_id, sposti, saap_pvm, poist_pvm, varaus_tila)
        VALUES (?, ?, ?, ?, 'Vahvistettu')'''

    #toeutetaan varaukseen sijoitetut tiedot
    cursor.execute(sql, (asiakas_id, mokki_id, sposti, saap_pvm, poist_pvm))
    yhteys.commit()
    yhteys.close()
    print('Varaus on luotu')
