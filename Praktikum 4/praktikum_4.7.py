class Mahasiswa:

    def __init__(self,val1='', val2=0, val3=''):
        self.__nama =val1
        self.nim=val2
        self.__prodi =val3

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.nim

    def get_prodi(self):
        return self.__prodi

mhs1 = Mahasiswa('Alya',1234,'Ilmu Hukum')

# print(mhs1.__nama) # Menyebabkan AttributeError karena __nama bersifat private

print(mhs1.get_nama())
print(mhs1.get_nim())
print(mhs1.get_prodi())
