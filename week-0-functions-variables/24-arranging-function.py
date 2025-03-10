#defining the main function
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("helllo,", to)

main()
