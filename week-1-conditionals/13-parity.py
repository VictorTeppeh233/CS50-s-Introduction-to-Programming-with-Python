# main function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# even function
def is_even(n):
    return True if n % 2 == 0 else False

# calls the main function
main()