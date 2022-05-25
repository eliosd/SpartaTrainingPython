print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:
def find_divisors(number):
    for i in range(1, int(number) + 1):
        if number % i == 0:
            print(i)

find_divisors(12)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:

def factor(int1, int2):
    if int1 % int2 == 0:
        return True
    else:
        return False

print(factor(12, 5))

# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#             "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:

def pos_letter(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z", " "]
    return str(alphabet.index(letter) + 1)

print(pos_letter("b"))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:

def name_index(name):
    index = []
    id_number = ""
    for char in name:
        find = pos_letter(char)
        index.append(find)
    id_number = "".join(index)
    return id_number

print(name_index("hello"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:

def password(user_id):
    string = name_index(user_id)
    calc = 0
    for i in string:
        string_int = int(i)
        calc = calc + string_int
    return calc

print(password("abc"))

# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:

def is_number_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

print(is_number_prime(11))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:

def is_number_prime(n):
    if n.isnumeric():
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return "Invalid input, please enter a number."

print(is_number_prime("hello"))

# -------------------------------------------------------------------------------------- #