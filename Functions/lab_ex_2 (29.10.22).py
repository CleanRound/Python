number = int(input('Enter the number: '))

def factorial(number):
    try:
        if number == 0:
            return 1
        return number * factorial(number - 1)
    except Exception as err:
        return f'Error: {err}'
print(factorial(number))
