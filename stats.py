def get_num_words(file_path):
    file_contents = ""
    with open(file_path) as f:
        text = f.read()
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def get_char_count(file_path):
    file_contents = ""
    char_count_dict = {}
    with open(file_path) as f:
        text = f.read()
    for char in text:
        char_lowercase = char.lower()
        char_count_dict[char_lowercase] = char_count_dict.get(char_lowercase, 0) +1
    return char_count_dict

