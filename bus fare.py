class vehicle:
    def __init__(self,capacity):
        self.capacity=capacity
    def fare(self):
        return self.capacity*100
class Bus(vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)
    def fare(self):
        base=super().fare()
        return base+base*0.10
    school_bus=Bus(50)
    print("Final fare:",school_bus.fare)