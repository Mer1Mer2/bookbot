import sys

from stats import count_words, count_characters, sort_char_counts, get_book_text

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts_dict = count_characters(text)
    sorted_char_data = sort_char_counts(char_counts_dict) 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...") 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_entry in sorted_char_data:
        current_char = char_entry["char"]
        current_num = char_entry["num"]
        if current_char.isalpha(): 
            print(f"{current_char}: {current_num}") 
    print("============= END ===============")

if __name__ == "__main__":
    main()