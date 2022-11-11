import random
import math

size = int(input('Enter the size of a list: '))
begin = int(input('Enter the beginning of a list: '))
end = int(input('Enter the end of a list: '))

my_list = list()
my_list.sort()
for i in range(size):
    my_list.append(random.randint(begin, end))

for i in range(0, len(my_list)):
    print(f'{my_list[i]}[{i}]', end=' ')
print()

mul = 1
for i in range(0, len(my_list), 3):
    print(f'{mul} * {my_list[i]}[{i}] = ', end=' ')
    mul *= my_list[i]
    print(mul)

product = math.prod(my_list[1:-1]) if len(my_list) > 2 else 0

sum_list1 = sum(my_list[1:-1]) if len(my_list) > 2 else 0

sum_list = [0] * 3

for item in my_list:
    if item < 0:
        sum_list[0] += item
    if item % 2 == 0:
        sum_list[1] += item
    if item % 2 != 0:
        sum_list[2] += item

print(f'Sum negative: {sum_list[0]}')
print(f'Sum even: {sum_list[1]}')
print(f'Sum odd: {sum_list[2]}')
print(f'Mul even 3 index: {mul}')
print(f'Product of min and max element: {product}')
print(f'Sum of elements between the first and the last: {sum_list1}')
