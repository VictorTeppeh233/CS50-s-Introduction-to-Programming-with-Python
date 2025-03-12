# Asks user for x and y
x = int (input("What's x? "))
y = int (input("What's y? "))

# Compares to know if x is less, greater or equal to y.
# Then prints the results.
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")