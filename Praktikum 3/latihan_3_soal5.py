saldo = 500000

while True:
    print("\nSaldo Anda saat ini:", saldo)
    try:
        teks = input("Masukkan nominal tarik tunai (atau ketik 'q' untuk keluar): ")
        if teks.lower() == 'q':
            print("Terima kasih, program selesai.")
            break

        nominal = int(teks)

        if nominal <= 0:
            raise Exception("Nominal harus lebih dari 0!")

        if nominal > saldo:
            raise Exception("Saldo tidak mencukupi!")

        saldo -= nominal
        print("Tarik tunai berhasil! Sisa saldo Anda:", saldo)

    except ValueError:
        print("Error: Nominal yang dimasukkan harus berupa angka!")
    except Exception as e:
        print("Error:", e)
