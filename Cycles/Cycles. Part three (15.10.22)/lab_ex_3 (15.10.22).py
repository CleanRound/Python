import sys

try:
    num_1 = int(input('Enter the size of a square side: '))
    for width in range(num_1):
        for length in range(num_1):
            if width == 0 or length == 0 or width == num_1 - 1 or length == num_1 - 1:
                sys.stdout.write("*  ")
            else:
                sys.stdout.write("   ")
        print('')
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')