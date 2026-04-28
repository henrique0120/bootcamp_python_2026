import art
# print(art.logo)

first = int(input("Type the first number: \n"))
operator = input("Type the mathematical operator ")
second = int(input("Type the second number: \n"))

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

print(calc["+"](first, second))

# calculadora = add
# print(calculadora(5, 5))

