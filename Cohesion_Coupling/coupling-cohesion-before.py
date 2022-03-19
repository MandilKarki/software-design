import string
import random


class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k =2))}-{''.join(random.choices(string.ascii_uppercase,k =2))}"


class Application:
    def register_vehicle(self, brand: string):

        #create a registery instance
        registry = VehicleRegistry()

        #generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)
        print(vehicle_id)

        #now generate a license plate for the vehicle
        #using the first two character of vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)
        print(license_plate)

        #compute the catalog price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 80000
        elif brand == "Volkswagen":
            catalogue_price = 60000
        elif brand == "BMW":
            catalogue_price = 50000

        #compute the tax percentage(default 5% of the catalogue price, except for electric cars which is 2%
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen":
            tax_percentage = 0.02

        #compute the payable tax
        payable_tax = tax_percentage*catalogue_price

        #print out the vehicle registration information
        print("Registration complete, Vehicle Information:")
        print(f"Brand : {brand}")
        print(f"ID: {vehicle_id}")
        print(f"Vehicle license : {license_plate}")
        print(f"Payable tax:{payable_tax}")






app = Application()
app.register_vehicle("Volkswagen")