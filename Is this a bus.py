class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    pass

School_bus=Bus("School volvo",180,12)
print("Vehicle name:",School_bus.name,"Speed:",School_bus.max_speed,"Mileage:",School_bus.mileage)