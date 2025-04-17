#create the main function
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

#create the get_int function
def get_int(prompt):

    #introducing while loop
    while True:
    #try runs the code
        try:
          return int(input(prompt))
        #except ValueError runs when the code in try doesn't run
        except ValueError:
            #pass skips the code and continues the loop
            pass
main()