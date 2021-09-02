class Bank:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount to deposit"))
        self.balance+=amount
        print("your new balance:",self.balance)
    def withdraw(self):
        amount = int(input("enter the amount to withdraw"))
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("your remaining balance is",self.balance)
b=Bank()
b.deposit()
b.withdraw()