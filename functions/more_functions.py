def division(denom: int, num: int) -> float:
    return denom / num

a = division(12, 6)

print(a)


# Good Functions
# - Name them clearly, lowercase_with_underscores
# - Clear argument names
# - Functions that don't RETURN something return None
# - Keep them small
# - Use comments
# - Document appropriately
# - Consider type hints

def fizzbuzz_line(num: int):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)

def fizzbuzz_game():
    for i in range(1, 51):
        print(fizzbuzz_line(i))

fizzbuzz_game()