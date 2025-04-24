def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def main():
    count = word_count("books/frankenstein.txt")
    print(f"{count} words found in the document")
    return

main()


