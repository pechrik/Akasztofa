from data import *
from os import system
import time
import random

def menu():
    system('cls')
    print(nehezseg)
    print(f'Menü\n\nKilépés\t\t\t(0)\nÚj játék\t\t(1)\nNehézség módosítása\t(2)\nSzavak módosítása\t(3)\n')
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
        Betuk()

        #Ellenőrzés
        valasztottbetu = input('Válassz egy betűt: ').lower()
        if valasztottbetu not in betuk:
            system('cls')
            print('Olyan betűt adjon meg, amit még nem használt fel!')
            time.sleep(1.5)
            system('cls')
        else:
            if not valasztottbetu in szavak[jelenlegiszo].lower():
                hiba = hiba + 1
                print(f'A(z) "{valasztottbetu}" betű nincs a szóban.')
            else:
                for i,betu in enumerate(szavak[jelenlegiszo]):
                    if betu == valasztottbetu:
                        kitalalt.append(i)
                        for i,egybetu in enumerate(betuk):
                            if valasztottbetu == egybetu:
                                betuk.pop(i)
                print(f'A(z) "{valasztottbetu}" betű megtalálható a szóban.')

        #nyerés ellenőrzés
        if len(kitalalt) == len(szavak[jelenlegiszo]):
            system('cls')
            print(f'A keresett szó: {szavak[jelenlegiszo].capitalize()}\nGratulálok, győztél\n\n+1 érme\n\n\n')
            helyesvalasz = True
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


def Szo(kiirando, jelenlegiszo):
    listaszo = []
    for betu in jelenlegiszo:
        listaszo.append(betu)
    for i, betu in enumerate(jelenlegiszo):
        if not i in kiirando:
            listaszo[i] = '_'
    vegleges = "".join(listaszo)
    print(vegleges.capitalize())

def Betuk():
    pass

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
        print(f'A játék nehézségének módosítása\n\nKönnyű\t10 próbálkozás \t(1)\nKözepes\t5 próbálkozás\t(2)\nNehéz\t3 próbálkozás\t(3)\nJelenlegi nehézség:{nehezszoval}\n')
        valasz = input(f'Válasz:')
        if valasz == '1':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Könnyű')
            time.sleep(1.5)
            return int(valasz)
        elif valasz == '2':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Közepes')
            time.sleep(1.5)
            return int(valasz)
        elif valasz == '3':
            system('cls')
            loop = True
            print('Nehézség beállítva a következőre: Nehéz')
            time.sleep(1.5)
            return int(valasz)
        else:
            system('cls')
            print('Hibás válasz')
            time.sleep(1.5)

def Szavak():
    pass