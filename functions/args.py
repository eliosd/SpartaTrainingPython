# # Multi args - unknown parameters
# def multiargs(*args):
#     print(args, type(args))
#
# multiargs(1, 2, 3)



# def product(*nums):
#     if len(nums) == 0:
#         return None
#
#     result = 1
#
#     for num in nums:
#         # result = result * num
#         result *= num
#     return result
#
# print(product(1, 1, 4, 2))
# print(product())


# def kwargs_demo(**kwargs):
#     print(kwargs, type(kwargs))
#
# print(kwargs_demo(a="One", b="Two"))


def tip_calc(meal_list, total_cost, tip_pc):
    print("You had: ")

    for meal in meal_list:
        print(f"- {meal}")

    print(f"Your subtotal is: {total_cost}")
    print(f"With a {tip_pc:.0%} tip, the total is {total_cost * (1 + tip_pc)}")

# tip_calc(["Burger", "Pizza"], 18.50, 0.1)

# tip_calc(
#     meal_list=["Pizza", "Burger", "Kebab"],
#     tip_pc=0.1,
#     total_cost=30
# )

def calc_total_cost(**meal_prices):
    # total = 0
    # for price in meal_prices.values():
    #     total += price
    # return total
    return sum(meal_prices.values())

print(calc_total_cost(
    Pizza=8.99,
    Burger=4.50,
    Kebab=9.99
))