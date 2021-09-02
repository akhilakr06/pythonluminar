class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        # self.c=c
        c=self.a+self.b
        print("Sum:",c)
    def mul(self):
        c=self.a*self.b
        print("Multiplication:",c)
    def div(self):
        c=self.a/self.b
        print("Division:",c)
    def sub(self):
        c=self.a-self.b
        print("Substraction:",c)

c=Calculator(2,4)
c.sum()
c.mul()
c.div()
c.sub()
