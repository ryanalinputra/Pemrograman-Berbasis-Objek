class Item():
    def __init__(self, Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        self.Code = Code
        self.Title = Title
        self.Description = Description
        self.Category = Category
        self.Picture = Picture
        self.QuantityInStock = QuantityInStock
        self.Price = Price

    def viewFullDescription(self):
        pass
    def addToCart(self):
        pass
    def updateStockLevel(self):
        pass

class DVD(Item):
    def __init__(self, Director='', Certificate='', ListoActors='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.Director = Director
        self.Certificate = Certificate
        self.ListoActors = ListoActors

class MP3(Item):
    def __init__(self, Duration=0, Artist = '', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.Duration = Duration
        self.Artist = Artist

    def playExtract(self):
        pass
    def download(self):
        pass

class Book(Item):
    def __init__(self, ISBN=0 , Author='', Sysnopsis='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.ISBN = ISBN
        self.Author = Author
        self.Sysnopsis = Sysnopsis

    def preview(self):
        pass

Item1 = DVD(
    'raffi ahmad',
    'Dewasa',
    'rama',
    1, 
    'Malam Terakhir',
    'Horor banget',
    'Horor',
    'Gambar malam',
    2,
    100000
)

Item2 = MP3(
    5,
    'raffi ahmad',
    2, 
    'Malam Terakhir',
    'Horor banget',
    'Horor',
    'Gambar malam',
    2,
    100000
)

Item3 = Book(
    5363574746,
    'rama',
    'malam menjadi gelap', 
    9,
    'Horor banget',
    'Horor',
    'Gambar malam',
    2,
    100000
)