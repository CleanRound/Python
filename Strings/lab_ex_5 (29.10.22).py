try:
    string = input('Enter the string: ')
    word = input('Enter the word for search: ')
    replace_word = input('Enter the word for replacement: ')

    new_str = string.replace(word, replace_word)
    print(new_str)
except Exception as err:
    print(f'Error: {err}')