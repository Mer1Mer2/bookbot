def get_book_text(pwd):
    with open(pwd) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower = text.lower()
    counts = {}
    for letter in lower:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts

def sort_char_counts(char_counts):
    dict_list = []
    for key, value in char_counts.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_dict_list)
    return dict_list

def sort_dict_list(item_dict):
    return item_dict["num"]


