print("Welcome to FizzBuzz!")


choice = ""


while choice != "2":
    print("Please select a number from the menu:")
    print("1. Play FizzBuzz")
    print("2. Quit")

    choice = input()

    if choice == "1":
        number = int(input("Enter a number between 1 - 100: "))

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
    elif choice == "2":
        break
    else:
        print("Incorrect input, please try again.")
        print()




# for count in range(1, 51):
#     if count % 3 == 0 and count % 5 == 0:
#         print("FizzBuzz")
#     elif count % 3 == 0:
#         print("Fizz")
#     elif count % 5 == 0:
#         print("Buzz")
#     else:
#         print(count)