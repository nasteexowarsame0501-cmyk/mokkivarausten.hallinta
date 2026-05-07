import sqlite3

#luodaan varaukselle testaus


#luodaan ensiksi yhteys tietokantaan
yhteys = sqlite3.connect('mokkivaraus.db')
cursor = yhteys.cursor()
cursor.execute(sql)
yhteys.commit()

print('VARAUSTEN TESTAUS')

#haetaan bvaraukset taulusta kaikki tiedot
try:
    cursor.execute("SELECT * FROM varaukset")
    kaikki_varaukset = cursor.fetchall()

    #kaydaan jokainen rivi lapi ja tulostetaan
    if not kaikki_varaukset:
        print('tietokanta on tyhjä')
    else:
        for varaus in kaikki_varaukset:
            print(f"ID: {varaus[0]} |Asiakas: {varaus[1]} |Mökki numero: {varaus[2]}| Tila: {varaus[4]}")

except sqlite3.OperationalError:
    print("Virhe: Taulu ei loytynyt")

yhteys.close()



