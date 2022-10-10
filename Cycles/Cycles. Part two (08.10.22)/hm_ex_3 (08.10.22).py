try:
    while True:
        while True:
            num = int(input("Enter the number: "))
            if num == 7:
                print("Good Bye!")
            elif num > 0:
                print("Number is positive")
            elif num < 0:
                print("Number is negative")
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            print("The program has finished")
            break
except Exception as err:
    print(f'Error: {err}')
finally:
    print("The program has finished.")