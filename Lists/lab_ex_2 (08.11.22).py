import random

try:
    size = int(input('Enter the size of a list: '))
    begin = int(input('Enter the beginning of a list: '))
    end = int(input('Enter the end of a list: '))

    my_list = list()
    for i in range(size):
        my_list.append(random.randint(begin, end))

    for i in range(0, len(my_list)):
        print(f'{my_list[i]}[{i}]', end=' ')
    print()

    result_list_even = list()
    result_list_odd = list()
    result_list_negative = list()
    result_list_positive = list()

    for item in my_list:
        if item % 2 == 0:
            result_list_even.append(item)
        if item % 2 != 0:
            result_list_odd.append(item)
        if item < 0:
            result_list_negative.append(item)
        if item > 0:
            result_list_positive.append(item)

    print(f'List even: {result_list_even}')
    print(f'List odd: {result_list_odd}')
    print(f'List negative: {result_list_negative}')
    print(f'List positive: {result_list_positive}')
except Exception as err:
    print(f'Error: {err}')