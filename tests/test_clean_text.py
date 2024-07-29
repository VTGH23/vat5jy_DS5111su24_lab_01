# pylint: disable=C0413

"""
This module contains tests for the 'clean_text' function from the 'pkg_vat5jy' package.
"""

import os
import platform
import sys
import string
import pytest

sys.path.append('./src')
import pkg_vat5jy as pkg # pylint: disable=E0401

def test_clean_text():
    '''
    Given a string _text_ of text from The Raven
    When I pass _text_ to the 'clean_text()' function
    Then I should get a string as a return with all lowercase words and no punctuation
    '''
    text = """But the Raven, sitting lonely on the placid bust, spoke only That
 one word, as if his soul in that one word he did outpour."""
    cleaned_text = pkg.clean_text(text)
    expected_clean_text = """but the raven sitting lonely on the placid bust spoke only that
 one word as if his soul in that one word he did outpour"""

    assert isinstance(cleaned_text, str), f"clean_text() failed on sample text: {text}"
    assert cleaned_text == expected_clean_text, f"clean_text() failed on sample text: {text}"

@pytest.mark.xfail(reason="""This test is intended to fail on purpose because it does not return
 words in lowercase""")
def test_clean_text_fail():
    '''
    # Given a string _text_ of text from The Raven
    # When I pass _text_ to the 'clean_text()' function
    # Then I should get a string as a return with all lowercase words and no punctuation
    '''

    text = """But the Raven, sitting lonely on the placid bust, spoke only That one word,
 as if his soul in that one word he did outpour."""
    cleaned_text = pkg.clean_text(text)
    expected_clean_text_fail = """But the Raven sitting lonely on the placid bust spoke
 only That one word as if his soul in that one word he did outpour."""

    assert isinstance(cleaned_text, str), f"clean_text() failed on sample text: {text}"
    assert cleaned_text == expected_clean_text_fail, f"""clean_text() failed on sample
 text: {text}"""

