from User import User
from Barang import Barang

def greeting():
    print("="*40)
    print("SELAMAT DATANG DI APLIKASI KASIR APOTEK")
    print("="*40)

def menu_admin():
    print(">> Menu Admin")
    print("1) Lihat data user \n2) Tambah data user \n3) Edit data user \n4) Delete data user \n5) Logout")

def menu_kasir():
    print(">> Menu Kasir")
    print("1) Lihat data barang \n2) Tambah data barang \n3) Edit data barang \n4) Delete data barang \n5) Logout")

user_login = ""

def login():
    global user_login
    print("\nSilahkan masukkan username dan password ")
    usernamelogin = input("Username : ")
    passwordlogin = input("Password : ")
    level_login = usr.login(usernamelogin, passwordlogin)
    user_login = usernamelogin
    if level_login:
        usr.insert_data_log(user_login, "Login")
    return level_login

usr = User()
brg = Barang()
greeting()

try:
    level_login = login()
    menu_berlanjut = True
    while (menu_berlanjut):
        if (level_login == "Admin"):
            menu_admin()
            menu = int(input("Masukkan menu yang Anda Inginkan:"))
            if (menu == 1):
                usr.select_data()
                usr.insert_data_log(user_login, "Melihat data user")
            elif (menu == 2):
                nama_baru = input("Masukkan nama :")
                username_baru = input("Masukkan username :")
                password_baru = input("Masukkan password :")
                level_baru = input("Masukkan level :")
                usr.insert_data(nama_baru, username_baru, password_baru, level_baru)
                usr.select_data()
                usr.insert_data_log(user_login, "Menambah data user")
            elif (menu == 3):
                username = input("Masukkan username data yang akan diganti :")
                nama_baru = input("Masukkan nama :")
                password_baru = input("Masukkan password :")
                level_baru = input("Masukkan level :")
                usr.update_data(nama_baru, password_baru, level_baru, username)
                usr.select_data()
                usr.insert_data_log(user_login, "Mengubah data user")
            elif (menu == 4):
                username = input("Masukkan username data yang akan dihapus :")
                usr.delete_data(username)
                usr.select_data()
                usr.insert_data_log(user_login, "Menghapus data user")
            elif (menu == 5):
                usr.insert_data_log(user_login, "Logout")
                level_login = login()
            else:
                usr.insert_data_log(user_login, "Logout")
                menu_berlanjut = False
        elif (level_login == "Kasir"):
            menu_kasir()
            menu = int(input("Masukkan menu yang Anda Inginkan:"))
            if (menu == 1):
                brg.select_data()
                brg.insert_data_log(user_login, "Melihat data barang")
            elif (menu == 2):
                id_baru = input("Masukkan id : ")
                nama_baru = input("Masukkan nama : ")
                stok_baru = input("Masukkan stok : ")
                harga_baru = input("Masukkan harga : ")
                kategori_baru = input("Masukkan kategori : ")
                brg.insert_data(id_baru, nama_baru, stok_baru, harga_baru, kategori_baru)
                brg.select_data()
                brg.insert_data_log(user_login, "Menambah data barang")
            elif (menu == 3):
                id = input("Masukkan id data yang akan diganti :")
                nama_baru = input("Masukkan nama :")
                stok_baru = input("Masukkan stok :")
                harga_baru = input("Masukkan harga :")
                kategori_baru = input("Masukkan kategori : ")
                brg.update_data(nama_baru, stok_baru, harga_baru, kategori_baru, id)
                brg.select_data()
                brg.insert_data_log(user_login, "Mengubah data barang")
            elif (menu == 4):
                id = input("Masukkan id data yang akan dihapus :")
                brg.delete_data(id)
                brg.select_data()
                brg.insert_data_log(user_login, "Menghapus data barang")
            elif (menu == 5):
                brg.insert_data_log(user_login, "Logout")
                level_login = login()
            else:
                brg.insert_data_log(user_login, "Logout")
                menu_berlanjut = False
        else:
            menu_berlanjut = False
except Exception as e:
    print(e)
