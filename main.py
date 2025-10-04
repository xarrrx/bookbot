#from stats import count_words
#from stats import count_characters
#from stats import dictionary_to_sorted_list
from stats import *
import sys


if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    contents = ""
    with open(file_path) as f:
        contents = f.read()
    
    return contents

#path = "books/frankenstein.txt"
path = sys.argv[1]


def main():
    #print(get_book_text("./books/frankenstein.txt"))
   # count_words(get_book_text(path))
    
    chars = count_characters(get_book_text(path))
    #print(chars)
    sorted_chars = dictionary_to_sorted_list(chars)


   # print("TESTTESTTEST")
  #  print(chars)
  #  print("TESTTESTTESTTEST")
   # print(sorted_chars)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}... ")
    print("----------- Word Count ----------")
    print(count_words(get_book_text(path)))
    print("--------- Character Count -------")
    for ele in sorted_chars:
        if ele["char"].isalpha():
            print(f"{ele["char"]}: {ele["num"]}")
    print("============= END ===============")



if __name__ == "__main__":
    main()