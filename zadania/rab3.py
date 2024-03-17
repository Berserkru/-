class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
    def description(self):
        print("Продукт -", self.name, "Тип -", self.type, "Цена -",  self.price)
product1 = Product("Молоко", "Молочный", 100)
product1.description()
