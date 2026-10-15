class Hewan():
    pass

class Kucing(Hewan):
    pass

class Persia(Kucing):
    pass

print(issubclass(Kucing, Hewan))
print(issubclass(Persia, Hewan))
print(issubclass(Hewan, Persia))

kucing1 = Persia()
print(isinstance(kucing1, Persia))
print(isinstance(kucing1, Hewan))
print(isinstance(kucing1, str))