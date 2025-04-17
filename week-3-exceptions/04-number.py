#try runs the code
try:
    x = int(input("What's x? "))

#except ValueError runs when the code in try doesn't run
except ValueError:
    print("x is not an integer")

#else runs when the code in try runs without difficulties
else:
    print(f"x is {x}")