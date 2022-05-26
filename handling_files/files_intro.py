# try:
#     file = open("order.txt")
# except FileNotFoundError as errormsg:
#     print("File has not been found")
#     print(errormsg)
#     raise
#
# print(file, type(file))

# with open("order.txt") as file:
#     orders = list(map(lambda x: x.strip(), file.readlines()))
#
# print(orders)

with open("order.txt") as file:
    orders = file.read()

print(orders)
order_list = orders.split("\n")
print(order_list)