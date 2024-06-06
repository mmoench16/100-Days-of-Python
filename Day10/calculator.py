from art import logo

#region Function definitions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
#endregion

#region Operations dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#endregion

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    active = True

    while active:
        operation = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        calc_function = operations[operation]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Would you like to continue calculating with {answer}? Type 'y' to continue or 'n' to start new calculation. ") == "y":
            num1 = answer
        else:
            active = False
            calculator()

calculator()