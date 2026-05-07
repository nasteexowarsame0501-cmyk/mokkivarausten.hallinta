import sqlite3

#luodaan maaritykset muokkauksille  ja luodaan yhteys
def varausten_luonti(varaus_id, saap_pvm, poist_pvm):
    yhteys = sqlite3.connect('mokkivaraus.db')
    cursor = yhteys.cursor()

    #muokataan varaukset
    sql = ''' UPDATE varaukset 
         SET saap_pvm = ?, poist_pvm = ?,
         WHERE asiakas_id = ?'''

    #tallennetaan ja tulostetaan kun on onnistunut
    cursor.execute(sql, (saap_pvm, poist_pvm, varaus_id))
    yhteys.commit()
    yhteys.close()
    print(f'Varaus {varaus_id} on muokattu')