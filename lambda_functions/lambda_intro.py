def add_plus_one(num1, num2):
    return num1 + num2 + 1
print(add_plus_one(2, 3))


# Lambda (or anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(6, 1))


# map

savings = [234.00, 555.00, 647.25, 839.00]

bonus = []

for saving in savings:
    bonus.append(saving * 1.1)

print(bonus)


def apply_bonus(saving):
    return saving * 1.1

bonus_map = list(map(apply_bonus, savings))
print(bonus_map)


bonus_lambda = list(map(lambda x: x * 1.1, savings))
squared_bonus = map(lambda x: x ** 2, bonus_lambda)

# print(list(squared_bonus))
print(list(f"{sb:.2f}" for sb in squared_bonus))

# total = sum(bonus_lambda)
# print(total)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

calc_lambda = map(lambda x: x ** 2 + 3, numbers)
# print(list(calc_lambda))

even_numbers = filter(lambda x: x % 2 == 0, calc_lambda)
print(list(even_numbers))


jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]

frmt = filter(lambda x: "Data" in x, jobs)
# print(list(frmt))

rmv = map(lambda x: x.replace("Data ", ""), frmt)
print(list(rmv))