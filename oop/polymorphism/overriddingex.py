class P:
    def set(self,a):
        self.a=a
        print("inside A",a)
class B(P):
    def set(self,b):
        self.b=b
        print("inside B",b)
b=B()
b.set(22)