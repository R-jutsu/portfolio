import os, time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def waktu():
    time.sleep(1.2);clear()
    
def tipeEror(teks):
    try:
        masukan = int(input(teks))
        return masukan
    except ValueError:
        print("Masukan angka bro")
        return 0

def masukan_pin():
    percobaan = 7
    while percobaan > 0:
        pin = tipeEror("masukan pin: ")
        if pin == 12345:
            print("pin benar! akses di terama")
            break
        else:
            print("pin salah ")
            waktu();percobaan -= 1
    else:
         for i in range(3600, 1, -1):
             print(f"kamu di blokir! kembali lagi dalam {i} detik");waktu()  
masukan_pin()

saldo = 100000000

def fungsi(teks):
    clear();global saldo
    while True:
        print(f"{teks} tunai".center(20))
        xxx = tipeEror(f"\njumlah {teks}: ");clear()
        if xxx > saldo:
            print("\nsaldo anda tidak cukup")
            waktu()
        elif xxx <= 0:
            print(f"\nlu mau {teks} apa jir")
            waktu()
        else:
            saldo -= xxx
            print(f"STATUS: {teks} berhasil")
            print(f"total {teks}: Rp{xxx}")
            print(f"sisa saldo: Rp{saldo}")
            
            lagi = input(f"\nmau {teks} lagi (y/n): ")
            if lagi == "y": print(" "); clear()
            else:break
            
def transfer_tunai():
    fungsi("tranfer")    

def tarik_tunai():
    fungsi("tarik")

def cek_saldo():
    print(" CEK SALDO\n ".center(30))
    print(f"saldo anda adalah Rp{saldo:,}")
    
def menu():
    while True:
        print(" |======================| ")
        print(" |SIMULASI ATM SEDERHANA| ")
        print("  ======================  ")
        print("  |  c. cek saldo      |  ")
        print("  |  1. tarik tunai    |  ")
        print("  |  2. tranfer tunai  |  ")
        print("  |  3. keluar         |  ")
        print(" ------------------------ ")
        
        pilih = input("\npilih menu: ")
        if pilih == "c":
            cek_saldo()
        elif pilih == "1":
            tarik_tunai()       
        elif pilih == "2":
            transfer_tunai()
        elif pilih == "3":
            exit()
            
        input("\nKEMBALI")
        clear()
menu()