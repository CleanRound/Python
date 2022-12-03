import string

try:
    print("File to perform capitalization on:")
    fileToSearch = input("> ")


    with open(fileToSearch) as file:
        lines = []
        for line in file:
            words = line.split(' ')
            for i, word in enumerate(words):
                if len(word.strip(string.punctuation + string.whitespace)) > 3:
                    words[i] = word.capitalize()
            lines.append(' '.join(words))
        capitalised = ''.join(lines)

    with open(fileToSearch, 'w') as file:
        file.write(capitalised)
    print('Capitalization was successful')
except Exception as err:
    print(f'Error: {err}')