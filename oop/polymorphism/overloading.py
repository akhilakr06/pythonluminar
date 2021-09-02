class A:
    def set(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
class B(A):
    def set(self,m):
        self.m=m
        print(self.m)
b=B()
b.set(1)