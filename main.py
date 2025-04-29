from stats import get_num_words
from stats import get_char_count
from stats import sort_list

def main():
    count = get_num_words("books/frankenstein.txt")
    char_count_dict = get_char_count("books/frankenstein.txt")
    sorted_chars =  sort_list(char_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    print("============= END ===============")
    return

main()


