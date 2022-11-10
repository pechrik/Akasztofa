file = 'words.csv'

#Feladványok adatai
szavak = []
temakorok = []
tippek = []

#Beolvassa a feladványokat és azok egyéb adatait
def BeolvasasSzavak():
    with open('words.csv', 'r', encoding='utf-8') as forras:
        for row in forras:
            halmaz = row.split(';')
            szavak.append(halmaz[0])
            temakorok.append(halmaz[1])
            tippek.append(halmaz[2].strip())