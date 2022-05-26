# Write mode
# with open("order.txt", "w") as file:
#     file.write("Hello world!")

# Will overwrite contents of file
# If file doesn't exist it will create it

# Append mode
with open("order.txt", "a") as file:
    file.write("Hello world!\n")