try:
    text = input('Enter the text: ')

    sentences = text.count('. ')

    print(f'The amount of sentences is {sentences}')
except Exception as err:
    print(f'Error: {err}')
