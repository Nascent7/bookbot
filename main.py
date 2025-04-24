from stats import get_book_text
from stats import char_count
from stats import sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path) # puts string into a usable variable

    words = text.split() # makes string into list of words
    num_words = len(words) # counts the number of words 

    count = char_count(text)
    sorted_dict = sort_dict(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")

    print("-------- Character Count --------")
    for char_dict in sorted_dict:
        if char_dict["char"].isalpha(): # only prints alphabetical characters
            print(f"{char_dict['char']}: {char_dict['num']}")

main()