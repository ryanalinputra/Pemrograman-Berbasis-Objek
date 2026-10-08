class Mamalia:
    paruparu = True
    def __init__(self,val):
        self.nama = val

class Kucing(Mamalia):
    kaki = 4
    def __init__(self,val):
        self.nama =val

obj1=Kucing('Kiwi')
print(obj1.nama)
print(obj1.kaki)
print(obj1.paruparu)

obj2=Kucing('Berry')
print(obj2.nama)
print(obj2.kaki)
print(obj2.paruparu)

class Mamalia:
    def __init__(self):
        self.paruparu = True

class Kucing(Mamalia):
    def __init__(self,val1, val2, val3):
        super().__init__()
        self.nama=val1
        self.kaki=val2
        self.warna=val3

obj1=Kucing('Kiwi',4,'Golden')
print(obj1.nama)
print(obj1.kaki)
print(obj1.paruparu)
obj2=Kucing('Berry',4, 'Abu')
print(obj2.nama)
print(obj2.kaki)
print(obj2.paruparu)

class Mamalia():
    paruparu = True
    def __init__(self):
        self.gigi = True

    def bergerak(self):
        return 'Berjalan/Berenang'

class Kucing(Mamalia):
    ekor = True
    def __init__(self, val1, val2, val3):
        self.nama = val1
        self.kaki = val2
        self.suara=val3

    def bersuara(self):
        return self.suara

class Mamalia():
    paruparu = True
    def __init__(self):
        self.gigi = True

    def bergerak(self):
        return 'Berjalan/Berenang'

class Kucing(Mamalia):
    ekor = True
    def __init__(self, val1, val2, val3):
        super().__init__() #memanggil konstruktor superclass
        self.nama = val1
        self.kaki = val2
        self.suara=val3

    def bersuara(self):
        return self.suara

obj = Kucing('Kiwi',4,'Meow')
print('Suara : ',obj.bersuara())
print('Kaki : ',obj.kaki)
print('Ekor : ',obj.ekor)
print('Bergerak : ',obj.bergerak())
print('Paru-paru : ',obj.paruparu)
print('Gigi : ',obj.gigi)
