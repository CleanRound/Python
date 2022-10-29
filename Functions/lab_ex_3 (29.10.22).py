number = int(input('Enter the number: '))

def prime(number):
    try:
        if number > 1:
            for i in range(2,number):
                if (number % i) == 0:
                    return f'{number} is not a prime number'
                else:
                    return f'{number} is a prime number'
    except Exception as err:
        return f'Error: {err}'
print(prime(number))
