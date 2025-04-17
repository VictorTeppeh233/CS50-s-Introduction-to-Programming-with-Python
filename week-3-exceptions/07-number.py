#create the main function
def main():
    x = get_int()
    print(f"x is {x}")

#create the get_int function
def get_int():

    #introducing while loop
    while True:
    #try runs the code
        try:
            x = int(input("What's x? "))

        #except ValueError runs when the code in try doesn't run
        except ValueError:
            print("x is not an integer")
    #loop breaks when code indented in try: runs
        else:
            break
    return x

main()