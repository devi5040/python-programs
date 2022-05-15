class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount

    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=0.02*self.__vehicle_cost
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=0.06*self.__vehicle_cost
        else:
            print("Invalid Vehicle")
        
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount

    def display_vehicle_details(self):
        print(vehicle.get_vehicle_id())
        print(vehicle.get_vehicle_type())
        print(vehicle.get_vehicle_cost())
        print(vehicle.get_premium_amount())

vehicle=Vehicle()
vehicle.set_vehicle_id(1234)
vehicle.set_vehicle_type("Two Wheeler")
vehicle.set_vehicle_cost(10000)
vehicle.set_premium_amount(1000)
vehicle.calculate_premium()
vehicle.display_vehicle_details()