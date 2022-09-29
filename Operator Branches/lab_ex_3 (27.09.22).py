console_value = int(input('Enter the console value: '))
amount_of_consoles = int(input('Enter the amount of consoles: '))
discount_value = int(input('Enter the discount percentage value: '))
choice = int(input('Enter 1 for the total sum of the order.\nEnter 2 for the price of the one console with the'
                   'discount:\n'))

if choice == 1:
    print (f' The total sum of the order is {console_value * amount_of_consoles}')
elif choice == 2:
    print(f' The price of the one console with the discount is {console_value // 100 * discount_value}')
else:
    print(f' Error, something is wrong with your choice')




