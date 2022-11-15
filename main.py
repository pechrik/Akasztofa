from functions import *

valasz = ''
while valasz != '0':
    BeolvasasSzavak()
    BolvasasStat()
    valasz = menu()
    #Kilépés
    if valasz == '0':
        Kilepes()

    #Új játék
    elif valasz == '1':
        UjJatek()

    #Nehézség
    elif valasz == '2':
        Nehezseg()

    #Szavak Módosítása
    elif valasz == '3':
        Szavak()
    elif valasz == '4':
        Statisztikak()
    MentesStat()
    MentesSzavak()