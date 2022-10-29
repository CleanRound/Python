try:
    string = (input('Enter the string: '))

    reversed_string = ''.join(reversed(string))

    print(reversed_string)
except Exception as err:
    print(f'Error: {err}')
