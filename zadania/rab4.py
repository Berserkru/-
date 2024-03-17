class mebel:
    def __init__(self, name, material, price):
        self.name = name
        self.material = material
        self.price = price
    def description(self):
        print("Мебель -", self.name, "Материал -", self.material, "Цена -",  self.price)
mebel1 = mebel("Стол", "Дерево", 10000)
mebel1.description()