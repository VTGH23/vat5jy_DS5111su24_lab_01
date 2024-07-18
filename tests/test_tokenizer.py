import pytest
import pylint
from my_functions import clean_text, tokenize, count_words

def test_tokenize():

	# Given a string _text_ of text from the Raven
	# When I pass _text_ to the 'tokenize()' function
	# Then I should get a python list, where each item is a word from _text_

	text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
	tokenized_list = tokenize(text)
	expected_return = ["But", "the", "Raven,", "sitting", "lonely", "on", "the",  "placid", "bust,", "spoke", "only", "That", "one", "word,", "as",
	"if", "his", "soul", "in", "that", "one", "word", "he",  "did", "outpour."]

	assert isinstance(tokenized_list,list), f"Tokenizer failed on sample text: {text}"
	assert expected_return == tokenized_list, f"Tokenizer failed on sample text: {text}"

@pytest.mark.xfail(reason="This test is intended to fail on purpose because it expects the return value to be a tuple")
def test_tokenize_fail():

        # Given a string _text_ of text from The Raven
        # When I pass _text_ to the 'tokenize()' function
        # Then I should get a python list, where each item is a a word from _text_

        text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
        tokenized_list = tokenize(text)
        expected_return_fail = ("But", "the", "Raven,", "sitting", "lonely", "on", "the",  "placid", "bust,", "spoke", "only", "That", "one", "word,", "as",
        "if", "his", "soul", "in", "that", "one", "word", "he",  "did", "outpour.")

        assert isinstance(tokenized_list,list), f"Tokenizer failed on sample text: {text}"
        assert expected_return_fail == tokenized_list, f"Tokenizer failed on sample text: {text}"

def test_tokenize_The_Raven():

	# Given a string _text_ of the full text of The Raven
	# When I pass _text_ to the 'tokenize()' function
	# Then I should get a python list, where each item is a word from _text_

	# Read in The Raven as a string
	file_path = '/home/ubuntu/vat5jy_DS5111su24_lab_01/pg17192.txt'
	with open(file_path, 'r') as file:
		file_content = file.read()

	tokenized_list = tokenize(file_content)

	assert isinstance(tokenized_list, list), f"Tokenizer failed on The Raven"
	# Test that the length of return list is as expected
	assert len(tokenized_list) == len(file_content.split()), f"Tokenizer failed The Raven. List length is not as expected."
	# Test that all tokens are strings as expected
	assert all(isinstance(token, str) for token in tokenized_list), f"Tokenized failed on The Raven. Not all tokens are str type."

# Use parametrize decorator to test tokenize() on a list of text files.
book_list = ["pg17192.txt","pg932.txt", "pg1063.txt","pg10031.txt"]

@pytest.mark.parametrize("book_name", book_list)
def test_tokenize_list_of_texts(book_name):

	# Given strings _text_ from a specified list of full texts written by Poe
	# When I pass _text_ to the 'tokenize()' function
	# Then I should get a python list, where each item is a word from _text_, for each of my specified texts

	file_path = f'/home/ubuntu/vat5jy_DS5111su24_lab_01/{book_name}'
	with open(file_path, 'r') as file:
		file_content = file.read()

	tokenized_list = tokenize(file_content)

	assert isinstance(tokenized_list, list), f"Tokenizer failed on {book_name}"
	# Test that the length of return list is as expected
	assert len(tokenized_list) == len(file_content.split()), f"Tokenizer failed on {book_name}. List length is not as expected."
	# Test that all tokens are strings as expected
	assert all(isinstance(token, str) for token in tokenized_list), f"Tokenized failed on {book_name}. Not all tokens are str type."

# Now perform a similar test but concatenate all of the English text files together as the test input for tokenizer().

def test_tokenizer_list_of_texts_combined():

	# Given string _text_ which is a concatenated string built from a specified list of full English texts written by Poe
	# When I pass _text_ to the 'tokenizer' function
	# Then I should get a python list, where each item is a word from _text_

	# Read and combine text
	text_concat = ""
	for c in book_list:

		file_path = f'/home/ubuntu/vat5jy_DS5111su24_lab_01/{c}'
		with open(file_path, 'r') as file:
			text_concat += file.read() + ' ' # Add a space here between text from different files

	tokenized_list = tokenize(text_concat)

	assert isinstance(tokenized_list, list), f"Tokenizer failed on combined texts."
	# Test that the length of return list is as expected
	assert len(tokenized_list) == len(text_concat.split()), f"Tokenizer failed on combined texts. List length is not as expected."
	# Test that all tokens are strings as expected
	assert all(isinstance(token, str) for token in tokenized_list), f"Tokenized failed on combined texts. Not all tokens are str type."

def test_tokenizer_Le_Corbeau():

        # Given string _text_ which is a string of text from Le Corbeau
        # When I pass _text_ to the 'tokenizer()' function
        # Then I should get a python list, where each item is a word from _text_

	text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne p>
	que je fis à peine davantage que marmotter «D'autres amis déjà ont
	pris leur vol--demain il me laissera comme mes Espérances déjà ont
	pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

	tokenized_list = tokenize(text)

	assert isinstance(tokenized_list, list), f"Tokenizer failed on Le Corbeau"
	# Test that the length of return list is as expected
	assert len(tokenized_list) == len(text.split()), f"Tokenizer failed Le Corbeau. List length is not as expected."
	# Test that all tokens are strings as expected
	assert all(isinstance(token, str) for token in tokenized_list), f"Tokenized failed on Le Corbeau. Not all tokens are str type."
