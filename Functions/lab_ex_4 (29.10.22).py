import math
number = int(input('Enter the number: '))

def cube(number):
    try:
        return math.pow(number, 3)
    except Exception as err:
        print(f'Error: {err}')
print(cube(number))