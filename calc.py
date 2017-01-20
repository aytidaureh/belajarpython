import os
pil = 'y'
while(pil=='y'):
    os.system("cls")
    prin("===============================")
    print("==    KALKULATOR SEDERHANA   ==")
    print("===============================")
    print("MENU-UTAMA : ")
    print("1 Penjumlahan")
    print("2 Pengurangan")
    print("3 Perkalian")
    print("4 Pembagian")

    def penjumlahan ():
        print("PENJUMLAHAN DUA BUAH BILANGAN")
        print("=============================")
        x = float(input ("Bilangan pertama: "))
        y = float(input ("Bilangan kedua  : "))
        print("-----------------------------")
        print "Jumlah = ", x+y
    def pengurangan ():
        print("PENGURANGAN DUA BUAH BILANGAN")
        print("=============================")
        x = float(input("Bilangan pertama: "))
        y = float(input("Bilangan kedua  : "))
        print("-----------------------------")
        print "Jumlah = ", x-y
    def perkalian ():
        print("PERKALIAN DUA BUAH BILANGAN")
        print("===========================")
        x = float(input("Bilangan pertama: "))
        y = float(input("Bilangan kedua  : "))
        print("---------------------------")
        print "Jumlah = ", x*y
    def pembagian ():
        print("PEMBAGIAN DUA BUAH BILANGAN")
        print("===========================")
        x = float(input("Bilangan pertama: "))
        y = float(input("Bilangan kedua  : "))
        print("---------------------------")
        print "Jumlah = ", x/y
    pilihan = int(input("Masukkan pilihan Anda(1,2,3, dan 4): "))
    if (pilihan==1):
        penjumlahan ()
    elif (pilihan==2):
        pengurangan ()
    elif (pilihan==3):
        perkalian ()
    elif (pilihan==4):
        pembagian ()
    else:
        print("Pilihan Anda salah")
    pil = raw_input("ulang KALKULATOR lagi? (y): ")
