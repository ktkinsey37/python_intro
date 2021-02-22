def print_upper_words(words, must_start_with):
    """Accepts a list of words and a set of letters.
    Iterates through the list and if the word
    starts with a letter in the set, prints the word in upper case.
    """
    for word in words:
        if word[0] in must_start_with:
            print(f"{word.upper()}")

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})