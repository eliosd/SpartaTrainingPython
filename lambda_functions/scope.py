# LEGB

# Local
# Enclosed
# Global
# Built-in

x = 5

def outer(x):
    def inner():
        print(x)
    inner()

outer("hello")