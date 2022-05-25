print("Welcome to FizzBuzz!")




def fizz_buzz():
    games = int(input("What number do you want to go up to? "))

    for number in range(1, games):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def menu():
    choice = ""

    while choice != "2":
        print("Please select a number from the menu:")
        print("1. Play FizzBuzz")
        print("2. Quit")

        choice = input()

        if choice == "1":
            fizz_buzz()

        elif choice == "2":
            break
        else:
            print("Incorrect input, please try again.")
            print()

menu()