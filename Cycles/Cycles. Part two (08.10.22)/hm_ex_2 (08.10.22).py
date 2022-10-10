try:
    num_1 = map(int, input("Enter the number: ").split())
    symbol = input("Enter the symbol: ")

    for num in num_1:
        print('\n'.join(symbol*num))
except Exception as err:
    print(f'Error: {err}')
finally:
    print("The program has finished.")