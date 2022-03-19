import string
import random


class VehicleInfo:
    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"brand :{ self.brand}")
        print(f"payable tax: {self.compute_tax()}")


class Vehicle:
    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"ID : {self.id}")
        print(f"license plate info: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    def __init__(self):
        self.vehicle_info = {}
        self.add_vehicle_info("Tesla", True, 60000)
        self.add_vehicle_info("Volkswagen", True, 30000)
        self.add_vehicle_info("BMW", False, 40000)


    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(id)
        return Vehicle(id, license_plate, self.vehicle_info[brand] )


class Application:
    def register_vehicle(self, brand: string):
        #create a registry instance
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)

        #print out the vehicle information
        vehicle.print()





app = Application()
app.register_vehicle("Volkswagen")