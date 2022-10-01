number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

for num in range(number_1, number_2 + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz_Buzz", end=' ')
    elif num % 5 == 0:
        print("Buzz", end=' ')
    elif num % 3 == 0:
        print("Fizz", end=' ')
    else:
        print(num, end=' ')