import random
import time

while True:
    print("Salam! Loto oyununa xoş gəldiniz.")
    say_miqdari = int(input("Neçə ədəd daş çıxarılsın? "))

    # Tesadüfi sayı seçmek üçün bir siyahı tertib et
    sayilar = []
    for i in range(say_miqdari):
        say = random.randint(1, 49)
        while say in sayilar:  # Eyni sayını iki defe seçme
            say = random.randint(1, 49)
        sayilar.append(say)

    # İstifadeçinin seçdiyi sayları sırala
    sayilar.sort()

    print("Sizin rəqəminiz:", sayilar)
    print()

    # Torba qarışdırılana qeder 3 saniye gözle
    print("Torba qarışdırılır. Gözləyin...")
    time.sleep(3)