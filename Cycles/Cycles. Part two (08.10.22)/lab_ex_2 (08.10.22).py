try:
    num_1 = int(input("Enter the first number: "))
    factorial = 1

    for num in range(1,num_1 + 1):
        factorial = factorial * num
    print(f'The factorial is {factorial}')
except Exception as err:
    print(f'Error: {err}')
finally:
    print("The program has finished.")