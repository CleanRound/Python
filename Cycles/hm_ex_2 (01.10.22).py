number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

for num in range(number_1, number_2 + 1):
    print(num, end=' ')
print('')
for num in reversed(range(number_1, number_2)):
    print(num, end=' ')
print('')
for num in range(number_1, number_2 + 1):
    if num % 7 == 0:
        print(num, end=' ')
print('')
for num in range(number_1, number_2 + 1):
    if num % 5 == 0:
        print(num, end=' ')