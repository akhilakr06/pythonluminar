# same method name same no of arguments
class A:
    def printv(self,name):
        self.name=name
        print("inside A",self.name)
class B(A):
    def printv(self,class1):
        self.class1=class1
        print("inside B",self.class1)
b=B()
b.printv("aaa")
# child class method overrides parent class method