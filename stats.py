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

def sort_dict(char_dict): # sorting function
    chars_list = [] # list to hold dictionaries of (char : num) pairs

    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})
    
    def sort_on(dict): # helper function for sorting 
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on) # sorts list from greatest to least

    return chars_list # returns originally created list 