class mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print("brand", self.brand)
        print("price", self.price) 

phone = mobile("samsung", 25000)

phone.details()