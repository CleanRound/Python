try:
    num_1 = int(input('Enter the width of a square: '))
    num_2 = int(input('Enter the length of a square: '))
    for i in range(num_1):
        for j in range(num_2):
            print(f' *', end='')
        print()
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')