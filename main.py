from stats import get_book_text
from stats import char_count

def main():
    text = get_book_text("books/frankenstein.txt") # puts string into a usable variable
    words = text.split() # makes string into list of words
    num_words = len(words) # counts the number of words 

    count = char_count(text)

    print(f"{num_words} words found in the document.")
    print(count)

main()