from data import *
from os import system
import time
import random

#Fejléc
def Alcím():
                #     '<--- Menü ---------->
                #     'Érmék:xx
    if nehezseg == 1:
        nehezszoval = '              Könnyű'
    if nehezseg == 2:
        nehezszoval = '             Közepes'
    if nehezseg == 3:
        nehezszoval = '               Neház'
    return nehezszoval

def Alcím2():
    if érmék < 10:
        alcím2 = f'Érmék:0{str(érmék)}{Alcím()}'
    else:
        alcím2 = f'Érmék:{str(érmék)}{Alcím()}'
    return alcím2

def menu():
    # menucim = menuszo.
    system('cls')
    print(f'{BOLDstart}<---------- Menü ---------->\n{Alcím2()}{BOLDend}\n\nKilépés\t\t\t(0)\nÚj játék\t\t(1)\nNehézség módosítása\t(2)\nSzavak módosítása\t(3)\n')
    valasz = input(f'Válasz: ')
    return valasz


def Kilepes():
    system('cls')
    print('Kilépés.')
    time.sleep(0.5)
    system('cls')
    print('Kilépés..')
    time.sleep(0.5)
    system('cls')
    print('Kilépés...')
    time.sleep(0.5)
    system('cls')

def UjJatek():
    system('cls')
    #konstansok
    lose = False
    elerhetobetuk = betuk
    hiba = 0
    jelenlegiszo = random.randint(0,len(szavak)-1)
    kitalalt = []
    helyesvalasz = False

    #játéloop
    while helyesvalasz != True:

        #Játék elemek
        system('cls')
        print(f'Témakör: {temakorok[jelenlegiszo]}')
        Szo(kitalalt, szavak[jelenlegiszo])
        Hangman(hiba)
        Betuk(elerhetobetuk)

        #Ellenőrzés
        valasztottbetu = input('Válassz egy betűt: ').lower()
        if valasztottbetu not in elerhetobetuk:
            system('cls')
            print('Olyan betűt adjon meg, amit még nem használt fel!')
            time.sleep(1.5)
            system('cls')
        else:
            if not valasztottbetu in szavak[jelenlegiszo].lower():
                hiba = hiba + 1
                for i,egybetu in enumerate(elerhetobetuk):
                            if valasztottbetu == egybetu:
                                elerhetobetuk.pop(i)
                print(f'A(z) "{valasztottbetu}" betű nincs a szóban.')
                time.sleep(1)
            else:
                for i,betu in enumerate(szavak[jelenlegiszo]):
                    if betu == valasztottbetu:
                        kitalalt.append(i)
                        for i,egybetu in enumerate(elerhetobetuk):
                            if valasztottbetu == egybetu:
                                elerhetobetuk.pop(i)
                print(f'A(z) "{valasztottbetu}" betű megtalálható a szóban.')
                time.sleep(1)

        #nyerés ellenőrzés
        if len(kitalalt) == len(szavak[jelenlegiszo]):
            system('cls')
            print(f'A keresett szó: {szavak[jelenlegiszo].capitalize()}\nGratulálok, győztél\n\n+1 érme\n\n\n')
            helyesvalasz = True
            ermek = ermek + 1
            input('A továbblépéshez nyomja meg az ENTER gombot!')

        #vesztés ellenőrzés
        if nehezseg == 1:
            if hiba > 9:
                lose = True
        if nehezseg == 2:
            if hiba > 4:
                lose = True
        if nehezseg == 3:
            if hiba > 2:
                lose = True
        if lose == True:
            system('cls')
            print(f'A keresett szó: {szavak[jelenlegiszo].capitalize()}\nVesztettél\n')
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n\n')
            helyesvalasz = True
            input('A továbblépéshez nyomja meg az ENTER gombot!')

        #Segítség felajánlása
        tipp = False
        if nehezseg == 1:
            if hiba == 9:
                tipp = True
        if nehezseg == 2:
            if hiba == 4:
                tipp = True
        if nehezseg == 3:
            if hiba == 2:
                tipp = True
        if tipp == True:
            choice = False
            while choice != True:
                system('cls')
                print('Már csak egy próbálkozása maradt.\nSzeretne segíséget kérni?')
                if érmék < 10:
                    alcím3 = f'Érmék:0{str(érmék)}'
                else:
                    alcím3 = f'Érmék:{str(érmék)}'
                print('\nNem kérek segítséget\t\t(0)')
                print('Egy betű megadása\t1 érme\t(1)')
                print('Szó definíciója\t\t5 érme\t(2)')
                print(f'{BOLDstart}{alcím3}{BOLDend}')
                choice = input('\nVálasz:')
                if choice == '0':
                    Kilepes()
                    choice = True
                elif choice == '1':
                    input('ddawd')
                elif choice == '2':
                    input('wraaa')
                    choice = True
                else:
                    print('Hibás válasz')
                    choice = False
                    time.sleep(1.5)



