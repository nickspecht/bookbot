from stats import get_num_words

def main():
    count = get_num_words("books/frankenstein.txt")
    print(f"{count} words found in the document")
    return

main()


