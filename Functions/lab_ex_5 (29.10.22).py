number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

def max_number(number_1, number_2):
    try:
        if number_1 >= number_2:
            return f'{number_1} is a maximum number'
        else:
            return f'{number_2} is a maximum number'
    except Exception as err:
        return f'Error: {err}'
print(max_number(number_1, number_2))