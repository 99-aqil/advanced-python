class Vehicle:
    def __init__(self, name, speed, mileage, seating_capacity):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def display_info(self):
        print("Vehicle Name:", self.name)
        print("Speed:", self.speed)
        print("Mileage:", self.mileage)

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        final_amount = total_fare + maintenance_charge
        return final_amount


school_bus = Bus("School Volvo", 180, 12, 50)

school_bus.display_info()

print("Fare:", school_bus.fare())
