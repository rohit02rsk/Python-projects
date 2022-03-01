import art
print(art.logo)
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calc():
    num1 = float(input("What's the first number?: "))
    for sym in operations:
        print(sym)

    should_cont = True
    while should_cont:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What's the other number?: "))

        calc_fun = operations[op_symbol]
        ans = calc_fun(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans} or type 'n' to continue with another calculation:") == "y":
            num1 = ans 
        else:
            should_cont = False
            calc()

calc()