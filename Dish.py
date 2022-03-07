from typing import Any, Type


class Dish:
    name = str
    price = complex
    qty = int

    @property
    def Dish(self, name, price):
        self.name = name
        self.price = price

    def getName(self, name):
        return self.name

    def setPrice(self, price):
        self.price = price

    def getPrice(self, price):
        return self.price

    def setName(self, name):
        self.name = name

    def getQuantity(self, qty):
        return self.qty

    def setQuantity(self, qty):
        self.qty = qty
