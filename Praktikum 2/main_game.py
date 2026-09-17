from game.Sound import play
from game.Sound import pause
from game.Sound import load as load_sound
from game.Level import start
from game.Level import over
from game.Level import load as load_level
from game.Image import open
from game.Image import close
from game.Image import change

def konfirmasi():
    choice = input("Apakah kamu ingin melanjutkan? (y/n): ")
    if choice == "y":
        return False
    else:
        return True

while True:
    print("\n1. Play Sound")
    print("2. Pause Sound")
    print("3. Load Sound")
    print("4. Start Level")
    print("5. Over Level")
    print("6. Load Level")
    print("7. Open Image")
    print("8. Close Image")
    print("9. Change Image")
    print("10. Exit")
    choice = input("Masukkan pilihan: ")
    if choice == "1":
        print("")
        print(play.info_play())
        print("")
        if konfirmasi():
            break
    elif choice == "2":
        print("")
        print(pause.info_pause())
        print("")
        if konfirmasi():
            break
    elif choice == "3":
        print("")
        print(load_sound.info_load())
        print("")
        if konfirmasi():
            break
    elif choice == "4":
        print("")
        print(start.info_start())
        print("")
        if konfirmasi():
            break
    elif choice == "5":
        print("")
        print(over.info_over())
        print("")
        if konfirmasi():
            break
    elif choice == "6":
        print("")
        print(load_level.info_load())
        print("")
        if konfirmasi():
            break
    elif choice == "7":
        print("")
        print(open.info_open())
        print("")
        if konfirmasi():
            break
    elif choice == "8":
        print("")
        print(close.info_close())
        print("")
        if konfirmasi():
            break
    elif choice == "9":
        print("")
        print(change.info_change())
        print("")
        if konfirmasi():
            break
    elif choice == "10":
        break
    else:
        print("Pilihan tidak ada")