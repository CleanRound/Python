try:
    width = int(input("Enter the width of rectangle: "))
    length = int(input("Enter the length of rectangle: "))

    for i in range(width):
        if (i == 0) or (i == width - 1):
            print('*  ' * length)
        else:
            print('*  ' + '   ' * (length - 2) + '*')
except Exception as err:
    print(f'Error: {err}')
finally:
    print('The program has finished')