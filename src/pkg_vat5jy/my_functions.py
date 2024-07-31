'''
my_functions.py

This module contains various utility functions for processing text data.

Functions:
- clean_text(my_str)
- tokenize(my_str)
- count_words(my_str)
'''

import string
from collections import Counter

def clean_text(my_str):
    '''
    Input: my_str str
    Output: my_str but with all lowercase words and throw out any punctuation
    '''

    assert isinstance(my_str, str), f"expected str but got {type(my_str)}"

    trans = str.maketrans('','',string.punctuation)
    assert isinstance(trans, dict), f"expected dict but got {type(trans)}"

    txt = my_str.lower().translate(trans)
    assert isinstance(txt, str), f"expected str but got {type(my_str)}"
    assert not txt == "", "should not be empty"
    return txt

def tokenize(my_str):
    '''
    Input: my_str str
    Output: a python list where each item is a word in my_str
    '''
    assert isinstance(my_str, str), f"expected str but got {type(my_str)}"

    my_list = my_str.split()
    return my_list

def count_words(my_str):
    '''
    Input: my_str str
    Output: a python dictionary with the words in my_str as keys and their counts as values
    '''
    assert isinstance(my_str, str), f"expected str but got {type(my_str)}"

    counts = Counter(my_str.split())
    assert counts != "", "should not be empty"

    my_dict = dict(counts)
    assert isinstance(my_dict, dict), f"expected dict but got {type(my_dict)}"
    return my_dict
