def get_book_text(file_path):
    
    file_contents = open_book(file_path)    
    # print(file_contents)
    return get_book_word_count(file_contents)
    
def open_book(file_path):
    with open(file_path) as f:
        file_contents = f.read()    
        return file_contents

def get_word_array(text):
    word_array = text.split()
    return word_array


def get_book_word_count(text):
    word_array = get_word_array(text)
    num_words = len(word_array)
    return (f"Found {num_words} total words")

def get_char_counts(file_path):
    
    with open(file_path) as f:
        file_contents = f.read()
        return count_chars(file_contents)

def count_chars(text):
    chars_counts = {}
    char_count_list = []
    for word in text:
        for char in word:
            char = char.lower()
            if char in chars_counts:
                chars_counts[char] += 1
            else:
                chars_counts[char] = 1
    for char, count in chars_counts.items():
        if not(char.isalpha()):
            continue
        char_count_list.append({"char": char, "num": count})
    return(char_count_list)
    

def format_report(file_path):
    book_contents = open_book(file_path)
    word_array = get_word_array(book_contents)
    char_counts = count_chars(word_array)
    #print("Character Count Report", book_contents)
    #print("-----------------------")
    # print(word_array)
    char_counts.sort(reverse=True, key=sort_on)
    #print(char_counts)
    for item in char_counts:
        print(f"{item['char']}: {item['num']}")
    
    

def sort_on(items):
    return items["num"]
        
        
    