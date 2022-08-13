class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, val1, val2):
        return cls(val1 + val2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


number = FixedFloat(18.5796)
new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number.from_sum(1, 2))
print(new_number)

money = Euro(18.786)
print(money)

# print(money.from_sum(1.2, 3.4))
money = Euro.from_sum(16.758, 9.999)
print(money)
