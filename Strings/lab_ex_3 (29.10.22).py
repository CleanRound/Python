try:
    def count_Occurrence(ch, str1):
        count = 0
        for i in range(len(string)):
            if(string[i] == char):
                count = count + 1
        return count

    string = input("Enter the string: ")
    char = input("Enter the character: ")

    cnt = count_Occurrence(char, string)
    print(f'The total number of times {char} has occured = {cnt}')
except Exception as err:
    print(f'Error: {err}')
