
# -*- coding: utf-8 -*-
"""
Code : find out  most common word programme
@author: Tajender Singh Katal
"""
from collections import Counter

def count_words_from_text(text):
    word_counter = Counter()
    
    # Split the text into words
    words = text.split()  # Split by whitespace
    word_counter.update(words)
    
    # Get the most common word
    if word_counter:
        most_common = word_counter.most_common(1)
        most_common_word, count = most_common[0]
        return most_common_word, count
    else:
        return None

def main():
    # Sample text
    text = """This is a dummy text. 
    This text is just a used for dummy testing.
    This program will use counter library"""
    
    result = count_words_from_text(text)
    
    if result:
        word, count = result
        print(f"The most common word is '{word}' with a count of {count}.")
    else:
        print("No words found or there was an error processing the text.")

if __name__ == "__main__":
    main()
    
#OUTPUT : The most common word is 'This' with a count of 3.
    
    