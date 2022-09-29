seconds_value = int(input('Enter the seconds time value: '))
choice = int(input('Enter 1 for the hours value.\nEnter 2 for the minutes value.\nEnter 3 for the seconds value:\n'))

if choice == 1:
    res_1 = (seconds_value // 3600)
    print(f'The {24 - res_1} hours value left until midnight')
elif choice == 2:
    res_2 = (seconds_value // 60)
    print (f' The {1440 - res_2} minutes value left until midnight')
elif choice == 3:
    print(f' The {86400 - seconds_value} seconds value left until midnight')
else:
    print(f' Error, something is wrong with your choice')
