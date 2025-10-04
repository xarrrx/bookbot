# count words of text and PRINT the result
def count_words(text):
    text_list = []
    text_list = text.split()
    word_count = len(text_list)

    print(f"Found {word_count} total words")
    return


# count characters and return as dictionary
def count_characters(text):
    dict = {}
    for char in text:
        c = char.lower()
        if c in dict:
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1
    
    return dict

def sort_on(items):
    return items["num"]


def dictionary_to_sorted_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)

    return list
    
