from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title='', authorship='', publicationYear=0):
        self.title = title
        self.authorship = authorship
        self.publicationYear = publicationYear
    @abstractmethod
    def displayDetails(self):
        pass

class Book(LibraryItem):
    def __init__(self, genre='', pageNumber=0, title='', authorship='', publicationYear=0):
        super().__init__(title, authorship, publicationYear)
        self.genre = genre
        self.pageNumber = pageNumber

class DigitalAsset(LibraryItem):
    def __init__(self, fileFormat='', fileSize=0.0, title='', authorship='', publicationYear=0):
        super().__init__(title, authorship, publicationYear)
        self.fileFormat = fileFormat
        self.fileSize = fileSize

class Movie(LibraryItem):
    def __init__(self, duration=0, genre='', title='', authorship='', publicationYear=0):
        super().__init__(title, authorship, publicationYear)
        self.duration = duration
        self.genre = genre

class PrintedBook(Book):
    def __init__(self, coverType='', weight=0.0, genre='', pageNumber=0, title='', authorship='', publicationYear=0):
        super().__init__(genre, pageNumber, title, authorship, publicationYear)
        self.coverType = coverType
        self.weight = weight

class Ebook(Book, DigitalAsset):
    def displayDetails(self):
        pass

class DigitalMovie(DigitalAsset, Movie):
    def displayDetails(self):
        pass

class BlueRay(Movie):
    def __init__(self, resolution='', duration=0, genre='', title='', authorship='', publicationYear=0):
        super().__init__(duration, genre, title, authorship, publicationYear)
        self.resolution = resolution
    def displayDetails(self):
        pass

class DVD(Movie):
    def __init__(self, regionCode = 0, duration=0, genre='', title='', authorship='', publicationYear=0):
        super().__init__(duration, genre, title, authorship, publicationYear)
        self.regionCode = regionCode
    def displayDetails(self):
        pass


