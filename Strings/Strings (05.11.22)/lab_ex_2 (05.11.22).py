from operator import countOf
try:
    list = input('Enter the list separated by commas: ')
    num = input('Enter the number: ')

    count = countOf(list, num)
    print(f'The amount of times the number appears in the list: {count}')
except Exception as err:
    print(f'Error: {err}')