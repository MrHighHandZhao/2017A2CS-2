import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
        return (self.__Title)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returing(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title,';',self.__Author__Artist,';', end='')
        print(self.__ItemID,';',self.__OnLoan,';',self.__DueDate)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self):
        self.__IsRequested = True

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre = ''
    def GetGenre(self):
        return(self.__Genre)
    def SetGenre(self,g):
        self.__Genre = g

def main():
    ThisBook = Book('Computing','Sylvia',1234)
    ThisCD = CD('Let it be','Beatles',2345)
    ThisBook.PrintDetails()
    ThisCD.PrintDetails()

main()
