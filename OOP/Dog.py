class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog."

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"a {self.age * 7} dog-years old dog."
        else:
            return self.__str__()


fido = Dog(5)
print(f"Fido is {fido:dog}")






# n = 0.006454
#
# print(f"Fixed Point: {n:f}")
# print(f"2 decimal points: {n:.2f}")
# print(f"Exponential: {n:e}")
# print(f"Percentage: {n:%}")