class InsufficientAmount(Exception):
    pass


class Wallet:
    def __init__(self, money: int = 0):
        self.money = money

    def withdraw(self, amount):
        if amount > self.money:
            print("Exception")
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
            # raise InsufficientAmount("You do not have enough balance for this request")
        self.money = self.money - amount

    def deposit(self, amount):
        self.money = self.money + amount

    def check_balance(self):
        return self.money


