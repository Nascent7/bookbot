# uses file path to find book contents
# reads file and converts contents to string
# returns string value of file contents 
def get_book_text(file_path):
    with open(file_path) as f:
        contents =  f.read()
        return contents
    
def char_count(contents):
    book_text = contents.lower() # book contents are in lower case
    char_dict = {}

# dictionaries dont use .append(), but are accessed with []
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1 # increments the cout of an existing key by 1
        else:
            char_dict[char] = 1 # adds key since it is not in the dict. and sets vlaue to 1
    
    return char_dict