def Szo(kiirando, jelenlegiszo):
    listaszo = []
    for betu in jelenlegiszo:
        listaszo.append(betu)
    for i, betu in enumerate(jelenlegiszo):
        if not i in kiirando:
            listaszo[i] = '_'
    vegleges = "".join(listaszo)
    print(vegleges.capitalize())

def Betuk(elerhetobetuk):
    text = ''
    for betu in elerhetobetuk:
        text = text + f' {betu}'
    print(f'Elérhető betűk:{text.upper()}')



def Hangman(hiba):
    if hiba == 0:
        print('\n\n\n\n\n\n\n\n')
    if nehezseg == 1:
        if hiba == 1:
            print('       \n       \n       \n       \n       \n       \n=========\n')
        if hiba == 2:
            print('      |\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 3:
            print('  _____\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 4:
            print('  _____\n  |   |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 5:
            print('  _____\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n')
        if hiba == 6:
            print('  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n')
        if hiba == 7:
            print('  _____\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n')
        if hiba == 8:
            print('  _____\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n')
        if hiba == 9:
            print('  _____\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n')
        if hiba == 10:
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')
    if nehezseg == 2:
        if hiba == 1:
            print('       \n       \n       \n       \n       \n       \n=========\n')
        if hiba == 2:
            print('      |\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 3:
            print('  _____\n      |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 4:
            print('  _____\n  |   |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 5:
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')
    if nehezseg == 3:
        if hiba == 1:
            print('       \n       \n       \n       \n       \n       \n=========\n')
        if hiba == 2:
            print('  _____\n  |   |\n      |\n      |\n      |\n      |\n=========\n')
        if hiba == 3:
            print('  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n')

def Nehezseg():
    loop = False
    while loop != True:
        system('cls')
        if nehezseg == 1:
            nehezszoval = 'Könnyű'
        if nehezseg == 2:
            nehezszoval = 'Közepes'
        if nehezseg == 3:
            nehezszoval = 'Nehéz'
        print(f'A játék nehézségének módosítása\nJelenlegi nehézség:{nehezszoval}\n\nKönnyű\t10 próbálkozás \t(1)\nKözepes\t5 próbálkozás\t(2)\nNehéz\t3 próbálkozás\t(3)\n')
        valasz = input(f'Válasz:')
        if valasz == '1':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Könnyű')
            time.sleep(1.5)
            return valasz
        elif valasz == '2':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Közepes')
            time.sleep(1.5)
            return valasz
        elif valasz == '3':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Nehéz')
            time.sleep(1.5)
            return valasz
        else:
            system('cls')
            print('Hibás válasz')
            time.sleep(1.5)

def Szavak():
    valasz = ''
    while valasz != '0':
        system('cls')
        print('Vissza a főmenübe\t(0)\nSzavak kilistázása\t(1)\nSzó törlése\t\t(2)\nSzó hozzáadása\t\t(3)\n')
        valasz = input('Válasz: ')
        if valasz == '0':
            Kilepes()
        elif valasz == '1':
            Osszesszo()
        elif valasz == '2':
            Szotorles()
        elif valasz == '3':
            Szohozzaad()
        else:
            system('cls')
            print('Hibás válasz')
            time.sleep(1.5)

def Szotorles():
    valasz = False
    while valasz != True:
        system('cls')
        bekertszo = input('Adja meg a törölni kívánt szót: ')
        if not bekertszo.lower() in szavak:
            print('Ilyen szó nem létezik.')
            time.sleep(1.5)
        else:
            for i,szo in enumerate(szavak):
                if bekertszo.lower() == szo:
                    szavak.pop(i)
                    temakorok.pop(i)
                    tippek.pop(i)
            print(f'\nA(z) {bekertszo.capitalize()} törölve.')
            valasz = True
            time.sleep(1.5)


def Osszesszo():
    system('cls')
    for szo in szavak:
        print('\t',szo.capitalize())
    input('\nA továbblépéshez nyomja meg az ENTER billlenytűt!')

def Szohozzaad():
    system('cls')
    szavak.append(input('Adjon meg egy szót: ').lower())
    temakorok.append(input('Adja meg a szó témakörét: ').lower())
    tippek.append(input('Adjon a szóhoz tippet: ').capitalize())

def Segitseg():
    pass