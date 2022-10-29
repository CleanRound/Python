try:
    def word_occurence(string, word):
        x = string.split(" ")
        c = 0
        for i in range(0, len(x)):
            if (word == x[i]):
                c = c + 1
        return c


    string = input("Enter the string: ")
    word = input("Enter the word: ")

    wrd_occ = word_occurence(string, word)
    print(f'The total number of times the word {word} has occured = {wrd_occ}')
except Exception as err:
    print(f'Error: {err}')
