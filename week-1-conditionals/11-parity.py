# Program to tell if a number is even or odd
x = int(input("What's x? "))

# Tells if a number is even or odd by using the remainder when divided by 2
# If the remiander is 0, the number is even, otherwise odd
if x % 2 == 0:
    print("Even")
else:
    print("odd")