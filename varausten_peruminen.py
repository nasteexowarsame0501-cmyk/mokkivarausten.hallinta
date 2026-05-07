import sqlite3

# maaritellaan varauksen perumiselle oma taulu ja luodaan yhteys
def varausten_peruminen(varaus_id, varaus_tila):
    yhteys = sqlite3.connect('mokkivaraus.db')
    cursor = yhteys.cursor()

   sql = '''UPDATE varaukset SET varaus_tila = 'PERUUTTU' WHERE varaus_id = ?'''

    #tallennetaan ja tulostetaan kun on onnistunut
    cursor.execute(sql, (varaus_id))
    yhteys.commit()
    yhteys.close()

#listaaan aina muutettu muuttuja mukaan, jotta se nakyy tulostuksessa
    print(f'Varaus {varaus_id} on peruttu')