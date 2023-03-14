def str_in_number():
    try:
        num = int(input('Enter the number: '))
        return f'Thank you, you entered {num}'
    except ValueError:
        return f'Error: Non-numeric value entered.'


print(str_in_number())
