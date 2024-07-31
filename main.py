

def main():
    with open("books/frankenstein.txt") as f:
        print("--- Begin report of books/frankenstein.txt ---")
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)

        print(f"{word_count} words found in the document\n")
        sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

        for char, count in sorted_chars:
                print(f"The '{char}' character was found {count} times")

        print("--- End report ---")


def count_words(string):
    wordsCount = len(string.split())
    return wordsCount

def count_chars(string):
    char_dictionary = {}
    lowered_string = string.lower()

    for letter in lowered_string:
        if letter.isalpha() == True:
            if char_dictionary.get(letter):
                char_dictionary[letter] += 1
            else:
                char_dictionary[letter] = 1

    return char_dictionary

def sort_on(dict):
    return dict["num"]


main()