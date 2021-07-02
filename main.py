name = input("Whats your name?")
print ("Hello, " + name + ". I am the comparisoner.")
print ("Give me inputs of two number. Not decimal. Only integer. Then i will compare it.")
print("Do you want to find out the comparison of two decimal numbers or integers?")
x = input("decimal or integer:")
if x == "decimal":
    print ("Decimal:")
    x = input("first number:")
    y = input("second number:")
    if float(x) > float(y):
        print("The first number is bigger")
    elif float(x) < float(y):
        print("The second number is bigger")
    elif float(x) == float(y):
        print("Both numbers are equal.")
elif x == "integer":
    print("Integer:")
    x = input("first number:")
    y = input("second number:")
    if x > y:
        print("The first number is bigger")
    elif x < y:
        print("The second number is bigger")
    elif x == y:
        print("Both numbers are equal.")

