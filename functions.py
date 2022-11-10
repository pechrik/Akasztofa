from data import *
from os import system
import time
import random

def menu():
    system('cls')
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
    win = ''
    hiba = 0
    jelenlegiszo = random.randint(0,len(szavak)+1)
    kitalalt = []
    allapot = False
    helyesvalasz = False
    while helyesvalasz != True:
        system('cls')
        print(f'Témakör: {temakorok[jelenlegiszo]}')
        print(szavak[jelenlegiszo])
        Szo(kitalalt, szavak[jelenlegiszo], win)
        Hangman(hiba)
        Betuk()
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
                print(f'A(z) "{valasztottbetu}" betű megtalálható a szóban.')


def Szo(kiirando, jelenlegiszo,kiszervezés):
    listaszo = []
    for betu in jelenlegiszo:
        listaszo.append(betu.lower())
    for i, betu in enumerate(jelenlegiszo):
        if not i in kiirando:
            listaszo[i] = '_'
    vegleges = "".join(listaszo)
    print(vegleges)
    kiszervezés = vegleges

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
    valasz = False
    while valasz != True:
        system('cls')
        print(f'A játék nehézségének módosítása\n\nKönnyű\t10 próbálkozás \t(1)\nKözepes\t5 próbálkozás\t(2)\nNehéz\t3 próbálkozás\t(3)\n')
        nehezseg = input(f'Válasz:')
        if nehezseg == '1':
            system('cls')
            valasz = True
            print('Nehézség beállítva a következőre: Könnyű')
            time.sleep(1.5)
            return nehezseg
        elif nehezseg == '2':
            system('cls')
            valasz = True
            print('Nehézség beállítva a következőre: Közepes')
            time.sleep(1.5)
            return nehezseg
        elif nehezseg == '3':
            system('cls')
            valasz = True
            print('Nehézség beállítva a következőre: Nehéz')
            time.sleep(1.5)
            return nehezseg
        else:
            system('cls')
            print('Hibás válasz')
            time.sleep(1.5)
            valasz = False

def Szavak():
    pass