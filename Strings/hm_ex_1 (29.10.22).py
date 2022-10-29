try:
    def isPalindrome(string):
        return string == string[::-1]

    string = input('Enter the string: ')
    palin = isPalindrome(string)

    if palin:
        print('This string is a palindrome')
    else:
        print('This string is not a palindrome')
except Exception as err:
    print(f'Error: {err}')