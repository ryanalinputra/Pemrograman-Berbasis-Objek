class Mamalia:
    def __init__(self, nama):
        self.nama = nama
    def __str__(self):
        return "Nama : "+ self.nama + "."

class Kucing(Mamalia):
    def __init__(self, nama):
        Mamalia.__init__(self, nama)

obj1 = Kucing("Kiwi")
print(obj1)

class Mamalia:
    def __init__(self, nama):
        self.nama = nama
    def __str__(self):
        return "Nama : "+ self.nama + "."

class Kucing(Mamalia):
    def __init__(self, nama):
        super().__init__(nama)

obj2 = Kucing("Berry")
print(obj2)
