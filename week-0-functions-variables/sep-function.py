#Ask user for their name
name = input("What's your name? ")

#Say hello to user

#Using end="" prevents the print function from moving to the next line
print("hello, ", end="")
print(name)

#Using sep="  " defines how much space by default should the program give when you concatenate
print("hello,", name, sep="  ")