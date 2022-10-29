number = int(input('Enter the first number: '))

def max_number(number):
    try:
        if number >= 0:
            return 'True'
        else:
            return 'False'
    except Exception as err:
        return f'Error: {err}'
print(max_number(number))