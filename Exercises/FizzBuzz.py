print("Welcome to FizzBuzz!")

number = int(input("Enter a number between 1 - 100: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)



# for count in range(1, 51):
#     if count % 3 == 0 and count % 5 == 0:
#         print("FizzBuzz")
#     elif count % 3 == 0:
#         print("Fizz")
#     elif count % 5 == 0:
#         print("Buzz")
#     else:
#         print(count)