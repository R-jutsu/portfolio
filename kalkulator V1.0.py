import time, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def timer():
    time.sleep(1.1);clear()
    
def erorType(teks):
    try:
        masukan = int(input(teks))
        return masukan
    except ValueError:
        print("\nmasukan angka jir, bukan angka/simbol")
        return 0
    
def tambah():
    angka1 = erorType("\n<angka ke-1>> ")
    angka2 = erorType("<angka ke-2>> ")
    hasil = angka1 + angka2
    print(f"hasil perbandingan dari: {angka1} + {angka2} = {hasil}")
   
def kurang():
    angka1 = erorType("\n<angka ke-1>> ")
    angka2 = erorType("<angka ke-2>> ")
    hasil = angka1 - angka2
    print(f"hasil perbandingan dari: {angka1} - {angka2} = {hasil}")
    
def kali():
    angka1 = erorType("\n<angka ke-1>> ")
    angka2 = erorType("<angka ke-2>> ")
    hasil = angka1 * angka2
    print(f"hasil perbandingan dari: {angka1} x {angka2} = {hasil}")
def bagi():
    angka1 = erorType("\n<angka ke-1>> ")
    angka2 = erorType("<angka ke-2>> ")
    try:
        hasil = angka1 / angka2
        print(f"hasil perbandingan dari: {angka1} ÷ {angka2} = {hasil}")
    except ZeroDivisionError:
        print("\nga bisa dibagi dua co jirlah")
    
def pilihan():
    pilih = erorType("pilih opsi perbandingan:\n=====>> ")
    
    if pilih == 1:tambah()
    elif pilih == 2:kurang()
    elif pilih == 3:kali()
    elif pilih == 4:bagi()
    else: print("matanya di pake om pilihan gada jir")
    
def menu():
    while True:
        print("  =====================  ")
        print(" |KALKULATOR MATEMATIKA| ")
        print("  ---------------------  ")
        print("  1. penjumlahan    = +  ")
        print("  2. pengerangan    = -  ")
        print("  3. perkalian      = *  ")
        print("  4. pembagian      = /  ")
        print("  n. KELUAR              ")
        
        pilihan()
        xy = input("\nENTER ");timer()
        if xy.lower() == "n":
            print("OKEH SEHAT-SEHAT BRO");exit()
        
def petunjuk():
    print('''
    PANDUAN:
    ingat!, ini adalah versi yang baru selesai di
    buat, jadi jangan kebanyakan ngide. pakai
    seperlunya.
    
    fiturnya juga masih seditik dan banyak bug nya.
    jangan mengetik huruf/teks di temoat yang bukan
    tempatnya, karna besar kemungkin akan eror.
    
    ATURAN BUKAN UNTUK DI LANGGAR, JADI PATUHI!!!
    ''')
    input("\nENTER UNTUK MASUK")
    timer()
    menu()
petunjuk()



    
    