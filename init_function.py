class book_shop:

    # constructor
    def __init__(self, title):
        self.title = title

    # Sample method
    def book(self):
        print('The tile of the book is', self.title)


b = book_shop('Sandman')
b.book()
# The tile of the book is Sandman

class book_detail:
    def __init__(self,price=2000):
        self.price = price
        print("Constructor is invoked")
    
    def book_price(self):
        print("The price of book is",self.price)
b1 = book_detail()
b1.book_price()