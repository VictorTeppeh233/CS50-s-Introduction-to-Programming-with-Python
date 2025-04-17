#introducing while loop
while True:
#try runs the code
    try:
        x = int(input("What's x? "))
        #break stops the loop when the code in try is successful and skips the except code
        break
    #except ValueError runs when the code in try doesn't run
    except ValueError:
        print("x is not an integer")

#this gets printed when code in try runs
print(f"x is {x}")