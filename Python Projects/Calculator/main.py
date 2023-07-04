import art
import replit
# import replit

print(art.logo)


def addition(n1, n2):
    return n1 + n2


def multiplication(n1, n2):
    return n1 * n2


def minus(n1, n2):
    return n1 - n2


def division(n1, n2):
    return n1 / n2


def calculator():
    decision = 'yes'
    first_no = float(input('Enter the first number : '))
    while (decision == 'yes'):
        print('+\n-\n*\n/')
        operation = input('Pick up an operation : ')
        second_no = float(input('Whats the second number : '))
        if operation == '+':
            result = addition(first_no, second_no)
        elif operation == '-':
            result = minus(first_no, second_no)
        elif operation == '*':
            result == multiplication(first_no, second_no)
        elif operation == '/':
            result == division(first_no, second_no)
        print(f"{first_no} {operation} {second_no} = {result}")
        decide = input(
            f'Type y to continue with {result} or type n to start new calculation\n'
        )

        if decide == 'y':
            first_no = result
        else:
            replit.clear()
            print(art.logo)
            calculator()


calculator()
