from HitungBangun.luas import persegi
from HitungBangun.luas import lingkaran
from HitungBangun.volume import kubus
from HitungBangun.volume import tabung


def konfirmasi():
    choice = input("Apakah kamu ingin melanjutkan? (y/n): ")
    if choice == "y":
        return False
    else:
        return True
        
while True:
        print("1. Hitung Luas Persegi")
        print("2. Hitung Luas Lingkaran")
        print("3. Hitung Volume Kubus")
        print("4. Hitung Volume Tabung")
        print("5. Exit")
        choice = input("Masukkan pilihan: ")
        if choice == "1":
            a = float(input("Masukkan panjang: "))
            b = float(input("Masukkan lebar: "))
            print("Luas Persegi: ", persegi.persegi(a,b))
            if konfirmasi():
                break
        elif choice == "2":
            r = float(input("Masukkan jari-jari: "))
            print("Luas Lingkaran: ", lingkaran.lingkaran(r))
            if konfirmasi():
                break
        elif choice == "3":
            s = float(input("Masukkan sisi: "))
            print("Volume Kubus: ", kubus.kubus(s))
            if konfirmasi():
                break
        elif choice == "4":
            r = float(input("Masukkan jari-jari: "))
            t = float(input("Masukkan tinggi: "))
            print("Volume Tabung: ", tabung.tabung(r,t))
            if konfirmasi():
                break
        elif choice == "5":
            break
        else:
            print("Pilihan tidak ada")