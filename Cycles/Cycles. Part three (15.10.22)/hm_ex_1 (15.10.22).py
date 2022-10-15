try:
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    for num in range(num_1, num_2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')