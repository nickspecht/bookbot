def get_num_words(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count