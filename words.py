words = ['hello', 'hey', 'goodbye', 'yo', 'yes']

def print_upper_words(words, must_start_with=[]):
    """Takes in a list of words, then prints out each word seperatly and upper cased.
    You can enter an optional second param in the form of a list to only print words that start with the characters entered"""
    if must_start_with != []:
        for char in must_start_with:
            for word in words:
                word = word.upper()
                if char.upper() == word[0]:
                    print(word)
    else:
        for word in words:
            print(word.upper())
            


print_upper_words(words, ['h', 'y'])