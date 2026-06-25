#Super vehicle class 
class Vehicle:
    def __init__(self, type):
        self.type = type

#class that takes in the attributes year, make, model, door roof and type
#All answers will be inputed but type will be imported from the Vehicle class
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, door, roof):
        Vehicle.__init__(self, type)
        self.year = year
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

# ---application begins---

#ask user for car information
    
type = input("Enter vehicle type: ")
year = int(input("Enter the year: ")) # make sure its an int, could make a while true statement to repeat
make = input("Enter the make: ")
model = input("Enter the model: ")
door = int(input("Enter number of doors (2 or 4): "))#number of doors also int
roof = input("Enter type of roof (solid or sun): ")

#make a new varible that holds all the information
car = Automobile(type, year, make, model, door, roof)

#use car variable to get the values stored to print
print("\nVehicle Type: ", car.type) #\n to create space between imput and putput
print("Year: ", car.year)
print("Make: ", car.make)
print("Model: ", car.model)
print("Number of doors: ", car.door)
print("Type of roof: ", car.roof)