import datetime
class TBorrower:
    def __init__(self, n, e, i):
        self.__BorrowerName = n
        self.__EmailAddress = e
        self.__BorrowerID = i
        self.__ItemsOnLoan = 0
    def getBorrowerName(self):
        return(self.__BorrowerName)
    def getEmailAddress(self):
        return(self.__EmailAddress)
    def getBorrowerID(self):
        return(self.__BorrowerID)
    def getItemsOnLoan(self):
        return(self.__ItemsOnLoan)
    def updateItemsOnLoan(self, n):
        self.__ItemsOnLoan = self.__ItemsOnLoan + n
    def printDetails(self):
        print(self.__BorrowerName, ';', self.__BorrowerID, ';', end='')
        print(self.__EmailAddress, ';', self.__ItemsOnLoan)

class TLibraryItem:
    def __init__(self, t, a, i): # initialiser method
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__BorrowerID = 0
        self.__DueDate = datetime.date.today()
    def getTitle(self):
        return(self.__Title)
    def getAuthor_Artist(self):
        return(self.__Author_Artist)
    def getItemID(self):
        return(self.__getItemID)
    def getOnLoan(self):
        return(self.__OnLoan)
    def getBorrowerID(self):
        return(self.__BorrowerID)
    def getDueDate(self):
        return(self.__DueDate)
    def Borrowing(self, i, x):
        if x.getItemsOnLoan() < 5:
            self.__OnLoan = True
            self.__BorrowerID = x.getBorrowerID()
            self.__DueDate = self.__DueDate + datetime.timedelta(weeks=1)
            x.updateItemsOnLoan(1)
        else:
            print("too many books on loan")
    def Returning(self, i, x):
        self.__OnLoan = False
        x.updateItemsOnLoan(-1)
    def printDetails(self):
        print(self.__Title, ';', self.__Author_Artist, ';', end =' ')
        print(self.__ItemID, ';', self.__OnLoan, ';', end = ' ')
        print(self.__BorrowerID, ';', self.__DueDate)

class TBook(TLibraryItem):
    def __init__(self, t, a, i): # initialiser method
        TLibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def getIsRequested(self):
        return(self.__IsRequested)
    def getRequestedBy(self):
        return(self.__RequestedBy)
    def RequestBook(self, i, x):
        self.__IsRequested = True
        self.__RequestedBy = x.getBorrowerID()
    def printDetails(self):
        TLibraryItem.printDetails(self)
        print(self.__IsRequested, ';', self.__RequestedBy)

class T_CD(TLibraryItem):
    def __init__(self, t, a, i): # initialiser method
        TLibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def getGenre(self):
        return(self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
    def printDetails(self):
        TLibraryItem.printDetails(self)
        print(self.__Genre)

def DisplayMenu():
    print('1 - Add a new borrower')
    print('2 - Add a new book')
    print('3 - Add a new CD')
    print('4 - Borrow book')
    print('5 - Return book')
    print('6 - Borrow CD')
    print('7 - Return CD')
    print('8 - Request book')
    print('9 - Print all details')
    print('99 - Exit program')
    print
    print('Enter your menu choice: ')

def main():
    Finish = False
    NextBorrowerID = 1
    NextBookID = 1
    NextCD_ID = 1
    while Finish == False:
        DisplayMenu()
        MenuChoice = int(input())
    if MenuChoice == 1: # new borrower
        BName = input("Name: ")
        Email = input("email address: ");
        BorrowerID = NextBorrowerID
        NextBorrowerID = NextBorrowerID + 1
        Borrower = TBorrower(BName, Email, BorrowerID)
    elif MenuChoice == 2: # new book
        Title = input("Title: ")
        Author = input("Author: ")
        ItemID = NextBookID
        NextBookID = NextBookID + 1
        Book = TBook(Title, Author, ItemID)
    elif MenuChoice == 3: # new CD
        Title = input("Title: ")
        Artist = input("Artist: ")
        ItemID = NextCD_ID
        NextCD_ID = NextCD_ID + 1
        CD = T_CD(Title, Artist, ItemID)
    elif MenuChoice == 4: # borrow book
        BorrowerID = input("Borrower ID: ")
        ItemID = input("Book ID: ")
        Book.Borrowing(ItemID, Borrower)
    elif MenuChoice == 5: # return book
        BorrowerID = input("Borrower ID: ")
        ItemID = input("Book ID: ")
        Book.Returning(ItemID, Borrower)
    elif MenuChoice == 6: # borrow CD
        BorrowerID = input("Borrower ID: ")
        ItemID = input("CD ID: ")
        CD.Borrowing(ItemID, Borrower)
    elif MenuChoice == 7: # return CD
        BorrowerID = input("Borrower ID: ")
        ItemID = input("CD ID: ")
        CD.Returning(ItemID, Borrower)
    elif MenuChoice == 8: # request book
        BorrowerID = input("Borrower ID: ")
        ItemID = input("Book ID: ")
        Book.RequestBook(ItemID, Borrower)
    elif MenuChoice == 9: # print all details
        print("Borrower Details")
        Borrower.printDetails()
        print("Book Details")
        Book.printDetails()
        print("CD Details")
        CD.printDetails()
    elif MenuChoice == 99: # end program
        Finish = True
    else:
        print("wrong input")
    input()
main()
