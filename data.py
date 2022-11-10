file = 'words.csv'
betuk = ['a' ,'á' ,'b', 'c', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű', 'v', 'w', 'x', 'y', 'z',]
szamok = [1,2,3,4,5,6,7,8,9]

#Feladványok adatai
szavak = []
temakorok = []
tippek = []

nehezseg = 1

#Beolvassa a feladványokat és azok egyéb adatait
def BeolvasasSzavak():
    with open('words.csv', 'r', encoding='utf-8') as forras:
        for row in forras:
            halmaz = row.split(';')
            szavak.append(halmaz[0])
            temakorok.append(halmaz[1])
            tippek.append(halmaz[2].strip())


print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')