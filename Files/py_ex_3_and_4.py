import collections
import pprint

try:
    print("Enter the filename:")
    fileToSearch = input("> ")

    with open(fileToSearch, 'r') as info:
        count = collections.Counter(info.read().upper())
        value = pprint.pformat(count)
    print(value)

    with open(fileToSearch, 'a') as file:
        file.write('\n\n' + value)
except Exception as err:
    print(f'Error: {err}')