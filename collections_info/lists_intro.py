shopping_list = ["bread", "bananas", "biscuits", "oat milk"]

# print(shopping_list, type(shopping_list))
#
# # Indexing and Slicing
#
# print(shopping_list[0])
# print(shopping_list[-1])
# print(shopping_list[::-1])
#
#
# # Lists are MUTABLE
#
# shopping_list[0] = "sugar"
# print(shopping_list)


shopping_list.append("cereal")
print(shopping_list)

shopping_list.append("chocolate")
print(shopping_list)

print(len(shopping_list))

shopping_list.remove("biscuits")  # Removes first instance of string parsed
print(shopping_list)

print(shopping_list.pop())
print(shopping_list)


mixed_list = [1, 2, 3, "greetings", True]
print(mixed_list)


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[0])
print(nested_list[0][-1])


print(shopping_list.count("bananas"))
print(shopping_list.index("biscuits"))