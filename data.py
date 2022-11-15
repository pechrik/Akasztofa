file = 'words.csv'
BOLDstart = "\033[1m"
BOLDend = "\033[0;0m"
ITALICstart ='\033[1;3m'
ITALICend = '\033[0m'

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

def MentesSzavak():
    with open(file, 'w', encoding='utf-8') as cel:
        for i in range(len(szavak)):
            cel.write(f'{szavak[i]};{temakorok[i]};{tippek[i]}\n')
    szavak.clear()
    temakorok.clear()
    tippek.clear()