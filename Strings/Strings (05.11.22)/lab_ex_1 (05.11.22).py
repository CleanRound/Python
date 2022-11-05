import re
try:
    string = input("Enter the text: \n")
    lines = string.split('. ')

    for index, line in enumerate(lines):
        lines[index] = line[0].upper() + line[1:]
    print(". ".join(lines))

    total_digits = len(re.findall('[0-9]', string))
    print("Total digits found -", total_digits)

    count = 0
    for i in range(0, len(string)):
        if string[i] in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            count = count + 1

    print(f"Total number of punctuation characters exists in string: {count}")
except Exception as err:
    print(f'Error: {err}')