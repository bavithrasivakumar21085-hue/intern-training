

# class BankAccount with deposit and withdrawal and balance methods
class BankAccount():
    def __init__(self,balance):
        self.balance= balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("amount is deposited, total balance is",  self.balance)

    def withdrawal(self, amount):
        if amount<= self.balance:
            self.balance-= amount
            print("Your balance amount is,", self.balance)
        else:
            print("insufficient balance")
    def current_balance(self):
        print("your balance is", self.balance)

c1 = BankAccount(10000)
c2 = BankAccount(12000)

c1.deposit(2000)
c1.current_balance()

c2.withdrawal(1000)
c2.current_balance()