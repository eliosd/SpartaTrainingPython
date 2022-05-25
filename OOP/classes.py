# class Dog:
#     def __init__(self, name, colour):  # initialise
#         self.animal_type = "canine"
#         self.legs = 4
#         self.name = name
#         self.colour = colour
#
#
#     def bark(self):  # method
#         return f"Woof! I am {self.animal_type}"
#
# fido = Dog("Fido", "Black")  # instantiation = creating an INSTANCE of the class
#
# print(fido.animal_type)
# print(fido.name)
# print(fido.colour)


# class Spartan:
#     def __init__(self, firstname, lastname, stream):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.stream = stream
#
# elios = Spartan("Elios", "Dauti", "Data Engineering")
# sam = Spartan(
#     firstname="Sam",
#     lastname="Rustle",
#     stream="Data Engineering"
# )
#
#
# print(elios.firstname)
# print(sam.lastname)
# print(elios.stream)


class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.__speed = 0  # protected variable, dunder ".__" makes it immutable

    def accelerate(self, accel):
        if self.__speed + accel > self.top_speed:
            self.__speed = self.top_speed
            #  self.speed = min(self.speed + accel, self.top_speeD)
            return "Car has reached it's top speed"
        else:
            self.__speed += accel
            return self.__speed

    def brake(self, brake):
        if self.__speed - brake < 0:
            return "Car is stationery"
        else:
            self.__speed -= brake
            return self.__speed

    def get_speed(self):
        return self.__speed

car1 = Car("BMW", "M4", 180)


print(car1.accelerate(50))
print(car1.brake(20))
print(car1.accelerate(200))
