number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

for num in range(number_1, number_2 + 1):
    if num % 7 == 0:
        print(num, end=' ')