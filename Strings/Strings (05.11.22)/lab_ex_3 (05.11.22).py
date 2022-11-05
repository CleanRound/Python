try:
    string = input('Enter elements of a list separated by space ')
    print("\n")

    user_list = string.split()
    print('list:', user_list)

    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])


    def average(user_list):
        return sum(user_list) / len(user_list)


    average = average(user_list)

    print("Average of the list =", round(average, 2))
except Exception as err:
    print(f'Error: {err}')