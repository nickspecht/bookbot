import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_list

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    count = get_num_words(path_to_book)
    char_count_dict = get_char_count(path_to_book)
    sorted_chars =  sort_list(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
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


