import pytest
import pylint
from collections import Counter
from my_functions import clean_text, tokenize, count_words

def test_count_words_example():
	# Example test

	# Given a string _text_ of text with words
	# When I pass _text_ to the 'count_words()' function
	# I should get a dictionary as return representing the words in the string as keys and their counts as value
	text = 'philosophical prose poem of "Eureka," which he deemed the crowning work'
	assert isinstance(count_words(text), dict), f"count_words() failed on sample text: {text}"

def test_count_words():

	# Given a string _text_ of text from The Raven
	# When I pass _text_ to the 'count_words()' function
	# I should get a dictionary as return representing the words in the string as keys and their counts as value

	text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
	counts = count_words(text)
	expected_counts = {"But": 1, "the": 2, "Raven,": 1, "sitting": 1, "lonely": 1, "on": 1, "placid": 1, "bust,": 1, "spoke": 1, "only": 1, 
	"That": 1, "one": 2, "word,": 1, "as": 1, "if": 1, "his": 1, "soul": 1, "in": 1, "that": 1, "word": 1, "he": 1, "did": 1, "outpour.": 1}

	assert isinstance(counts, dict), f"count_words() failed on sample text: {text}"
	assert counts == expected_counts, f"count_words() failed on sample text: {text}"

@pytest.mark.xfail(reason="This test is intended to fail on purpose because it will expect a return with incorrect counts")
def test_count_words_fail():

	# Given a string _text_ of text from The Raven
	# When I pass _text_ to the 'count_words()' function
	# I should get a dictionary as a return representing the words in the string as keys and their counts as values

	text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
	counts = count_words(text)
	expected_counts_fail = {"But": 1, "the": 1, "Raven,": 1, "sitting": 1, "lonely": 1, "on": 1, "placid": 1, "bust,": 1, "spoke": 1, "only": 1, 
	"That": 1, "one": 1, "word,": 1, "as": 1, "if": 1, "his": 1, "soul": 1, "in": 1, "that": 1, "word": 1, "he": 1, "did": 1, "outpour.": 1}

	assert isinstance(counts, dict), f"count_words() failed on sample text: {text}"
	assert counts == expected_counts_fail, f"count_words() failed on sample text: {text}"

def test_count_words_The_Raven():

	# Given a string _text_ of the full text of The Raven
	# When I pass _text_ to the 'count_words()' function
	# Then I should get a dictionary as a return representing the words in the string as keys and their counts as values

	# Read in The Raven as a string
	file_path = '/home/ubuntu/vat5jy_DS5111su24_lab_01/pg17192.txt'
	with open(file_path, 'r') as file:
		file_content = file.read()
	counts = count_words(file_content)

	assert isinstance(counts, dict), f"count_words() failed on The Raven."

def test_count_words_The_Raven_keys():

	# Given a string _text_ of the full text of The Raven
	# When I pass _text_ to the 'count_words()' function and the 'tokenize()' function
	# Then the keys of my return dictionary from count_words() should be the same as the unique strings returned from tokenize().

	# Read in The Raven as a string
	file_path = '/home/ubuntu/vat5jy_DS5111su24_lab_01/pg17192.txt'
	with open(file_path, 'r') as file:
		file_content = file.read()
	counts = count_words(file_content)

	# Test return dictionary has keys which represent the unique words in the string
	assert set(list(counts.keys())) == set(tokenize(file_content)), f"count_words() failed on The Raven. Keys do not represent the unique words in the string"

def test_count_words_The_Raven_dict():

	# Given a string _text_ of the full text of The Raven
	# When I pass _text_ to the 'count_words()' function and the 'tokenize()' function
	# Then the counts for the keys in the return dict from count_words() should equal the counts of strings returned from tokenize().

	# Read in The Raven as a string
	file_path = '/home/ubuntu/vat5jy_DS5111su24_lab_01/pg17192.txt'
	with open(file_path, 'r') as file:
		file_content = file.read()

	counts = count_words(file_content)

	# Tokenize The Raven
	tokenized_list = tokenize(file_content)

	# Build dictionary of counts from tokenized list
	tokenized_dict = Counter(tokenized_list)

	# Test return dictionary has values which represent the counts of the unique words in the string
	assert counts  == tokenized_dict, f"count_words() failed on The Raven. Key values do not represent the counts of the words in the string"

# Use parametrize decorator to test count_words() on a list of text files.
book_list = ["pg17192.txt","pg932.txt", "pg1063.txt","pg10031.txt"]

@pytest.mark.parametrize("book_name", book_list)
def test_count_words_list_of_texts(book_name):

	# Given strings _text_ from a specified list of full texts written by Poe
	# When I pass _text_ to the 'count_words()' function and the 'tokenize()' function
	# Then the counts for the keys in the return dict from count_words() should equal the counts of strings returned from tokenize(), for each text

	file_path = f'/home/ubuntu/vat5jy_DS5111su24_lab_01/{book_name}'
	with open(file_path, 'r') as file:
		file_content = file.read()

	counts = count_words(file_content)

	# Tokenize the text
	tokenized_list = tokenize(file_content)

	# Build dictionary of counts from tokenized list
	tokenized_dict = Counter(tokenized_list)

	# Test return dictionary has values which represent the counts of the unique words in the string
	assert counts  == tokenized_dict, f"count_words() failed on {book_name}. Key values do not represent the counts of the words in the string"

# Now perform a similar test but concatenate all of the English text files together as the test input for count_words().

def test_count_words_list_of_texts_combined():

        # Given string _text_ which is a concatenated string built from a specified list of full English texts written by Poe
        # When I pass _text_ to the 'count_words()' function
	# Then the counts for the keys in the return dict from count_words() should equal the counts of strings returned from tokenize(), for all texts combined

	# Read and combine text
	text_concat = ""
	for c in book_list:

		file_path = f'/home/ubuntu/vat5jy_DS5111su24_lab_01/{c}'
		with open(file_path, 'r') as file:
			text_concat += file.read() + ' ' # Add a space here between text from different files

	counts = count_words(text_concat)

	# Tokenize the text
	tokenized_list = tokenize(text_concat)

	# Build dictionary of counts from tokenized list
	tokenized_dict = Counter(tokenized_list)

	# Test return dictionary has values which represent the counts of the unique words in the string
	assert counts  == tokenized_dict, f"count_words() failed on combined texts. Key values do not represent the counts of the words in the string"

def test_count_words_Le_Corbeau():

        # Given string _text_ which is a string of text from Le Corbeau
        # When I pass _text_ to the 'count_words()' function
	# Then the counts for the keys in the return dict from count_words() should equal the counts of strings returned from tokenize().

	text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne p>
	que je fis à peine davantage que marmotter «D'autres amis déjà ont
	pris leur vol--demain il me laissera comme mes Espérances déjà ont
	pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

	counts = count_words(text)

	# Tokenize Le Corbeau
	tokenized_list = tokenize(text)

	# Build dictionary of counts from tokenized list
	tokenized_dict = Counter(tokenized_list)

	# Test return dictionary has values which represent the counts of the unique words in the string
	assert counts  == tokenized_dict, f"count_words() failed on Le Corbeau. Key values do not represent the counts of the words in the string"
