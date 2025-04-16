#To be able to handle errors.
#We use try and except
#ValueError is a type of error.
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")