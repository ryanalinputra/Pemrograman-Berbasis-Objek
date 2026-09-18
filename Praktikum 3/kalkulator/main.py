import kalkulator

def konfirmasi():
    konfirmasi = input("\nHitung Lagi? (y/n): ")
    if konfirmasi.lower() == "n":
        exit()

print("=== KALKULATOR ===")
while True:
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Error: Input harus berupa angka")
        konfirmasi()
    try:
        print("\n1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            print("Hasil: ", kalkulator.tambah(a, b))
            konfirmasi()
        elif pilihan == 2:
            print("Hasil: ", kalkulator.kurang(a, b))
            konfirmasi()
        elif pilihan == 3:
            print("Hasil: ", kalkulator.kali(a, b))
            konfirmasi()
        elif pilihan == 4:
            try:
                print("Hasil: ", kalkulator.bagi(a, b))
                konfirmasi()
            except ZeroDivisionError:
                print("Error: Tidak boleh membagi dengan nol")
                konfirmasi()
        else:
            print("Pilihan operasi tidak tersedia")
            konfirmasi()
    except ValueError:
        print("Error: Input harus berupa angka")
        konfirmasi()