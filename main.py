def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = word_count(file_contents)
        letter_counts = letter_count(file_contents)
        sorted_letters = prepare_sorted_list(letter_counts)
        generate_report(sorted_letters, total_words)

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    my_dict = {}
    for character in text.lower():
        if character.isalpha():
            if character not in my_dict:
                my_dict[character] = 1
            else:   
                my_dict[character] += 1
    return my_dict

def prepare_sorted_list(my_dict):
    char_list = []
    for char, count in my_dict.items():  
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)  
    return char_list

def sort_on(dict):
    return dict["num"]

def generate_report(char_list, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

main()