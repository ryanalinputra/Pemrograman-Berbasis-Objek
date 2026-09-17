try:
    bil1=9
    bil2=0
    x=bil1/bil2
except ZeroDivisionError as e:
    print(e)
print("<< End Program >>")

import math

try:
    print(math.a)
except AttributeError as e:
    print(e)
print("<< End Program >>")

try:
    from time import datetime
except ImportError as e:
    print(e)
print("<< End Program >>")

try:
    import mymodul
except ModuleNotFoundError as e:
    print(e)
print("<< End Program >>")

try:
    list = [1, 2, 3]
    print(list[3])
except IndexError as e:
    print(e)
print("<< End Program >>")

try:
    harga = {"apel": 25000, "jeruk": 20000, "mangga": 15000}
    harga["anggur"]
except KeyError as e:
    print(e)
print("<< End Program >>")

try:
    list=[]
    x=max(list)
except ValueError as e:
    print(e)
print("<< End Program >>")

try:
    text='Hallo, mari belajar eksepsi'
    print(teks)
except NameError as e:
    print(e)
print("<< End Program >>")

try:
    varString = "Hello"
    varInt = 100
    print(varString + varInt)
except TypeError as e:
    print(e)
print("<< End Program >>")

try:
    with open("sample.txt", mode="r") as file:
        print(file.read())
except Exception as e:
    print(e)
print("<< End Program >>")
