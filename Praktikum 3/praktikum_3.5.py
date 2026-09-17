try:
    bil1=9
    bil2=0
    x=bil1/bil2
except IndexError:
    print("Ada kesalahan indeks")
except ZeroDivisionError:
    print("Ada kesalahan pembagian 0")

print("<< End Program >>")

try:
    list = [1, 2, 3]
    print(list[3])
except ZeroDivisionError:
    print("Operasi tidak bisa dijalankan")
except IndexError:
    print("Ada kesalahan indeks")
print("<< End Program >>")

try:
    list = [1, 2, 3]
    print(list[3])
except ZeroDivisionError:
    print("Operasi tidak bisa dijalankan")
except:
    print("Ada kesalahan ")
print("<< End Program >>")

try:
    list = [1, 2, 3]
    print(list[3])
except LookupError:
    print("Ada kesalahan")
except IndexError:
    print("Ada kesalahan indeks")
except:
    print("Ada kesalahan ")
print("<< End Program >>")

try:
    list = [1, 2, 3]
    print(list[3])
except IndexError:
    print("Ada kesalahan indeks")
except LookupError:
    print("Ada kesalahan")
except:
    print("Ada kesalahan ")
print("<< End Program >>")

try:
    bil1=9
    bil2=0
    x=bil1/bil2
except ArithmeticError:
    print("Ada kesalahan aritmatika")
except FloatingPointError:
    print("Ada kesalahan floating point")
except ZeroDivisionError:
    print("Ada kesalahan pembagian 0")
print("<< End Program >>")

try:
    bil1=9
    bil2=0
    x=bil1/bil2
except FloatingPointError:
    print("Ada kesalahan floating point")
except ZeroDivisionError:
    print("Ada pembagian dengan 0")
except ArithmeticError:
    print("Ada kesalahan aritmatika")
print("<< End Program >>")
