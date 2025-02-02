class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"Deposited successfully\nCurrent balance: {self.balance}")

    def withdraw(self, aqwa):
        if self.balance >= aqwa:
            self.balance-=aqwa
            print(f"Withdrawn successfully\nCurrent balance: {self.balance}")
        else:
            print(f"Not enough money on balance\nCurrent balance: {self.balance}")


acc1 = Account("Darkhan", 1000)
acc1.deposit(500)
print("\n")

acc1.withdraw(750)
print("\n")

acc1.withdraw(1000)
print("\n")

acc1.withdraw(10000)
print("\n")
