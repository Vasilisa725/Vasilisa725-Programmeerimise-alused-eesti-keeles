#卍
class Building:
    def __init__(self,floors,year_built):
        self.__address = address
        self.__floors = floors
        self.__year_buit = year_built
        

    def displayInfo():
        print(self.__address)
        print(self.__floors)
        print(self.__year_built)
        
    def renovate(self, year):
        if(self.__year_built<year):
            print("ei saa renoveerida hoone")
        else:
            self.__year_built = year
            self.isRenovate = True
            
building = Building("Laikmaa 2",5,1100)
building.displayInfo
building.renovate(2000)
building.displayInfo()

class Library(Building):
    def __init__(self,address,floors,year_built,books):
        super().__init__(address,floors,year_built)
        self.books = []
        
    def display_info():
        super().displayInfo()
        print("aamatude arv:", len(self.books))
        
        
    def list_books:
        for book in self.books:
            print("Nimetus: ", book.title,"author: ", book.author,"year: ",book.year)
            
    def borow_book:
        if book in self.books:
            self.books.isBorrowed = True
        else:
            print("See reemat puudub")
        
    def return_book:
        self.books.isBorrowed = False
        
    def add_book:
        self.books.append(book)
    
    

