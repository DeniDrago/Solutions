def divide_numbers():
    n1, n2 = int(input('Enter a divisible number: ')), int(input('Enter the divisor of the number: '))
    try:
        return f'Division result = {n1 / n2}'
    except ZeroDivisionError:
        return f"You can't divide by zero."


print(divide_numbers())
