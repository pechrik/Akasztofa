from data import *
from functions import *

valasz = ''
while valasz != '0':
    BeolvasasSzavak()
    valasz = menu()
    #Kilépés
    if valasz == '0':
        Kilepes()

    #Új játék
    elif valasz == '1':
        UjJatek()

    #Nehézség
    elif valasz == '2':
        nehezseg = Nehezseg()

    #Szavak Módosítása
    elif valasz == '3':
        pass