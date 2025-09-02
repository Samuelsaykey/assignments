# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"
    

# Child Class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call the parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
    
    # Method to show phone details
    def phone_details(self):
        return f"{self.device_info()} with {self.storage}GB storage and {self.battery}mAh battery"
    
    # Encapsulation example (private attribute)
    def __reduce_battery(self, usage):
        self.battery -= usage
    
    # Simulating usage
    def use_phone(self, hours):
        usage = hours * 100  # each hour consumes 100mAh
        self.__reduce_battery(usage)
        return f"Battery after {hours}h usage: {self.battery}mAh"
    

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 15", 128, 4200)

print(phone1.phone_details())
print(phone2.phone_details())
print(phone1.use_phone(3))  # Using phone for 3 hours
