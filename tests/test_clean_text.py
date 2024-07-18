import pytest
import pylint
import string
import platform
import sys
import os
from my_functions import clean_text, tokenize, count_words

def test_clean_text():

	# Given a string _text_ of text from The Raven
	# When I pass _text_ to the 'clean_text()' function
	# Then I should get a string as a return with all lowercase words and no punctuation

	text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
	cleaned_text = clean_text(text)
	expected_clean_text = "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"

	assert isinstance(cleaned_text, str), f"clean_text() failed on sample text: {text}"
	assert cleaned_text == expected_clean_text, f"clean_text() failed on sample text: {text}"

@pytest.mark.xfail(reason="This test is intended to fail on purpose because it does not return words in lowercase")
def test_clean_text_fail():

	# Given a string _text_ of text from The Raven
	# When I pass _text_ to the 'clean_text()' function
	# Then I should get a string as a return with all lowercase words and no punctuation

	text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
	cleaned_text = clean_text(text)
	expected_clean_text_fail = "But the Raven sitting lonely on the placid bust spoke only That one word as if his soul in that one word he did outpour."

	assert isinstance(cleaned_text, str), f"clean_text() failed on sample text: {text}"
	assert cleaned_text == expected_clean_text_fail, f"clean_text() failed on sample text: {text}"

def test_clean_text_The_Raven():

	# Given a string _text_ of the full text of The Raven
	# When I pass _text_ to the 'clean_text()' function
	# Then I should get a string as a return with all lowercase words and no punctuation

	# Read in The Raven as a string
	# file_path = '/home/ubuntu/vat5jy_DS5111su24_lab_01/pg17192.txt' --- old logic
	# file_path = os.path.join(os.path.dirname(__file__),'..', 'pg17192.txt') -- old logic
	root_dir = os.path.dirname(os.path.dirname(__file__)) # Get parent directory
	file_path = os.path.join(root_dir, 'pg17192.txt')
	with open(file_path, 'r') as file:
		file_content = file.read()

	cleaned_text = clean_text(file_content)
	assert isinstance(cleaned_text, str), f"clean_text() failed on The Raven."
	# Test for punctuation removal
	assert any(character in cleaned_text for character in string.punctuation) == False, f"clean_text() failed on removing punctuation on The Raven."
	# Test for all lowercase words
	assert any(character for character in cleaned_text if character.isupper()) == False, f"clean_text() failed on converting string to all lowercase words on The Raven."

# Use parametrize decorator to test clean_text() on a list of text files.
book_list = ["pg17192.txt","pg932.txt", "pg1063.txt","pg10031.txt"]

@pytest.mark.parametrize("book_name", book_list)
def test_clean_text_list_of_texts(book_name):

	# Given strings _text_ from a specified list of full texts written by Poe
	# When I pass _text_ to the 'clean_text()' function
	# Then I should get a string as a return with all lowercase words and no punctuation, for each of my specified texts
	# file_path = f'/home/ubuntu/vat5jy_DS5111su24_lab_01/{book_name}'
	# file_path = os.path.join(os.path.dirname(__file__),'..',f'{book_name}') -- old logic
	root_dir = os.path.dirname(os.path.dirname(__file__))
	file_path = os.path.join(root_dir, f'{book_name}')
	with open(file_path, 'r') as file:
		file_content = file.read()

	cleaned_text = clean_text(file_content)
	assert isinstance(cleaned_text, str), f"clean_text() failed on {book_name}."
	# Test for punctuation removal
	assert any(character in cleaned_text for character in string.punctuation) == False, f"clean_text() failed on removing punctuation on {book_name}."
	# Test for all lowercase words
	assert any(character for character in cleaned_text if character.isupper()) == False, f"clean_text() failed on converting string to all lowercase on {book_name}"

# Now perform a similar test but concatenate all of the English text files together as the test input for clean_text()

def test_clean_text_list_of_texts_combined():

	# Given string _text_ which is a concatenated string built from a specified list of full English texts written by Poe
	# When I pass _text_ to the 'clean_text()' function
	# Then I should get a string as a return with all lowercase words and no punctuation

	# Read and combine text
	text_concat = ""
	for c in book_list:

		# file_path = f'/home/ubuntu/vat5jy_DS5111su24_lab_01/{c}' --- old logic
		# file_path = os.path.join(os.path.dirname(__file__),'..',f'{c}') --- old logic
		root_dir = os.path.dirname(os.path.dirname(__file__))
		file_path = os.path.join(root_dir, 'pg17192.txt')
		with open(file_path, 'r') as file:
			text_concat += file.read() + ' ' # Add a space here between text from different files

	cleaned_text = clean_text(text_concat)
	assert isinstance(cleaned_text, str), f"clean_text() failed on combined texts."
	# Test for punctuation removal
	assert any(character in cleaned_text for character in string.punctuation) == False, f"clean_text() failed on removing punctuation on combined texts."
	# Test for all lowercase words
	assert any(character for character in cleaned_text if character.isupper()) == False, f"clean_text() failed on converting string to all lowercase on combined texts."

def test_clean_text_Le_Corbeau():

	# Given string _text_ which is a string of text from Le Corbeau
	# When I pass _text_ to the 'clean_text()' function
	# Then I should get a string as a return with all lowercase words and no punctuation

	text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
	que je fis à peine davantage que marmotter «D'autres amis déjà ont
	pris leur vol--demain il me laissera comme mes Espérances déjà ont
	pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

	cleaned_text = clean_text(text)
	assert isinstance(cleaned_text, str), f"clean_text() failed on Le Corbeau."
	# Test for punctuation removal
	assert any(character in cleaned_text for character in string.punctuation) == False, f"clean_text() failed on removing punctuation on Le Corbeau."
	# Test for all lowercase words
	assert any(character for character in cleaned_text if character.isupper()) == False, f"clean_text() failed on converting string to all lowercase on Le Corbeau."

# Extra Credit tests

@pytest.mark.skip(reason="clean_text does not support Japanese Kanji yet.")
def test_clean_text_Japanese():

	# Given a string _text_ which is a string of Japanese Kanji characters
	# When I pass _text_ to 'clean_text()'
	# Then I should get a string as a return with no punctuation (Kanji does not use lowercase/uppercase)

	Japanese_Example_Text = "This is a placeholder."
	expected_text = "this is a placeholder"
	cleaned_text = clean_text(Japanese_Example_Text)

	assert cleaned_text == expected_text, f"clean_text() failed on removing punctuation on Japanese example"

def test_clean_text_OS():

	# Given a string _text_ and current OS
	# When I pass _text_ to 'clean_text()'
	# Then I should get a string as a return with no punctuation and all lowercase. Fail if not on expected OS.

	my_OS = platform.system()
	print(my_OS)
	assert my_OS == 'Linux', f"Test failed because OS is not as expected"

	Example_Text = "This is a placeholder."
	expected_text = "this is a placeholder"
	cleaned_text = clean_text(Example_Text)

	assert cleaned_text == expected_text, f"clean_text() failed on example"

def test_clean_text_python_version():

	# Given a string _text_ and current python version
	# When I pass _text_ to 'clean_text()'
	# Then I should get a string as a return with no punctuation and all lowercase. Fail if not on expected python version.

	my_python = sys.version_info[:2]
	print(my_python)
	assert my_python == (3,12), f"Test failed because current python version is not expected version"

	Example_Text = "This is a placeholder."
	expected_text = "this is a placeholder"
	cleaned_text = clean_text(Example_Text)

	assert cleaned_text == expected_text, f"clean_text() failed on example"
