from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def tulangbelakang(self):
        pass

    @abstractmethod
    def organnafas(self):
        pass

    @abstractmethod
    def kaki(self):
        pass

hewan = Hewan()

class Kucing(Hewan):
    def tulangbelakang(self):
        return True
    def organnafas(self):
        return 'Paru-paru'
    def kaki(self):
        return 4

class Ikan(Hewan):
    def tulangbelakang(self):
        return True
    def organnafas(self):
        return 'Insang'
    def kaki(self):
        return 0

class Udang(Hewan):
    def tulangbelakang(self):
        return False
    def organnafas(self):
        return 'Insang'
    def kaki(self):
        return 10

kucing = Kucing()
print(kucing.tulangbelakang())
print(kucing.organnafas())
print(kucing.kaki())

ikan = Ikan()
print(ikan.tulangbelakang())
print(ikan.organnafas())
print(ikan.kaki())

udang = Udang()
print(udang.tulangbelakang())
print(udang.organnafas())
print(udang.kaki())

class Burung(Hewan):
    def tulangbelakang(self):
        return True
    def organnafas(self):
        return 'paru-paru dan pundi-pundi udara'

burung = Burung()
print(burung.tulangbelakang())
print(burung.organnafas())
