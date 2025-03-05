# defining my custom function with default parameter
def hello(to="world"):
    print("hello,", to)

# showing hello message
name = input("What's your name? ")
hello(name)




# using hello without a parameter
hello()