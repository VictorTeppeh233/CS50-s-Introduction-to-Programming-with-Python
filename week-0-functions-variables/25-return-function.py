# creates a main function
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# creates a square function
def square(n):
    return n * n

# calls the main function
main()
