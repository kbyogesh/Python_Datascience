class SuperMarket:
    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount

    def product_details(self):
        #return self.name,self.price,self.discount
        return '{}/{}/{}'.format(self.name,self.price,self.discount)

product1 = SuperMarket('Soap',20,0.04)
product2 = SuperMarket('Shampoo',12,0.05)

print(product1.product_details())
print(product2.product_details())
print(SuperMarket.product_details(product1))