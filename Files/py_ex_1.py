import fileinput

try:
    print("Text to search for:")
    textToSearch = input("> ")

    print("Text to replace it with:")
    textToReplace = input("> ")

    print("File to perform Search-Replace on:")
    fileToSearch = input("> ")

    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')
    print('The replacement was successful')
except Exception as err:
    print(f'Error: {err}')
