import string
from collections import Counter

def clean_text(my_str):
	assert isinstance(my_str, str), f"expected str but got {type(my_str)}"

	trans = str.maketrans('','',string.punctuation)
	assert isinstance(trans, dict), f"expected dict but got {type(trans)}"

	txt = my_str.lower().translate(trans)
	assert isinstance(txt, str), f"expected str but got {type(my_str)}"
	assert not txt == "", "should not be empty"
	return txt

def tokenize(my_str):
	assert isinstance(my_str, str), f"expected str but got {type(my_str)}"

	my_list = my_str.split()
	return my_list

def count_words(my_str):
	assert isinstance(my_str, str), f"expected str but got {type(my_str)}"

	counts = Counter(my_str.split())
	assert not counts == "", "should not be empty"

	my_dict = dict(counts)
	assert isinstance(my_dict, dict), f"expected dict but got {type(my_dict)}"
	return my_dict
