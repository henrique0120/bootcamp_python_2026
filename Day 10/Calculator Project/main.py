import art
print(art.logo)

first = int(input("Type the first number: "))
operator = str(input("\n+\n-\n*\n/\nPick an operator: "))
second = int(input("Type the second number: "))
sumNum = 0

working = True

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(first, operator, second,"=", calc[operator](first, second))
result = calc[operator](first, second)

while working:
    ask = input("Do you want to continue with the previous result? Type 'y' or 'n': \n")
    if ask == "y":
        operator = str(input("\n+\n-\n*\n/\nPick an operator: "))
        nextNum = int(input("What's the next number? \n"))
        sumNum = calc[operator](result, nextNum)
        result = sumNum
        print(result)
    else:
        print(f"Result: {sumNum}")
        print("Bye")
        working = False

# calculadora = add
# print(calculadora(5, 5))

