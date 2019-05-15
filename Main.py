import os, random
from scripts.myfunc import clear,f,persamaan
import scripts.MBisection as MB
import scripts.RegulaFalsi as RF#,NewtonRaphson

#--------------------------------------------------------------------------------------------------#
#Main Menu dan Pemanggilan fungsi fungsi
#--------------------------------------------------------------------------------------------------#
def method(p):
    pil = 4
    print("Metode yang ingin di gunakan?")
    print("1. Metode Bisection")
    print("2. Regula Falsi")
    print("3. Newton Raphson")
    pil = int(input("Masukkan Pilihan : "))

    if(pil == 1):
        MB.main(pers)
    elif(pil == 2):
        RF.main(pers)
    elif(pil == 3):
        print("belom ada.")
        #NewtonRaphson.main(persp)
    else:
        print("Wrong Input.")
        exit()

    return 0

#--------------------------------------------------------------------------------------------------#
# Input persamaan dan perulangan.
#--------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    clear()
    #Initialisasi Variable
    pil2 = 'y'
    pil3 = 'n'
    while(pil2 == 'y' or pil2 == 'Y'):
        if (pil3 == 'n' or pil3 == 'N'):
            print("ex. x^3 + 2*x^2 - 4*x - 4")
            pers = str(input("Masukkan Persamaan : "))
        print()

        #Pemilihan Metode Numerik
        method(pers)

        print()
        pil2 = input("Ulang ? (y/n) : ")
        if (pil2 =='y' or pil2 == 'Y'):
        	pil3 = input("Ulang dengan Persamaan yang sama ? (y/n) : ")
        	clear()
        else:
            exit()

#--------------------------------------------------------------------------------------------------#
#Langkah-langkah metode Newton Raphson
#1. Ambil satu titik sembarang   x1
#2. Tentukan f '(x)
#3. Hitunglah nilai  f(x1)  dan  f '(x1)
#4. Tentukan nilai   x2   =   x1  -   f(x1) / f '(x1)
#5. Hitunglah nilai  f(x2) .
#Bila nilai f(x2) mendekati 0 , x2 adalah akar persamaan , selesai.
#Bila tidak
#6. Tentukan   x1  =  x2   ( nilai  x1 digantikan  x2 )
#7. Kembali ke langkah 3.
