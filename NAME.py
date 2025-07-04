print("1 - add")
print("2 - subtraction")
print("3 - multiply")
print("4 - divide")
option = int(input("choose an operation: "))
result = 0


if(option   in [1,2,3,4]):
    num1 = float(input("enter first number: "))
    num2 = float(input("enter first number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2


else:
    print("invalid operation entered")

print("the result of the operation is {}".format(result))
