h = "Hello World!"

# double = "Double Quotes"
# single = 'Single Quotes'

# print(h, double, single)

# double_in_single = 'I said "Oh No!"'

# both = 'I said "Oh No! David\'s in trouble!"'
# print(both)

# string_block = """
# All of this is stored as a string
# including spaces
# and lines
# """

# print(string_block)


# STRING INDEXING & SLICING

# print(h[2:7])

# print(h[:4])

# print(h[1:-1:3])
# print(h[::-1])


# Methods

# print(h.lower())  # lowercase
# print(h.upper())  # uppercase
# print(h.count("l"))  # Counts how many instances of the string as an argument is in the string
# print(h.capitalize())  # Capitalises the first character in a string "Sentence Case"
# print(h.replace("o", "ooooo"))  # Replaces a character (first argument) with a string as second argument
# print(h.split(", "))


# Concatenation

a = "Mr"
b = "Blue"
c = "Sky"

d = "Mambo"
e = "Number"
f = 5

print(a + ". " + b + " " + c)


# F-String

print(f"{d} {e} {f}")

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years * 2} years old in dog years and {height_cm:.1f}cm tall.")
# Anything after colon specifies format

