class pitomec:
    def __init__(self, name, vid, age):
        self.name = name
        self.vid = vid
        self.age = age
    def description(self):
        print("Питомец -", self.name, "Вид -", self.vid, "Возраст -",  self.age)
pitomec1 = pitomec("Джек", "Обезьяна", 5)
pitomec1.description()