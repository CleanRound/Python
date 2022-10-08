try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    sum = 0
    count = 0

    for num in range(num_1, num_2 + 1):
        sum += num
        count += 1
    print(f'The sum of numbers is {sum}')
    print(f'The arithmetic mean is {sum // count}')
except Exception as err:
    print(f'Error: {err}')
finally:
    print("The program has finished.")