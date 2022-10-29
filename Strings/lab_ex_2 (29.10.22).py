import re

try:
    string = input('Enter the string: ')

    total_digits = len(re.findall('[0-9]', string))
    total_letters = len(re.findall('[A-z]', string))

    print("Total letters found :-", total_letters)
    print("Total digits found :-", total_digits)
except Exception as err:
    print(f'Error: {err}')