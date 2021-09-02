class Vehicle:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        # print("Name=",self.name)
        # print("Colour=",self.colour)


class Bus(Vehicle):
    def capacity(self,seat,name,colour):
        super().__init__(name,colour)
        self.seat=seat
        print("Seat Capacity of Bus",self.seat)
        print("Name=", self.name)
        print("Colour=", self.colour)
b=Bus("","")
b.capacity(20,"bus","blue")
