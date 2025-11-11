class vehicles:
    def __init__(self,num_wheels,fuel,color):
        self.__num_wheels = num_wheels
        self.__fuel = fuel
        self.__color = color
    def get_num_wheels(self):
        return self.__num_wheels
    def get_fuel(self):
        return self.__fuel
    def get_color(self):
        return self.__color

Car = vehicles(3,40,"red")
print(Car.get_num_wheels(),Car.get_fuel(),Car.get_color())

#Homework Now inherit a class called car from vehicle with the additional attribute of type and
#type can be "hatch_back". "sedan", "SUV"

class Car(vehicles):
    def __init__(self,hatch_back,Sedan,SUV,num_wheels,fuel,color):