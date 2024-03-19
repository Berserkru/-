class Order:
    def __init__(self, number, status="Новый"):
        self.number = number
        self.status = status

    def change_status(self, new_status):
        if new_status in ["Новый", "В обработке", "Отправлен", "Доставлен"]:
            self.status = new_status
            print(f"Статус заказа {self.number} изменен на {self.status}")
        else:
            print("Указан недопустимый статус заказа")

    def check_status(self):
        return self.status

# Создаем объект класса Order
order1 = Order("1428")

# Изменяем статус заказа
order1.change_status("В обработке")
order1.change_status("Отправлен")

# Выводим текущий статус заказа
print("Текущий статус заказа:", order1.check_status())