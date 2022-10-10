try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    sum = 0
    sum_1 = 0
    sum_2 = 0
    count = 0
    count_1 = 0
    count_2 = 0

    for num in range(num_1, num_2 + 1):
        if num % 2 == 0:
            sum += num
            count += 1
        elif num % 2 != 0:
            sum_1 += num
            count_1 += 1
    for num in range(num_1, num_2 + 1):
        if num % 9 == 0:
            sum_2 += num
            count_2 += 1
    print(f'The sum of even numbers is {sum}')
    print(f'The arithmetic mean of even numbers is {sum // count}')
    print('')
    print(f'The sum of odd numbers is {sum_1}')
    print(f'The arithmetic mean of odd numbers is {sum_1 // count_1}')
    print('')
    print(f'The sum of numbers multiple of 9 is {sum_2}')
    print(f'The arithmetic mean of numbers multiple of 9 is {sum_2 / count_2}')
except Exception as err:
    print(f'Error: {err}')
finally:
    print("The program has finished.")