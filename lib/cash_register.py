#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_name, item_price, quantity=1):
        self.total += item_price * quantity
        self.last_transaction = item_price * quantity
        for x in range(quantity):
            self.items.append(item_name)

    def apply_discount(self):
        if (self.discount == 0):
            print("There is no discount to apply.")
        else:
            self.total -= int(self.total * (self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction