width = int(input('Enter the width of the rectangle: '))
length = int(input("Enter the length of the rectangle: "))

def print_rectangle (width, length):
    try:
        for i in range (width):
            if (i == 0) or (i == width - 1):
                print('*  ' * length)
            else:
                print('*  ' + '   ' * (length - 2) + '*')
        return ''
    except Exception as err:
        return f'Error: {err}'
print(print_rectangle(width, length))
