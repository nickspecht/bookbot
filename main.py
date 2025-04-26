from stats import get_num_words
from stats import get_char_count

def main():
    count = get_num_words("books/frankenstein.txt")
    char_count_dict = get_char_count("books/frankenstein.txt")
    print(f"{count} words found in the document")
    print(char_count_dict)
    return

main()


