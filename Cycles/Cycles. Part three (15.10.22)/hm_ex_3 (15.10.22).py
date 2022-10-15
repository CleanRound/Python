try:
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    for i in range(num_1, num_2 + 1):
        print("\n\nMultiplication table for %d\n" % (i))
        for j in range(1, 11):
            print("%-5.d * %5.d    = %5.d"
                  % (i, j, i * j))
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')