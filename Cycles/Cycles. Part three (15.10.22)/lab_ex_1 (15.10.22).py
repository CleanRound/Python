try:
    num_1 = int(input('Enter the square size: '))
    for i in range(num_1):
        for j in range(num_1):
            print(f' *', end='')
        print()
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')