def test_clean_text_the_raven():
    '''
    # Given a string _text_ of the full text of The Raven
    # When I pass _text_ to the 'clean_text()' function
    # Then I should get a string as a return with all lowercase words and no punctuation
    '''
    # Read in The Raven as a string

    root_dir = os.path.dirname(os.path.dirname(__file__)) # Get parent directory
    file_path = os.path.join(root_dir, 'pg17192.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    cleaned_text = pkg.clean_text(file_content)
    assert isinstance(cleaned_text, str), "clean_text() failed on The Raven."
    # Test for punctuation removal
    assert any(character in cleaned_text for character in string.punctuation) is False,"""
clean_text()
failed on removing punctuation on The Raven."""
    # Test for all lowercase words
    assert any(character for character in cleaned_text if character.isupper()) is False,"""
clean_text()
failed on converting string to all lowercase words on The Raven."""

# Use parametrize decorator to test clean_text() on a list of text files.
book_list = ["pg17192.txt","pg932.txt", "pg1063.txt","pg10031.txt"]

@pytest.mark.parametrize("book_name", book_list)
def test_clean_text_list_of_texts(book_name):
    '''
    # Given strings _text_ from a specified list of full texts written by Poe
    # When I pass _text_ to the 'clean_text()' function
    # Then I should get a string as a return with all lowercase words and no punctuation,
    for each of my specified texts
    '''

    root_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(root_dir, f'{book_name}')
    with open(file_path, 'r',encoding='utf-8') as file:
        file_content = file.read()

    cleaned_text = pkg.clean_text(file_content)
    assert isinstance(cleaned_text, str), f"clean_text() failed on {book_name}."
    # Test for punctuation removal
    assert any(character in cleaned_text for character in string.punctuation) is False, f"""
clean_text() failed on removing punctuation on {book_name}."""
    # Test for all lowercase words
    assert any(character for character in cleaned_text if character.isupper()) is False, f"""
clean_text() failed on converting string to all lowercase on {book_name}"""

# Now perform a similar test but concatenate all of the English text files together as the
# test input for clean_text()

def test_clean_text_list_of_texts_combined():
    '''
    # Given string _text_ which is a concatenated string built from a specified list of
    full English texts written by Poe
    # When I pass _text_ to the 'clean_text()' function
    # Then I should get a string as a return with all lowercase words and no punctuation
    '''
    # Read and combine text
    text_concat = ""
    for c in book_list:
        root_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(root_dir, c)
        with open(file_path, 'r',encoding='utf-8') as file:
            text_concat += file.read() + ' '

    cleaned_text = pkg.clean_text(text_concat)
    assert isinstance(cleaned_text, str), "clean_text() failed on combined texts."
    # Test for punctuation removal
    assert any(character in cleaned_text for character in string.punctuation) is False, """
clean_text() failed on removing punctuation on combined texts."""
    # Test for all lowercase words
    assert any(character for character in cleaned_text if character.isupper()) is False, """
clean_text() failed on converting string to all lowercase on combined texts."""

def test_clean_text_le_corbeau():
    '''
    # Given string _text_ which is a string of text from Le Corbeau
    # When I pass _text_ to the 'clean_text()' function
    # Then I should get a string as a return with all lowercase words and no punctuation
    '''
    text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot
 comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il
 n'agita donc pas de plume--jusqu'à ceque je fis à peine davantage que marmotter «D'autres amis
 déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont
 pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

    cleaned_text = pkg.clean_text(text)
    assert isinstance(cleaned_text, str), "clean_text() failed on Le Corbeau."
    # Test for punctuation removal
    assert any(character in cleaned_text for character in string.punctuation) is False, """
clean_text() failed on removing punctuation on Le Corbeau."""
    # Test for all lowercase words
    assert any(character for character in cleaned_text if character.isupper()) is False, """
clean_text() failed on converting string to all lowercase on Le Corbeau."""

# Extra Credit tests

@pytest.mark.skip(reason="clean_text does not support Japanese Kanji yet.")
def test_clean_text_japanese():
    '''
    # Given a string _text_ which is a string of Japanese Kanji characters
    # When I pass _text_ to 'clean_text()'
    # Then I should get a string as a return with no punctuation
    # (Kanji does not use lowercase/uppercase)
    '''
    japanese_example_text = "This is a placeholder."
    expected_text = "this is a placeholder"
    cleaned_text = pkg.clean_text(japanese_example_text)

    assert cleaned_text == expected_text, """clean_text() failed on removing punctuation on
    Japanese example"""

def test_clean_text_os():
    '''
    # Given a string _text_ and current OS
    # When I pass _text_ to 'clean_text()'
    # Then I should get a string as a return with no punctuation and all lowercase.
    # Fail if not on expected OS.
    '''
    my_os = platform.system()
    print(my_os)
    assert my_os == 'Linux', "Test failed because OS is not as expected"

    example_text = "This is a placeholder."
    expected_text = "this is a placeholder"
    cleaned_text = pkg.clean_text(example_text)

    assert cleaned_text == expected_text, "clean_text() failed on example"

def test_clean_text_python_version():
    '''
    # Given a string _text_ and current python version
    # When I pass _text_ to 'clean_text()'
    # Then I should get a string as a return with no punctuation and all lowercase.
    Fail if not on expected python version.
    '''
    my_python = sys.version_info[:2]
    print(my_python)
    assert my_python in ((3,7),(3,12)), """Test failed because current python version is not
 expected version"""

    example_text = "This is a placeholder."
    expected_text = "this is a placeholder"
    cleaned_text = pkg.clean_text(example_text)

    assert cleaned_text == expected_text, "clean_text() failed on example"

@pytest.mark.integration
def test_clean_text_integration_01():
    '''
    # Given a string _text_
    # When I pass _text_ to 'clean_text()' and then to 'tokenize()'
    # Then I should get a python list, where each item is a word from _text_.
    Every word should be lowercase and there should be no punctuation.
    '''
    my_string = "Hello! We are testing some of our functions today!"
    expected_list = ["hello", "we", "are", "testing", "some", "of", "our",
"functions", "today"]

    cleaned_text = pkg.clean_text(my_string)
    assert isinstance(cleaned_text, str), "clean_text() failed on my_string"
    my_list = pkg.tokenize(cleaned_text)
    assert isinstance(my_list, list), "tokenize() failed on cleaned text"

    assert my_list == expected_list, "integration test failed on example text"

@pytest.mark.integration
def test_clean_text_integration_02():
    '''
    # Given a string _text_
    # When I pass _text_ to 'clean_text()' and then to 'count_words()'
    # Then I should get a python dictionary with the words of _text_ as keys,
    # and their counts as value AND
    # Every word should be lowercase and there should be no punctuation.
    '''
    my_string = "Hello! We are testing some of our functions today again. hello and goodbye!"
    expected_dict = {"hello":2,"we":1,"are":1,"testing":1,"some":1,"of":1,"our":1,
    "functions":1,"today":1,"again":1,"and":1,"goodbye":1}

    cleaned_text = pkg.clean_text(my_string)
    assert isinstance(cleaned_text, str), "clean_text() failed on my_string"
    my_dict = pkg.count_words(cleaned_text)
    assert isinstance(my_dict, dict), "count_words() failed on cleaned text"

    assert my_dict == expected_dict, "integration test failed on example text"
