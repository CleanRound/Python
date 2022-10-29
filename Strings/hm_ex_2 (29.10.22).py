try:
    text = input('Enter the text: ')
    words = input('Enter the words that have to be changed to uppercase register: ')
    split = words.split()

    for word in split:
        if text.count(word) > 0:
            x = word
            c = word.upper()

            text = text.replace(x, c)
    print(text)
except Exception as err:
    print(f'Error: {err}')
