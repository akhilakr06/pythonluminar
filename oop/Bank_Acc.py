class Bank_Acc:
    bname="sbi"
    def accCreate(self,acnum,name):
        self.acnum=acnum
        self.name=name

        self.minbalance = 500
        self.balance=self.minbalance
    def deposit(self,amount):
        self.amount=amount
        print("your",Bank_Acc.bname,"account has beem credited with amount",self.balance)
        # self.amount= int(input("enter the amount to deposit"))
        self.balance += self.amount
        print("your new balance:", self.balance)

    def withdraw(self,amount):
        self.amount=amount
        self.amount = int(input("enter the amount to withdraw"))
        if self.amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= self.amount
            print("your remaining balance is", self.balance)


b = Bank_Acc()
b.accCreate(1231,"Akhila")
b.deposit(2500)
b.withdraw(1500)