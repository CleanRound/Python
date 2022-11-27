import random
try:

    size = int(input('Enter the size of a list: '))
    begin = int(input('Enter the beginning of a list: '))
    end = int(input('Enter the end of a list: '))
    choice = int(input('1: See a maximum number in a list\n2: See a minimum number un a list\n3: See a reversed '
                   'list\n4: See all prime numbers in a list\n'))

    my_list = list()
    for i in range(size):
        my_list.append(random.randint(begin, end))
    print(my_list)

    prime = []

    for num in my_list:
        c = 0
        for j in range(1, num):
            if num % j == 0:
                c += 1
        if c == 1:
            prime.append(num)

    data = {1: lambda lst: max(lst), 2: lambda lst: min(lst), 3: lambda lst: my_list.reverse()}
    if choice == 1:
        print(data[1](my_list))
    elif choice == 2:
        print(data[2](my_list))
    elif choice == 3:
        print(data[3](my_list), my_list)
    else:
        print(prime)

except Exception as err:
    print(f'Error: {err}')
