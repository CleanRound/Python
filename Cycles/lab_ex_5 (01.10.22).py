number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

for num in range(number_1, number_2 + 1):
    if num % 2 != 0:
        print(num, end=' ')
else:
    for num in range(number_2, number_1 + 1):
        if num % 2 != 0:
            print(num, end=' ')
