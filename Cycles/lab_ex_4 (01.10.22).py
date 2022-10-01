number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

for num in reversed(range(number_1, number_2)):
    print(num, end=' ')